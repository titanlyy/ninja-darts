import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import { readFile } from 'node:fs/promises';

const app = await readFile(new URL('../js/app.js', import.meta.url), 'utf8');
const helpers = vm.runInNewContext(
  app.slice(app.indexOf('  const escapeHtml ='), app.indexOf('  const venueKey =')) +
  '\n({linkify, venueWebsite})', { URL },
);
const distance = vm.runInNewContext(
  '(' + app.match(/function distanceKm\([\s\S]*?\n  }/)[0] + ')',
);

test('scheme-less social links become HTTPS while unsafe protocols are rejected', () => {
  assert.equal(helpers.linkify('facebook.com/ForestDarts4'), 'https://facebook.com/ForestDarts4');
  assert.equal(helpers.linkify('//example.com/shop'), 'https://example.com/shop');
  assert.equal(helpers.linkify('javascript:alert(1)'), '#');
  assert.equal(helpers.linkify('data:text/html,test'), '#');
  assert.equal(helpers.linkify('/relative-unknown'), '#');
  assert.doesNotMatch(helpers.linkify('https://example.com/"><script>'), /[<>"]/);
});

test('a corporate policy is not labelled a venue website', () => {
  assert.equal(helpers.venueWebsite('https://www.segasammy.co.jp/en/socialmediapolicy/'), false);
  assert.equal(helpers.venueWebsite('https://www.xinyan-livehouse.sg'), true);
});

test('nearest-venue distance handles the date line and polar geography', () => {
  assert.equal(distance(1.3, 103.8, 1.3, 103.8), 0);
  assert.ok(Math.abs(distance(0, 179.9, 0, -179.9) - 22.239) < .01);
  assert.ok(distance(89, 0, 89, 180) < 223);
});
