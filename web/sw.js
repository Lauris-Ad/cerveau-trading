// Garde le quiz et les pages disponibles hors-ligne (réseau d'abord, cache en secours).
const CACHE = "cerveau-trading-v2";
const BASE = ["./", "index.html", "quiz.html", "questions.json", "episodes.json", "couverture.png", "manifest.webmanifest", "laurisverse.html"];
self.addEventListener("install", e => e.waitUntil(caches.open(CACHE).then(c => c.addAll(BASE)).then(() => self.skipWaiting())));
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET" || e.request.url.includes("/audio/")) return;
  e.respondWith(fetch(e.request).then(r => { const copie = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copie)); return r; })
    .catch(() => caches.match(e.request)));
});
