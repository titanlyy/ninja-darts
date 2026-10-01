# Ninja Darts – Application Requirements Document (ARD)

Version: 0.1 (Draft) | Status: Proposed | Owner: @titanlyy
Tagline: Made by dart lovers, for dart lovers.

Conventions: distances in km/m, currency in SGD (S$) as base with multi-currency display, dates DD/MM/YYYY, time 24-hour, default timezone Asia/Singapore with per-venue local timezone.

---

## 1. Vision and Goals

Ninja Darts is a global directory of places to play darts (bars, clubs, arcades, leagues, dedicated darts venues). Venue owners claim and manage their own listings. Revenue comes from venue subscriptions, promoted events and ads.

Goals:
1. Be the most complete and trusted darts venue directory worldwide.
2. Let owners self-serve updates (hours, boards, prices, events).
3. Generate recurring revenue via subscriptions and promotion.
4. Foster a community of players (reviews, check-ins, event calendar).

Non-goals (v1): online score keeping, live streaming, betting/gambling features.

## 2. Users and Roles

| Role | Description | Key permissions |
|---|---|---|
| Visitor | Unauthenticated | Search, view venues, view events |
| Player | Registered user | Save favourites, review, suggest venues, RSVP to events, report errors |
| Venue Owner | Verified claimant of a venue | Edit own venue, post events, manage subscription, view analytics |
| Venue Staff | Invited by owner | Edit venue and events (no billing) |
| Moderator | Community/volunteer | Approve submissions, handle reports, resolve claim disputes |
| Admin | Platform team | Full access, pricing, refunds, user management, audit logs |

## 3. Scope and Phasing

- **Phase 0 (current):** GitHub repo, open data (JSON/CSV) seed list, contribution guide.
- **Phase 1 (MVP):** Public directory website, search/map, venue pages, accounts, claim and edit venue, moderation.
- **Phase 2 (Monetisation):** Subscription tiers, Stripe billing, verified badge, analytics.
- **Phase 3 (Events):** Event posting, city/country calendar, paid promotion, RSVP.
- **Phase 4 (Growth):** Mobile apps/PWA, leagues, ticketing, affiliate, sponsorships, API.

## 4. Functional Requirements

### 4.1 Venue Directory and Search (Phase 1)
- FR-1: Browse by country > city > venue with SEO-friendly URLs (e.g. /sg/singapore/venue-name).
- FR-2: Full-text search by name, city, postal code; autocomplete.
- FR-3: Filters: board type (steel-tip, soft-tip/electronic), number of boards, league nights, food/drinks, price per game or hour, opening now, accessibility, family-friendly, free to play, reservations.
- FR-4: Map view with clustering; "near me" search with radius in km (default 5 km, options 1/2/5/10/25/50 km).
- FR-5: Sorting: distance, rating, recently updated, name.
- FR-6: Venue detail page: name, description, address, geo coordinates, photos, opening hours (incl. holidays), contact (phone, email, website, socials), boards (type, count, brand), pricing, amenities, upcoming events, reviews, last-verified date.
- FR-7: Badges: Claimed, Verified (Pro), Community-submitted, Recently Updated.
- FR-8: Multilingual UI (English first; Mandarin, Malay, Tamil, German, Dutch, Spanish later). i18n-ready from day one.

### 4.2 Accounts and Authentication
- FR-9: Sign up/login via email + password, Google, Apple; email verification; password reset.
- FR-10: Optional MFA for owners.
- FR-11: Role-based access control (see Section 2).
- FR-12: PDPA/GDPR compliant consent, data export and deletion.

### 4.3 Venue Claiming and Management (Phase 1)
- FR-13: Owner clicks "Claim this venue" and verifies ownership by one of: business email on venue domain, phone call/SMS code to listed number, postcard code, or document upload (ACRA/business registration, utility bill).
- FR-14: Moderator review queue for claims with approve/reject/request-info; dispute handling for multiple claimants.
- FR-15: Owner dashboard to edit all venue fields, upload photos (max 10 MB each, JPG/PNG/WebP, auto-resized), set hours, special closures, and pricing.
- FR-16: Staff invitations with limited permissions.
- FR-17: Edit history/audit log with ability to revert; changes by free-tier owners may go through light moderation.
- FR-18: Owners can add a new venue (goes to moderation) or manage multiple venues/chain under one organisation account.
- FR-19: Player-submitted "Suggest a venue" and "Report incorrect info" flows.
- FR-20: Duplicate detection (name + geo proximity within 50 m).

### 4.4 Reviews and Community
- FR-21: 1-5 star ratings plus text, photos; one review per user per venue; owner can reply publicly.
- FR-22: Report/flag review; moderation tooling; profanity filter.
- FR-23: Favourites lists, check-ins (optional), "I played here" badge.

