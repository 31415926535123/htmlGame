// 缓存的版本
const VERSION = "v1";

// 缓存的名称
const CACHE_NAME = `snake-game-${VERSION}`;

// 使应用运作所需的静态资源
const APP_STATIC_RESOURCES = [
  "/",
  "/index.html",
  "/manifest.json",
  "/icons/favicon_16x16.png",
  "/icons/favicon_32x32.png",
  "/icons/favicon_48x48.png",
  "/icons/favicon_64x64.png",
  "/icons/favicon_128x128.png",
  "/icons/favicon_256x256.png",
  "/icons/favicon_512x512.png",

];

// 在安装时缓存静态资源
self.addEventListener("install", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(CACHE_NAME);
      cache.addAll(APP_STATIC_RESOURCES);
    })(),
  );
});

// 在被激活时删除旧的缓存
self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const names = await caches.keys();
      await Promise.all(
        names.map((name) => {
          if (name !== CACHE_NAME) {
            return caches.delete(name);
          }
        }),
      );
      await clients.claim();
    })(),
  );
});

// 在 fetch 时，拦截服务器请求并用缓存的响应内容进行响应而不流经网络
self.addEventListener("fetch", (event) => {
  // 作为一个单页应用，总是将应用定向到缓存的主页面
  if (event.request.mode === "navigate") {
    event.respondWith(caches.match("/index.html"));
    return;
  }

  // 对于其他所有请求，先找缓存，再去网络
  event.respondWith(
    (async () => {
      const cache = await caches.open(CACHE_NAME);
      const cachedResponse = await cache.match(event.request.url);
      if (cachedResponse) {
        // 如果有缓存的响应可用就将其返回
        return cachedResponse;
      } else {
        // 如果资源不在缓存中，返回 404
        return new Response(null, { status: 404 });
      }
    })(),
  );
});