/* ═══════════════════════════════════════════════════════════
   NINJA DARTS — map application
   Static SPA · Leaflet · marker clustering · lazy country data
   Designed to be wrappable by Capacitor (Android/iOS) later.
   ═══════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  // ── State ─────────────────────────────────────────────────
  const state = {
    countries: [],   // from data/index.json
    venues: [],      // all loaded venues
    markers: new Map(), // venue.id -> marker
    selected: null,  // selected country code ('all' default)
    query: '',
    leagueOnly: false,
    dl3Only: false,
  };

  // ── Elements ──────────────────────────────────────────────
  const $ = (id) => document.getElementById(id);
  const els = {
    map: $('map'),
    sidebar: $('sidebar'),
    sidebarToggle: $('sidebar-toggle'),
    search: $('search'),
    league: $('f-league'),
    dl3: $('f-dl3'),
    nearMe: $('near-me'),
    countryList: $('country-list'),
    venueCount: $('venue-count'),
    detail: $('detail'),
    detailBody: $('detail-body'),
    detailClose: $('detail-close'),
    toast: $('toast'),
  };

  // ── Map ───────────────────────────────────────────────────
  const map = L.map(els.map, {
    zoomControl: false,
    attributionControl: true,
  }).setView([25, 30], 2);

  L.control.zoom({ position: 'bottomleft' }).addTo(map);

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> contributors',
    maxZoom: 19,
  }).addTo(map);

  const clusterGroup = L.markerClusterGroup({
    chunkedLoading: true,
    maxClusterRadius: 55,
    spiderfyOnMaxZoom: true,
    showCoverageOnHover: false,
    iconCreateFunction: (cluster) =>
      L.divIcon({
        html: `<div class="mcluster">${cluster.getChildCount()}</div>`,
        className: 'mcluster-wrap',
        iconSize: [38, 38],
      }),
  });
  map.addLayer(clusterGroup);

  const markerIcon = (league) =>
    L.divIcon({
      html:
        '<div class="venue-marker' + (league ? ' league' : '') + '">' +
        '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#141210" stroke-width="3" stroke-linecap="round"><path d="M20 4L8 16"/><circle cx="5" cy="19" r="2.5" fill="#141210" stroke="none"/></svg>' +
        '</div>',
      className: 'venue-marker-wrap',
      iconSize: [26, 26],
      iconAnchor: [13, 26],
      popupAnchor: [0, -14],
    });

  // ── Helpers ───────────────────────────────────────────────
  const flag = (cc) =>
    String.fromCodePoint(
      ...[...cc.toUpperCase()].map((c) => 0x1f1e6 + c.charCodeAt(0) - 65)
    );

  const escapeHtml = (s) =>
    String(s == null ? '' : s)
      .replace(/&/g, '&' + 'amp;')
      .replace(/</g, '&' + 'lt;')
      .replace(/>/g, '&' + 'gt;')
      .replace(/"/g, '&' + 'quot;')
      .replace(/'/g, '&' + '#39;');

  const linkify = (s) =>
    /^https?:\/\//.test(s) ? escapeHtml(s) : 'https://' + escapeHtml(s);

  // Break business-hours strings into one line per day for readability
  const prettyHours = (h) =>
    String(h)
      .replace(/(Sun|Mon|Tue|Wed|Thu|Fri|Sat|Holiday|祝日)\s*/g, '$1 ')
      .replace(/(?=(Sun|Mon|Tue|Wed|Thu|Fri|Sat|Holiday) )/g, '\n')
      .replace(/\n+/g, '\n')
      .trim();

  let toastTimer;
  function toast(msg) {
    els.toast.textContent = msg;
    els.toast.classList.remove('hidden');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => els.toast.classList.add('hidden'), 2600);
  }

  // ── Data loading ──────────────────────────────────────────
  async function boot() {
    try {
      const res = await fetch('data/index.json');
      state.countries = await res.json();
      renderCountryList();
      await Promise.all(
        state.countries.map((c) =>
          fetch(`data/${c.cc}.json`)
            .then((r) => r.json())
            .then((venues) => {
              venues.forEach((v) => {
                v.cc = c.cc;
                state.venues.push(v);
              });
            })
        )
      );
      buildMarkers();
      els.venueCount.textContent =
        state.venues.length.toLocaleString() +
        ' venues · ' +
        state.countries.length +
        (state.countries.length === 1 ? ' country' : ' countries');
    } catch (err) {
      console.error(err);
      els.venueCount.textContent = 'Failed to load venue data';
      toast('Could not load venue data. Check your connection.');
    }
  }

  function renderCountryList() {
    const frag = document.createDocumentFragment();

    const all = document.createElement('button');
    all.className = 'country-item active';
    all.dataset.cc = 'all';
    all.innerHTML =
      '<span class="flag">🌍</span><span class="cc-name">All countries</span>' +
      '<span class="cc-count">' +
      state.countries.reduce((n, c) => n + c.count, 0).toLocaleString() +
      '</span><svg class="cc-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M20 6L9 17l-5-5"/></svg>';
    frag.appendChild(all);

    state.countries.forEach((c) => {
      const b = document.createElement('button');
      b.className = 'country-item';
      b.dataset.cc = c.cc;
      b.innerHTML =
        `<span class="flag">${flag(c.cc)}</span><span class="cc-name">${escapeHtml(c.name)}</span>` +
        `<span class="cc-count">${c.count.toLocaleString()}</span>` +
        '<svg class="cc-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M20 6L9 17l-5-5"/></svg>';
      frag.appendChild(b);
    });

    els.countryList.innerHTML = '';
    els.countryList.appendChild(frag);

    els.countryList.addEventListener('click', (e) => {
      const item = e.target.closest('.country-item');
      if (!item) return;
      selectCountry(item.dataset.cc);
    });
  }

  function selectCountry(cc) {
    state.selected = cc;
    els.countryList.querySelectorAll('.country-item').forEach((el) => {
      const active = el.dataset.cc === cc;
      el.classList.toggle('active', active);
      el.classList.toggle('selected', active);
    });
    if (cc === 'all') {
      map.setView([25, 30], 2);
    } else {
      const c = state.countries.find((x) => x.cc === cc);
      if (c) map.fitBounds(c.bounds, { padding: [40, 40], maxZoom: 11 });
    }
    applyFilters();
  }

  // ── Markers ───────────────────────────────────────────────
  function buildMarkers() {
    state.venues.forEach((v) => {
      const m = L.marker([v.la, v.lo], { icon: markerIcon(v.L) });
      m.on('click', () => showDetail(v));
      state.markers.set(v.id, m);
    });
    clusterGroup.addLayers([...state.markers.values()]);
  }

  function matchesFilters(v) {
    if (state.selected !== 'all' && v.cc !== state.selected) return false;
    if (state.leagueOnly && !v.L) return false;
    if (state.dl3Only && !v.d3) return false;
    if (state.query) {
      const hay = (v.n + ' ' + v.a + ' ' + v.g + ' ' + (v.st || '')).toLowerCase();
      if (!hay.includes(state.query)) return false;
    }
    return true;
  }

  function applyFilters() {
    let shown = 0;
    state.venues.forEach((v) => {
      const m = state.markers.get(v.id);
      if (!m) return;
      const keep = matchesFilters(v);
      if (keep) shown++;
      if (keep !== clusterGroup.hasLayer(m)) {
        keep ? clusterGroup.addLayer(m) : clusterGroup.removeLayer(m);
      }
    });
    els.venueCount.textContent =
      shown.toLocaleString() +
      (shown === state.venues.length && state.selected === 'all'
        ? ' venues · ' + state.countries.length + (state.countries.length === 1 ? ' country' : ' countries')
        : ' venues shown');
  }

  // ── Detail panel ──────────────────────────────────────────
  function showDetail(v) {
    const machines = [];
    if (v.d3) machines.push({ num: v.d3, lbl: 'DARTSLIVE3' });
    if (v.d2) machines.push({ num: v.d2, lbl: 'DARTSLIVE2' });

    const badges = [];
    if (v.L) badges.push('<span class="badge league">League Venue</span>');
    if (v.C) badges.push('<span class="badge campaign">Campaign</span>');
    if (v.g) badges.push(`<span class="badge genre">${escapeHtml(v.g)}</span>`);

    const socials = [];
    if (v.w) socials.push(`<a href="${linkify(v.w)}" target="_blank" rel="noopener">Website</a>`);
    if (v.ig) socials.push(`<a href="${linkify(v.ig)}" target="_blank" rel="noopener">Instagram</a>`);
    if (v.tw) socials.push(`<a href="${linkify(v.tw)}" target="_blank" rel="noopener">X / Twitter</a>`);
    if (v.fb) socials.push(`<a href="${linkify(v.fb)}" target="_blank" rel="noopener">Facebook</a>`);

    const directions = `https://www.google.com/maps/dir/?api=1&destination=${v.la},${v.lo}`;

    els.detailBody.innerHTML = `
      <div class="detail-header">
        <div class="detail-badges">${badges.join('')}</div>
        <h2 class="detail-title">${escapeHtml(v.n)}</h2>
        <p class="detail-sub">${flag(v.cc)} ${escapeHtml(v.a || '')}</p>
      </div>
      ${machines.length ? `
      <div class="detail-section">
        <h3>Machines</h3>
        <div class="machines">
          ${machines.map((m) => `<div class="machine-card"><div class="num">${m.num}</div><div class="lbl">${m.lbl}</div></div>`).join('')}
        </div>
      </div>` : ''}
      ${v.h ? `
      <div class="detail-section">
        <h3>Business Hours</h3>
        <p class="detail-hours">${escapeHtml(prettyHours(v.h))}</p>
      </div>` : ''}
      ${v.st ? `
      <div class="detail-section">
        <h3>Nearest Station</h3>
        <p>${escapeHtml(v.st)}</p>
      </div>` : ''}
      ${socials.length ? `
      <div class="detail-section">
        <h3>Links</h3>
        <div class="social-links">${socials.join('')}</div>
      </div>` : ''}
      <div class="detail-actions">
        <a class="btn primary" href="${directions}" target="_blank" rel="noopener">Directions</a>
        <a class="btn" href="${escapeHtml(v.url)}" target="_blank" rel="noopener">DARTSLIVE Page</a>
      </div>
    `;

    els.detail.classList.remove('hidden');
    els.detail.setAttribute('aria-hidden', 'false');
  }

  // ── Events ────────────────────────────────────────────────
  let debounce;
  els.search.addEventListener('input', (e) => {
    clearTimeout(debounce);
    debounce = setTimeout(() => {
      state.query = e.target.value.trim().toLowerCase();
      applyFilters();
    }, 220);
  });

  els.league.addEventListener('change', (e) => {
    state.leagueOnly = e.target.checked;
    applyFilters();
  });

  els.dl3.addEventListener('change', (e) => {
    state.dl3Only = e.target.checked;
    applyFilters();
  });

  els.detailClose.addEventListener('click', () => {
    els.detail.classList.add('hidden');
    els.detail.setAttribute('aria-hidden', 'true');
  });

  els.sidebarToggle.addEventListener('click', () => {
    const collapsed = els.sidebar.classList.toggle('collapsed');
    document.body.classList.toggle('sb-collapsed', collapsed);
    els.sidebarToggle.setAttribute('aria-expanded', String(!collapsed));
    setTimeout(() => map.invalidateSize(), 200);
  });

  els.nearMe.addEventListener('click', () => {
    if (!navigator.geolocation) {
      toast('Geolocation is not supported by this browser');
      return;
    }
    toast('Finding your location…');
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const { latitude: la, longitude: lo } = pos.coords;
        state.selected = 'all';
        els.countryList.querySelectorAll('.country-item').forEach((el) => {
          const active = el.dataset.cc === 'all';
          el.classList.toggle('active', active);
          el.classList.toggle('selected', active);
        });
        state.query = '';
        els.search.value = '';
        state.leagueOnly = false;
        state.dl3Only = false;
        els.league.checked = false;
        els.dl3.checked = false;
        applyFilters();

        const near = state.venues
          .map((v) => ({
            v,
            d: Math.hypot(v.la - la, (v.lo - lo) * Math.cos((la * Math.PI) / 180)) * 111.32,
          }))
          .sort((a, b) => a.d - b.d)
          .slice(0, 50);

        if (!near.length) {
          toast('No venues found near you');
          return;
        }

        // show only the nearest 50
        const nearIds = new Set(near.map((x) => x.v.id));
        state.markers.forEach((m, id) => {
          const keep = nearIds.has(id);
          if (keep !== clusterGroup.hasLayer(m)) {
            keep ? clusterGroup.addLayer(m) : clusterGroup.removeLayer(m);
          }
        });

        map.setView([la, lo], 11);
        toast(`${near.length} venues near you · closest: ${near[0].v.n} (${near[0].d.toFixed(1)} km)`);
        showDetail({ ...near[0].v, n: `${near[0].v.n} — ${near[0].d.toFixed(1)} km away` });
      },
      () => toast('Could not get your location. Check permissions.'),
      { enableHighAccuracy: false, timeout: 10000 }
    );
  });

  // Keyboard: Esc closes detail
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      els.detail.classList.add('hidden');
    }
  });

  // ── Service worker (PWA) ──────────────────────────────────
  // try/catch: accessing navigator.serviceWorker throws inside sandboxed
  // iframes (e.g. cross-origin previews); the app must still boot.
  try {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('sw.js').catch(() => {});
    }
  } catch (e) {
    /* sandboxed context — PWA install unavailable, app still works */
  }

  boot();
})();
