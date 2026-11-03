/* Ninja Darts service worker — app-shell caching for offline/PWA use.
   Venues data is network-first (fresh data), falling back to cache. */

const CACHE = 'ninja-darts-v10-live-phoenix-feeds';
const APP_SHELL = [
  './',
  './index.html',
  './css/style.css?v=10',
  './js/app.js?v=10',
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
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  // Leave third-party tiles/CDNs to browser caching and provider policies.
  if (url.origin !== self.location.origin || e.request.method !== 'GET') return;

  // Venue data: network-first so the directory stays fresh
  if (url.pathname.includes('/data/')) {
    e.respondWith(
      fetch(e.request)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((cache) => cache.put(e.request, copy));
          return res;
        })
        .catch(() => caches.match(e.request))
    );
    return;
  }

  // App shell: network-first, so returning visitors receive the current build.
  e.respondWith(
    fetch(e.request).then((res) => {
          if (e.request.method === 'GET' && res.ok) {
            const copy = res.clone();
            caches.open(CACHE).then((cache) => cache.put(e.request, copy));
          }
          return res;
        }).catch(() => caches.match(e.request))
  );
});
