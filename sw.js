/* Ninja Darts service worker — app-shell caching for offline/PWA use.
   Venues data is network-first (fresh data), falling back to cache. */

const CACHE = 'ninja-darts-v14-directory-ready';
const APP_SHELL = [
  './',
  './index.html',
  './css/style.css?v=14',
  './js/app.js?v=14',
  './vendor/leaflet/leaflet.js',
  './vendor/leaflet/leaflet.css',
  './vendor/markercluster/leaflet.markercluster.js',
  './vendor/markercluster/MarkerCluster.css',
  './icons/providers/dartslive.svg',
  './icons/providers/phoenix.png',
  './icons/providers/dartslive-symbol.png',
  './icons/providers/phoenix-symbol.png',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(APP_SHELL))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k.startsWith('ninja-darts-') && k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  // Leave third-party tiles/CDNs to browser caching and provider policies.
  if (url.origin !== self.location.origin || e.request.method !== 'GET') return;

  e.respondWith(networkFirst(e.request));
});

async function networkFirst(request) {
  let response;
  try {
    response = await fetch(request);
    if (response.ok) {
      try {
        const cache = await caches.open(CACHE);
        await cache.put(request, response.clone());
      } catch {
        // Storage exhaustion/private mode must not discard a valid response.
      }
      return response;
    }
  } catch {
    // A cached successful response is safer than an error response or no response.
  }
  const cached = await caches.match(request).catch(() => null);
  return cached || response || new Response('Offline: this resource has not been saved yet.', {
    status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
}
