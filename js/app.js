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
    selected: 'sg',
    defaultCountry: 'sg',
    provider: 'all',
    region: '',
    area: '',
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
    provider: $('provider'),
    locationFilter: $('location-filter'),
    locationHeading: $('location-heading'),
    region: $('geo-region'),
    area: $('geo-area'),
    regionLabel: $('region-label'),
    areaLabel: $('area-label'),
    areaControl: $('area-control'),
    countryList: $('country-list'),
    countryContext: $('country-context'),
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

  // Screen-pixel grouping distance. Lower values keep more venue pins separate.
  const CLUSTER_RADIUS_PX = 28;
  const clusterGroup = L.markerClusterGroup({
    chunkedLoading: true,
    maxClusterRadius: CLUSTER_RADIUS_PX,
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

  const providerLogo = (provider) =>
    `<img src="icons/providers/${provider === 'phoenix' ? 'phoenix.png' : 'dartslive.svg'}" alt="${provider === 'phoenix' ? 'Phoenix Darts' : 'DARTSLIVE'}" />`;
  const providerSymbol = (provider) =>
    `<img src="icons/providers/${provider === 'phoenix' ? 'phoenix' : 'dartslive'}-symbol.png" alt="${provider === 'phoenix' ? 'Phoenix Darts' : 'DARTSLIVE'}" />`;

  const markerIcon = (venue) =>
    L.divIcon({
      html:
        '<div class="provider-marker' + (venue.providers.length > 1 ? ' dual' : '') + '">' +
        venue.providers.map(providerSymbol).join('') +
        '</div>',
      className: 'venue-marker-wrap',
      iconSize: [38, 40],
      iconAnchor: [19, 40],
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
    /^https?:\/\//i.test(s) ? escapeHtml(s) : '#';

  const venueKey = (v) => `${v.cc}:${v.id}`;

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
  async function detectCountry() {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 2500);
    try {
      const response = await fetch('https://api.country.is/', {
        signal: controller.signal, credentials: 'omit', referrerPolicy: 'no-referrer', cache: 'no-store',
      });
      if (!response.ok) return null;
      const country = (await response.json()).country;
      return typeof country === 'string' && /^[A-Z]{2}$/i.test(country) ? country.toLowerCase() : null;
    } catch {
      return null;
    } finally {
      clearTimeout(timeout);
    }
  }

  async function boot() {
    try {
      // Starts alongside venue downloads; never requests precise browser location.
      const countryHintPromise = detectCountry();
      const res = await fetch('data/index.json');
      state.countries = await res.json();
      await Promise.all(
        state.countries.map((c) =>
          fetch(`data/${c.cc}.json`)
            .then((r) => r.json())
            .then((venues) => {
              venues.forEach((v) => {
                v.cc = c.cc;
                v.providers = ['dartslive'];
                v.sources = [{ provider: 'dartslive', id: v.id, url: v.url }];
                state.venues.push(v);
              });
            })
        )
      );
      // Additive pilot feed: preserve the original DARTSLIVE source records.
      let pilot = { venues: [] };
      try {
        const pilotResponse = await fetch('data/phoenix-sg.json');
        if (!pilotResponse.ok) throw new Error('Phoenix pilot data unavailable');
        pilot = await pilotResponse.json();
      } catch (error) {
        toast('Phoenix pilot could not load. DARTSLIVE venues are still available.');
      }
      pilot.venues.forEach((p) => {
        if (p.directory_eligible === false) return;
        const existing = p.dartslive_id
          ? state.venues.find((v) => v.cc === 'sg' && v.id === p.dartslive_id)
          : null;
        const source = { provider: 'phoenix', id: p.source_id, url: p.source_url, collected_at: p.collected_at };
        if (existing) {
          existing.providers.push('phoenix');
          existing.sources.push(source);
          existing.phoenix_machines = p.machines;
          existing.phoenix_name = p.name;
        } else if (p.map_eligible) {
          state.venues.push({
            id: `phoenix-${p.source_id}`, cc: 'sg', n: p.name, a: p.address,
            la: p.latitude, lo: p.longitude, g: '', h: '', st: '', d2: null, d3: null,
            L: false, C: false, providers: ['phoenix'], sources: [source],
            phoenix_machines: p.machines,
          });
        }
      });
      try {
        const locationsResponse = await fetch('data/locations.json');
        if (!locationsResponse.ok) throw new Error('Location metadata unavailable');
        const locations = await locationsResponse.json();
        state.venues.forEach((v) => {
          const location = locations.countries[v.cc]?.[v.id];
          v.region = location?.region || '';
          v.area = location?.area || '';
        });
      } catch (error) {
        toast('City filters could not load. Country browsing is still available.');
      }
      state.countries.forEach((c) => {
        const venues = state.venues.filter((v) => v.cc === c.cc);
        c.count = venues.length;
        c.bounds = [
          [Math.min(...venues.map((v) => v.la)), Math.min(...venues.map((v) => v.lo))],
          [Math.max(...venues.map((v) => v.la)), Math.max(...venues.map((v) => v.lo))],
        ];
      });
      const ipCountry = await countryHintPromise;
      const mappedCountry = ipCountry === 'mo' ? 'hk' : ipCountry;
      const supported = state.countries.some((c) => c.cc === mappedCountry);
      state.defaultCountry = supported ? mappedCountry : 'sg';
      state.countries.sort((a, b) =>
        Number(b.cc === state.defaultCountry) - Number(a.cc === state.defaultCountry) ||
        b.count - a.count || a.name.localeCompare(b.name));
      const defaultName = state.countries.find((c) => c.cc === state.defaultCountry).name;
      els.countryContext.innerHTML = supported
        ? `IP estimate: ${escapeHtml(defaultName)} · <a href="https://country.is/" target="_blank" rel="noopener">Country.is</a>`
        : `Singapore default · <a href="https://country.is/" target="_blank" rel="noopener">IP country unavailable or not listed</a>`;
      els.countryContext.title = 'Country is approximate and may reflect a VPN. Change country anytime. The lookup provider receives your IP; this app does not store it.';
      renderCountryList();
      buildMarkers();
      selectCountry(state.defaultCountry, { scroll: false });
      if (matchMedia('(max-width: 768px)').matches) {
        els.sidebar.classList.add('collapsed');
        document.body.classList.add('sb-collapsed');
        els.sidebarToggle.setAttribute('aria-expanded', 'false');
      }
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

  function selectCountry(cc, { scroll = true } = {}) {
    state.selected = cc;
    state.region = '';
    state.area = '';
    closeDetail();
    els.countryList.querySelectorAll('.country-item').forEach((el) => {
      const active = el.dataset.cc === cc;
      el.classList.toggle('active', active);
      el.classList.toggle('selected', active);
    });
    renderLocationFilters();
    if (scroll && !els.locationFilter.classList.contains('hidden')) {
      els.countryList.querySelector(`[data-cc="${cc}"]`)?.scrollIntoView({ block: 'start' });
    }
    if (cc === 'all') {
      map.setView([25, 30], 2);
    } else {
      const c = state.countries.find((x) => x.cc === cc);
      if (c) map.fitBounds(c.bounds, { padding: [48, 48], maxZoom: 11, animate: false });
    }
    applyFilters();
  }

  const missingLocation = '__missing__';
  const regionKey = (v) => v.region || missingLocation;
  const areaKey = (v) => JSON.stringify([v.region || '', v.area || '']);
  const geoLabels = {
    jp: ['Prefecture', 'City / district'],
    fr: ['Region', 'Department'],
    us: ['State', 'City'],
    ca: ['Province', 'City'],
    au: ['State / territory', 'City / locality'],
    tw: ['City / county', 'Area'],
    cn: ['Region', 'Province / municipality'],
    my: ['Region', 'State / territory'],
    hk: ['Region', 'District'],
  };

  function fillLocationOptions(select, items, allLabel, value) {
    select.replaceChildren(new Option(allLabel, ''));
    items.sort((a, b) => b.count - a.count || a.name.localeCompare(b.name))
      .forEach((item) => select.add(new Option(`${item.name} (${item.count.toLocaleString()})`, item.key)));
    select.value = value;
  }

  function renderLocationFilters() {
    const venues = state.venues.filter((v) => v.cc === state.selected);
    const providerVenues = venues.filter(matchesProvider);
    const regionGroups = new Map();
    venues.forEach((v) => {
      const key = regionKey(v);
      if (!regionGroups.has(key)) regionGroups.set(key, { key, name: v.region || 'Not provided', count: 0 });
      if (matchesProvider(v)) regionGroups.get(key).count++;
    });
    const hasGeography = state.selected !== 'sg' && venues.some((v) => v.region || v.area);
    els.locationFilter.classList.toggle('hidden', !hasGeography);
    if (!hasGeography) return;
    const country = state.countries.find((c) => c.cc === state.selected);
    const selectedButton = els.countryList.querySelector(`[data-cc="${state.selected}"]`);
    selectedButton.after(els.locationFilter);
    els.locationHeading.textContent = `Explore ${country.name}`;
    const [regionLabel, areaLabel] = geoLabels[state.selected] || ['Region', 'City / area'];
    els.regionLabel.textContent = regionLabel;
    els.areaLabel.textContent = areaLabel;
    fillLocationOptions(els.region, [...regionGroups.values()], `All (${providerVenues.length.toLocaleString()} venues)`, state.region);
    const areaVenues = venues.filter((v) => !state.region || regionKey(v) === state.region);
    const areaGroups = new Map();
    areaVenues.forEach((v) => {
      const key = areaKey(v);
      const suffix = !state.region && v.region ? ` · ${v.region}` : '';
      if (!areaGroups.has(key)) areaGroups.set(key, { key, name: (v.area || 'Not provided') + suffix, count: 0 });
      if (matchesProvider(v)) areaGroups.get(key).count++;
    });
    els.areaControl.classList.toggle('hidden', !areaVenues.some((v) => v.area));
    fillLocationOptions(els.area, [...areaGroups.values()], `All (${areaVenues.filter(matchesProvider).length.toLocaleString()} venues)`, state.area);
    els.locationFilter.querySelector('.location-note').textContent = state.provider === 'all'
      ? 'Counts across all providers' : `Counts for ${state.provider === 'phoenix' ? 'Phoenix' : 'DARTSLIVE'}`;
  }

  function focusGeography() {
    const venues = state.venues.filter((v) => v.cc === state.selected &&
      (!state.region || regionKey(v) === state.region) && (!state.area || areaKey(v) === state.area));
    map.stop();
    if (venues.length) map.fitBounds(venues.map((v) => [v.la, v.lo]), { padding: [48, 48], maxZoom: 14, animate: false });
    closeDetail();
    applyFilters();
  }

  // ── Markers ───────────────────────────────────────────────
  function matchesProvider(v) {
    return state.provider === 'all' || v.providers.includes(state.provider);
  }

  function updateProviderNavigation() {
    const counts = new Map(state.countries.map((c) => [c.cc, 0]));
    let total = 0;
    state.venues.forEach((v) => {
      if (!matchesProvider(v)) return;
      counts.set(v.cc, (counts.get(v.cc) || 0) + 1);
      total++;
    });
    const scrollTop = els.countryList.scrollTop;
    els.countryList.querySelector('[data-cc="all"] .cc-count').textContent = total.toLocaleString();
    [...state.countries].sort((a, b) =>
      Number(b.cc === state.defaultCountry) - Number(a.cc === state.defaultCountry) ||
      counts.get(b.cc) - counts.get(a.cc) || a.name.localeCompare(b.name)
    ).forEach((c) => {
      const button = els.countryList.querySelector(`[data-cc="${c.cc}"]`);
      button.querySelector('.cc-count').textContent = counts.get(c.cc).toLocaleString();
      els.countryList.appendChild(button);
    });
    renderLocationFilters();
    els.countryList.scrollTop = scrollTop;
  }

  function buildMarkers() {
    state.venues.forEach((v) => {
      const m = L.marker([v.la, v.lo], {
        icon: markerIcon(v), title: `${v.n} · ${v.providers.join(' + ')}`,
        alt: `${v.n} · ${v.providers.join(' + ')}`,
      });
      m.on('add', () => m.getElement()?.setAttribute('aria-label', `${v.n} · ${v.providers.join(' + ')}`));
      m.on('click', () => showDetail(v));
      state.markers.set(venueKey(v), m);
    });
    clusterGroup.addLayers([...state.markers.values()]);
  }

  function matchesFilters(v) {
    if (state.selected !== 'all' && v.cc !== state.selected) return false;
    if (state.region && regionKey(v) !== state.region) return false;
    if (state.area && areaKey(v) !== state.area) return false;
    if (!matchesProvider(v)) return false;
    if (state.leagueOnly && !v.L) return false;
    if (state.dl3Only && !v.d3) return false;
    if (state.query) {
      const hay = (v.n + ' ' + (v.phoenix_name || '') + ' ' + v.a + ' ' + v.g + ' ' + (v.st || '') + ' ' + (v.region || '') + ' ' + (v.area || '')).toLowerCase();
      if (!hay.includes(state.query)) return false;
    }
    return true;
  }

  function applyFilters() {
    if (selectedVenue && !matchesFilters(selectedVenue)) closeDetail();
    let shown = 0;
    state.venues.forEach((v) => {
      const m = state.markers.get(venueKey(v));
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
    if (!shown) toast('No matching venues. Try another provider, country or search.');
    else if (els.toast.textContent.startsWith('No matching venues.')) els.toast.classList.add('hidden');
  }

  // ── Detail panel ──────────────────────────────────────────
  let selectedVenue = null;
  let selectedPin = null;
  let selectedZoom = 16;
  let focusFrame = 0;

  function closeDetail() {
    selectedVenue = null;
    if (selectedPin) map.removeLayer(selectedPin);
    selectedPin = null;
    els.detail.classList.add('hidden');
    els.detail.setAttribute('aria-hidden', 'true');
  }

  function focusSelectedVenue() {
    if (!selectedVenue || els.detail.classList.contains('hidden')) return;
    map.invalidateSize({ pan: false });
    const bounds = els.map.getBoundingClientRect();
    const card = els.detail.getBoundingClientRect();
    const mobile = window.matchMedia('(max-width: 768px)').matches;
    const left = 16;
    const right = mobile ? bounds.width - 16 : Math.max(100, card.left - bounds.left - 20);
    const top = 76;
    const bottom = mobile ? Math.max(top + 64, card.top - bounds.top - 20) : bounds.height - 48;
    const target = L.point((left + right) / 2, (top + bottom) / 2);
    const centre = L.point(bounds.width / 2, bounds.height / 2);
    map.stop();
    map.setView([selectedVenue.la, selectedVenue.lo], selectedZoom, { animate: false });
    map.panBy(centre.subtract(target), { animate: false });
  }

  function queueSelectedFocus() {
    cancelAnimationFrame(focusFrame);
    focusFrame = requestAnimationFrame(focusSelectedVenue);
  }

  // Reposition for card size changes, browser chrome/orientation and drawer resizing.
  const selectionLayoutObserver = new ResizeObserver(() => {
    if (selectedVenue) queueSelectedFocus();
  });
  selectionLayoutObserver.observe(els.detail);
  selectionLayoutObserver.observe(els.map);

  function showDetail(v, options = {}) {
    closeDetail();
    selectedVenue = v;
    selectedZoom = options.nearMe ? 16 : Math.max(16, map.getZoom());
    selectedPin = L.marker([v.la, v.lo], {
      icon: markerIcon(v), zIndexOffset: 2000, keyboard: false, interactive: false,
    }).addTo(map);
    selectedPin.getElement().classList.add('selected-venue');
    selectedPin.bindTooltip(
      `<span>Selected venue</span><strong>${escapeHtml(v.n)}</strong>`,
      { permanent: true, direction: 'top', offset: [0, -48], className: 'selected-venue-label', opacity: 1 }
    );
    if (window.matchMedia('(max-width: 1024px)').matches) {
      els.sidebar.classList.add('collapsed');
      document.body.classList.add('sb-collapsed');
      els.sidebarToggle.setAttribute('aria-expanded', 'false');
    }
    const machines = [];
    if (v.d3) machines.push({ num: v.d3, lbl: 'DARTSLIVE3' });
    if (v.d2) machines.push({ num: v.d2, lbl: 'DARTSLIVE2' });
    (v.phoenix_machines || []).forEach((m) => machines.push({ num: m.count, lbl: `Phoenix ${m.model}` }));

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
        <div class="detail-provider-logos">${v.providers.map(providerLogo).join('')}</div>
        <div class="detail-badges">${badges.join('')}</div>
        <h2 class="detail-title">${escapeHtml(v.n)}</h2>
        ${Number.isFinite(options.distanceKm) ? `<p class="detail-distance">Closest venue · ${options.distanceKm.toFixed(1)} km away</p>` : ''}
        <p class="detail-sub">${flag(v.cc)} ${escapeHtml(v.a || '')}</p>
      </div>
      ${v.providers.includes('phoenix') && !(v.phoenix_machines || []).length ? '<p class="detail-sub">Phoenix machine inventory not published.</p>' : ''}
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
        ${v.sources.map((source) => `<a class="btn" href="${linkify(source.url)}" target="_blank" rel="noopener">${source.provider === 'phoenix' ? 'Phoenix' : 'DARTSLIVE'} Page</a>`).join('')}
      </div>
      <p class="source-note">Provider listings are not a guarantee of current operation or machine availability. Confirm opening hours and visitor access with the venue; some clubs may require membership.${v.sources.filter((s) => s.collected_at).map((s) => ' Phoenix collected ' + escapeHtml(s.collected_at.slice(0, 10)) + '.').join('')}</p>
    `;

    els.detail.classList.remove('hidden');
    els.detail.setAttribute('aria-hidden', 'false');
    els.detail.scrollTop = 0;
    queueSelectedFocus();
  }

  // ── Events ────────────────────────────────────────────────
  let debounce;
  els.region.addEventListener('change', () => {
    state.region = els.region.value;
    state.area = '';
    renderLocationFilters();
    focusGeography();
  });
  els.area.addEventListener('change', () => {
    state.area = els.area.value;
    focusGeography();
  });
  function syncProviderButtons() {
    els.provider.querySelectorAll('[data-provider]').forEach((button) =>
      button.setAttribute('aria-pressed', String(button.dataset.provider === state.provider))
    );
    updateProviderNavigation();
  }
  els.provider.addEventListener('click', (e) => {
    const button = e.target.closest('[data-provider]');
    if (!button) return;
    state.provider = button.dataset.provider;
    syncProviderButtons();
    closeDetail();
    applyFilters();
  });
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

  els.detailClose.addEventListener('click', closeDetail);

  els.sidebarToggle.addEventListener('click', () => {
    const collapsed = els.sidebar.classList.toggle('collapsed');
    document.body.classList.toggle('sb-collapsed', collapsed);
    els.sidebarToggle.setAttribute('aria-expanded', String(!collapsed));
    setTimeout(() => {
      map.invalidateSize();
      if (selectedVenue) queueSelectedFocus();
    }, 200);
  });

  els.nearMe.addEventListener('click', () => {
    if (!navigator.geolocation) {
      toast('Geolocation is not supported by this browser');
      return;
    }
    toast('Finding your location…');
    els.nearMe.disabled = true;
    els.nearMe.setAttribute('aria-busy', 'true');
    els.nearMe.querySelector('span').textContent = 'Locating…';
    const finishLocationRequest = () => {
      els.nearMe.disabled = false;
      els.nearMe.removeAttribute('aria-busy');
      els.nearMe.querySelector('span').textContent = 'Near me';
    };
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        finishLocationRequest();
        clearTimeout(debounce);
        const { latitude: la, longitude: lo } = pos.coords;
        state.selected = 'all';
        state.region = '';
        state.area = '';
        renderLocationFilters();
        els.countryList.querySelectorAll('.country-item').forEach((el) => {
          const active = el.dataset.cc === 'all';
          el.classList.toggle('active', active);
          el.classList.toggle('selected', active);
        });
        state.query = '';
        els.search.value = '';
        state.leagueOnly = false;
        state.dl3Only = false;
        state.provider = 'all';
        syncProviderButtons();
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
        const nearIds = new Set(near.map((x) => venueKey(x.v)));
        state.markers.forEach((m, id) => {
          const keep = nearIds.has(id);
          if (keep !== clusterGroup.hasLayer(m)) {
            keep ? clusterGroup.addLayer(m) : clusterGroup.removeLayer(m);
          }
        });
        els.venueCount.textContent = `${near.length} nearest venues shown`;

        els.toast.classList.add('hidden');
        showDetail(near[0].v, { nearMe: true, distanceKm: near[0].d });
      },
      () => {
        finishLocationRequest();
        toast('Could not get your location. Check permissions.');
      },
      { enableHighAccuracy: false, timeout: 10000 }
    );
  });

  // Keyboard: Esc closes detail
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeDetail();
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