### 4.5 Events and Calendar (Phase 3)
- FR-24: Owners create events: title, type (tournament, league night, social, beginners night, charity, pro exhibition), format (e.g. 501, cricket, doubles), start/end, recurrence, entry fee, prize pool, capacity, registration link, poster image, description.
- FR-25: Public calendar by city and country: month/week/list views, filters by event type, format, price, date range; add-to-calendar (ICS/Google).
- FR-26: iCal feed per city, per venue; embeddable widget for venue's own website.
- FR-27: RSVP/registration (free in v1; paid ticketing in Phase 4); waitlist; email reminders.
- FR-28: Notifications: new events in followed cities/venues (email, push).
- FR-29: Event moderation and spam controls.
- FR-30: Local timezone handling per venue.

### 4.6 Monetisation (Phase 2 and 3)
- FR-31: Subscription plans managed via Stripe (or equivalent supporting SGD, cards, PayNow/GrabPay where available), monthly/annual billing, 14-day free trial, proration, upgrade/downgrade, cancellation, invoices, GST handling (9% for Singapore at time of writing; make configurable) and tax per region.
- FR-32: Feature gating by plan (see 6.1).
- FR-33: Promotion purchase flow for events and venues (see 6.2), with scheduling, budget, and performance reporting.
- FR-34: Failed payment retries (dunning), grace period (7 days), auto-downgrade to Free.
- FR-35: Admin tools: coupons, refunds, manual plan overrides, revenue dashboard.
- FR-36: Clear "Sponsored" / "Promoted" labelling on all paid placements.

### 4.7 Analytics (Phase 2)
- FR-37: Owner dashboard: page views, search impressions, clicks to call/website/directions, event views and RSVPs, review trends, by date range.
- FR-38: Admin analytics: venues by country, claim rate, MRR, churn, conversion.

### 4.8 Admin and Moderation
- FR-39: Admin console for users, venues, claims, reports, events, promotions, billing.
- FR-40: Bulk import/export (CSV/JSON); sync with the GitHub open dataset.
- FR-41: Audit logs; abuse detection.

### 4.9 Public API (Phase 4)
- FR-42: Read-only REST/GraphQL API with API keys and rate limits; paid tiers for commercial use (darts brands, apps).

## 5. Data Model (Core Entities)

- **User**: id, name, email, role, locale, created_at, consent flags.
- **Organisation**: id, name, billing details, owner_user_id.
- **Venue**: id, org_id, slug, name, description, address lines, city, region, country_code, postal_code, lat, lng, phone, email, website, social links, status (draft/pending/published/closed), claim_status, verified_at, last_updated_at, source (owner/community/import).
- **VenueHours**: venue_id, weekday, open, close, exceptions (date ranges, holidays).
- **Board**: venue_id, type (steel/soft), brand, count, notes.
- **Pricing**: venue_id, type (per game/hour/free/minimum spend), amount, currency.
- **Amenity**: tag list (food, bar, parking, wheelchair access, air-con, etc.).
- **Photo**: venue_id, url, uploaded_by, status.
- **Review**: id, venue_id, user_id, rating, body, status, owner_reply.
- **Event**: id, venue_id, title, type, format, start_at, end_at, timezone, recurrence_rule, fee_amount, currency, prize_info, capacity, registration_url, status, promoted flag.
- **Registration**: event_id, user_id, status.
- **Subscription**: org_id, plan, status, period start/end, stripe ids.
- **Promotion**: target (event/venue), placement, start/end, budget, impressions, clicks, payment ref.
- **Claim**: venue_id, user_id, method, evidence, status, reviewer.
- **Report**, **AuditLog**, **Favourite**.

## 6. Revenue Model

### 6.1 Venue Subscription Tiers (proposed, S$ pricing to be validated)

| Feature | Free | Pro (~S$19/mo) | Premium (~S$49/mo) |
|---|---|---|---|
| Claim and edit basic details | Yes | Yes | Yes |
| Photos | 3 | 15 | Unlimited |
| Verified badge | No | Yes | Yes |
| Post events | 1 active | 10 active | Unlimited |
| Event calendar priority | No | Standard | Boosted |
| Analytics | Basic views | Full | Full + exports |
| Reply to reviews | Yes | Yes | Yes |
| Remove competitor suggestions on page | No | No | Yes |
| Booking/enquiry button | No | Yes | Yes |
| Multi-venue management | No | Up to 3 | Unlimited |
| Embeddable calendar widget | No | Yes | Yes |
| Monthly promoted credits | 0 | 0 | Included |

Annual plans discounted around 15-20%.

### 6.2 Additional Revenue Streams

