/* Basic opt-in: no Google script/request before an explicit analytics choice. */
(() => {
  'use strict';
  const panel = document.getElementById('analytics-consent');
  if (!panel) return;
  const id = panel.dataset.measurementId;
  const key = 'analytics-consent-v1';
  const disabled = 'ga-disable-' + id;
  let loaded = false;
  let returnFocus;
  window[disabled] = true;
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  const denied = { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };
  window.gtag('consent', 'default', denied);
  function readChoice() {
    try {
      const saved = JSON.parse(localStorage.getItem(key));
      if (saved && saved.expires > Date.now() && ['allow', 'deny'].includes(saved.value)) return saved.value;
    } catch (_) { /* No storage: ask again next page. */ }
    return null;
  }
  function saveChoice(value) {
    try { localStorage.setItem(key, JSON.stringify({ value, expires: Date.now() + 180 * 86400000 })); } catch (_) {}
  }
  function clearAnalyticsCookies() {
    const names = document.cookie.split(';').map(c => c.trim().split('=')[0]).filter(n => /^_ga(?:_|$)|^_gid$|^_gat/.test(n));
    const domains = ['', location.hostname];
    const parts = location.hostname.split('.');
    for (let i = 0; i < parts.length - 1; i++) domains.push('.' + parts.slice(i).join('.'));
    for (const name of names) for (const domain of domains) {
      document.cookie = name + '=; Max-Age=0; path=/' + (domain ? '; domain=' + domain : '') + '; SameSite=Lax';
    }
  }
  function enable() {
    window[disabled] = false;
    if (loaded) return;
    loaded = true;
    window.gtag('consent', 'update', { ...denied, analytics_storage: 'granted' });
    window.gtag('js', new Date());
    window.gtag('config', id, { allow_google_signals: false, allow_ad_personalization_signals: false });
    const script = document.createElement('script');
    script.id = 'consented-google-analytics';
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(script);
  }
  function disable() {
    window[disabled] = true;
    window.gtag('consent', 'update', denied);
    clearAnalyticsCookies();
    // Remove the already-loaded Google runtime, including its event handlers.
    if (loaded) location.reload();
  }
  function close() {
    panel.hidden = true;
    if (returnFocus) returnFocus.focus();
  }
  document.querySelectorAll('[data-cookie-settings]').forEach(button => {
    button.addEventListener('click', () => {
      returnFocus = button;
      panel.hidden = false;
      panel.querySelector('[data-choice="deny"]').focus();
    });
  });
  panel.querySelectorAll('[data-choice]').forEach(button => {
    button.addEventListener('click', () => {
      const value = button.dataset.choice;
      saveChoice(value);
      if (value === 'allow') enable(); else disable();
      close();
    });
  });
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      // A revocation in another tab must also stop this tab's runtime.
      if (readChoice() !== 'allow') { disable(); panel.hidden = readChoice() === 'deny'; }
    }
  });
  window.addEventListener('pageshow', event => {
    if (event.persisted && readChoice() !== 'allow') disable();
  });
  const choice = readChoice();
  if (choice === 'allow') enable(); else clearAnalyticsCookies();
  panel.hidden = choice !== null;
})();
