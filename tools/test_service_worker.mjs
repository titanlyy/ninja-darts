import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { readFile } from 'node:fs/promises';

const source = await readFile(new URL('../sw.js', import.meta.url), 'utf8');
function worker() {
  const events = {}, saved = new Map(), deleted = [];
  let network = async () => new Response('fresh');
  const key = (request) => request.url || request;
  const caches = {
    async open() {
      return {
        async put(request, response) { saved.set(key(request), response.clone()); },
        async addAll() {},
      };
    },
    async match(request) { return saved.get(key(request))?.clone(); },
    async keys() { return ['ninja-darts-v10-old', 'ninja-darts-v11-directory-ready', 'another-app-v1']; },
    async delete(name) { deleted.push(name); },
  };
  const self = {
    location: { origin: 'https://titanlyy.github.io' },
    addEventListener: (type, callback) => { events[type] = callback; },
    skipWaiting() {}, clients: { async claim() {} },
  };
  vm.runInNewContext(source, { self, caches, URL, Response, fetch: (...args) => network(...args) });
  return {
    events, deleted, saved,
    setNetwork(fn) { network = fn; },
    fetch(url = 'https://titanlyy.github.io/ninja-darts/data/sg.json') {
      let response;
      events.fetch({ request: new Request(url), respondWith(value) { response = value; } });
      return response;
    },
  };
}

test('successful data survives offline and HTTP 500 without cache poisoning', async () => {
  const w = worker();
  w.setNetwork(async () => new Response('valid venue data', { status: 200 }));
  assert.equal(await (await w.fetch()).text(), 'valid venue data');
  w.setNetwork(async () => new Response('server error', { status: 500 }));
  assert.equal(await (await w.fetch()).text(), 'valid venue data');
  w.setNetwork(async () => { throw new Error('offline'); });
  assert.equal(await (await w.fetch()).text(), 'valid venue data');
});

test('an uncached offline resource returns a useful response, not undefined', async () => {
  const w = worker();
  w.setNetwork(async () => { throw new Error('offline'); });
  const response = await w.fetch();
  assert.equal(response.status, 503);
  assert.match(await response.text(), /not been saved/);
});

test('map tiles and other third-party requests are never intercepted', () => {
  assert.equal(worker().fetch('https://tile.openstreetmap.org/3/1/2.png'), undefined);
});

test('activation leaves unrelated applications caches intact', async () => {
  const w = worker();
  let completion;
  w.events.activate({ waitUntil(promise) { completion = promise; } });
  await completion;
  assert.deepEqual(w.deleted, ['ninja-darts-v10-old']);
});