1. **Promoted events:** pay per week to feature a tournament on city/country calendar top, homepage, and email newsletter (flat fee or cost-per-day, e.g. S$15-S$100 by market size).
2. **Featured venue placement:** highlighted in search results and map pins for a city (clearly labelled sponsored).
3. **Tournament ticketing/registration fees:** 3-5% platform fee plus payment processing on paid event entries.
4. **Table/board booking commission or booking tool fee:** flat monthly add-on or per-booking fee.
5. **Newsletter and city guide sponsorship:** darts brands (Target, Winmau, Harrows, Unicorn, Red Dragon), barware and beverage sponsors.
6. **Affiliate marketing:** darts, flights, boards and accessories on venue and blog pages.
7. **Merchandise:** Ninja Darts branded shirts, flights, and shafts via print-on-demand.
8. **League management SaaS:** fixtures, standings and player stats for pub leagues (paid per league per season).
9. **Data/API licensing:** commercial access for apps, brands, and tourism boards.
10. **Verified Venue Audit/Mystery Player programme:** paid "Ninja Approved" certification for venue quality.
11. **Player premium (Ninja+):** ad-free, advanced alerts, travel itineraries ("darts pub crawl" planner), exclusive deals.
12. **Deals and vouchers:** venues sell game packages or happy-hour vouchers; platform takes a percentage.
13. **Job/Classifieds board:** board sales, venue-for-sale, referee and caller listings.
14. **Display ads:** only on free player-facing pages, strictly limited; never on owner dashboards.

## 7. Non-Functional Requirements

- **Performance:** page load LCP under 2.5 s on 4G; search response under 500 ms p95.
- **SEO:** server-side rendering, structured data (schema.org LocalBusiness, Event), sitemaps by city/country.
- **Availability:** 99.9% target; daily backups, point-in-time recovery.
- **Scalability:** support 100,000 venues and 1,000,000 monthly users initially.
- **Security:** OWASP Top 10, TLS everywhere, hashed passwords (Argon2/bcrypt), rate limiting, CSRF/XSS protection, image scanning, secrets management.
- **Privacy/compliance:** PDPA (Singapore), GDPR, cookie consent, PCI via Stripe (no card data stored).
- **Accessibility:** WCAG 2.2 AA.
- **Responsive and mobile-first;** PWA support.
- **Observability:** logging, error tracking, uptime monitoring, audit trail.
- **Localisation:** currencies, units (km default, miles optional), date and time formats.

## 8. Suggested Tech Stack (Open to Change)

- Frontend: Next.js (React, TypeScript), Tailwind CSS.
- Backend: Next.js API routes or NestJS; PostgreSQL with PostGIS for geo queries.
- Search: PostgreSQL full text initially; Meilisearch/Typesense/Algolia later.
- Auth: Auth.js or Clerk/Supabase Auth.
- Storage/CDN: S3-compatible storage + Cloudflare.
- Maps: Mapbox or Google Maps (Places for address autocomplete).
- Payments: Stripe Billing (+ Stripe Connect for ticketing).
- Email/Push: Resend/SendGrid; Web Push.
- Hosting: Vercel/Fly.io/AWS (Singapore region for APAC latency).
- CI/CD: GitHub Actions; environments for dev, staging, prod.

## 9. Key User Flows

1. **Player finds a venue:** search city > filter > view venue > get directions / call.
2. **Owner onboarding:** sign up > search venue > claim > verify > edit details > publish > upgrade to Pro.
3. **Event promotion:** owner creates event > selects "Promote" > chooses placement and dates > pays > event appears boosted > views report.
4. **Calendar discovery:** player picks city > calendar view > filters tournaments this weekend > RSVP > gets reminder.

## 10. Content and Data Seeding

- Seed from the open GitHub dataset (venues/ folder) and public sources (with licence compliance).
- Community contributions via pull requests and in-app suggestions.
- Outreach campaign to venue owners with pre-created "Claim your venue" emails.
- Data freshness: flag listings not verified in 12 months; periodic owner re-confirmation prompts.

## 11. Success Metrics (KPIs)

- Venues listed; percentage claimed; percentage verified.
- Monthly active users; search-to-click conversion.
- Free-to-paid conversion (target 5-8% of claimed venues); monthly recurring revenue; churn under 5% monthly.
- Events posted per month; RSVPs per event; promotion revenue.
- Data accuracy rate (reports per 1,000 views).

## 12. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Fake claims/fraud | Multi-step verification, moderator review |
| Cold-start (empty directory) | Seed data, open-source contributions, city-by-city launch (start Singapore) |
| Low owner adoption | Generous free tier, outreach, clear ROI analytics |
| Spam events/reviews | Rate limits, moderation, reputation system |
| Legal (data licensing, alcohol promotion rules) | Age-gating where required, review local advertising rules |
| Payment/tax complexity | Use Stripe Tax, start with SGD and limited regions |

## 13. Open Questions

1. Launch city/country focus (Singapore first?).
2. Final pricing and currency strategy per region.
3. Self-hosted vs managed auth/search.
4. Will paid events be processed by the platform (Stripe Connect) or linked externally?
5. Moderation staffing: volunteers vs paid.
6. Brand/legal entity and terms of service, privacy policy.

## 14. Milestones (Indicative)

| Milestone | Target |
|---|---|
| Requirements sign-off | Week 2 |
| Design (wireframes, UI kit) | Weeks 3-5 |
| MVP build (directory, search, claim/edit) | Weeks 6-16 |
| Private beta in Singapore | Week 18 |
| Subscriptions and analytics | Weeks 19-26 |
| Events calendar and promotions | Weeks 27-36 |
| Public multi-country launch | Week 38+ |
