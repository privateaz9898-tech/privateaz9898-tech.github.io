const CACHE = 'the-rizen-public-v11';
const SHELL = ['./', './index.html', './styles.css', './app.js', './db.js', './manifest.webmanifest', './assets/rizen-crown.svg', './assets/adan-unfiltered-dark-tactical.png'];

self.addEventListener('install', (event) => event.waitUntil(caches.open(CACHE).then((cache) => cache.addAll(SHELL))));
self.addEventListener('activate', (event) => event.waitUntil(self.clients.claim()));
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin || url.pathname.includes('/api/')) return;
  const shellPath = /\/(?:$|index\.html$|styles\.css$|app\.js$|db\.js$|manifest\.webmanifest$)/.test(url.pathname);
  if (shellPath) {
    event.respondWith(fetch(event.request).then((response) => {
      const copy = response.clone(); caches.open(CACHE).then((cache) => cache.put(event.request, copy)); return response;
    }).catch(() => caches.match(event.request)));
    return;
  }
  event.respondWith(caches.match(event.request).then((cached) => cached || fetch(event.request).then((response) => {
    const copy = response.clone(); caches.open(CACHE).then((cache) => cache.put(event.request, copy)); return response;
  })));
});
