# Umair Taxi and Limo

Airport transfers, local taxi journeys and private Ireland tours from Youghal.

## Local development

Use Node.js 22 or 24 and npm.

```sh
npm install
npm run dev
```

Open http://localhost:3000. Re-run the build after editing generated pages.

```sh
npm run build
npm start
```

The build generates `dist/` from `site/`. The Node entry point serves the generated site and handles permanent redirects from the former HTML routes. Change business details and service copy in [site/content.mjs](site/content.mjs), page structure in [site/build.mjs](site/build.mjs), and shared sections in [site/templates.mjs](site/templates.mjs). The root `assets/logo/` and the Python scripts are historical design material. The build uses the new assets in `site/assets/`.

## Hostinger deployment

The existing Hostinger Git deployment can serve the checked-in website directly from the repository root. After editing `site/`, run `npm run publish:static` and commit the regenerated HTML, assets, sitemap and redirect rules with the source changes. This deployment mode uses the built-in static file server, and booking continues to hand off to WhatsApp.

### Node.js Web App

In hPanel, create a **Web App** and import the GitHub repository. Use a plan with Node.js Web App support.

| Setting | Value |
| --- | --- |
| Repository | `TechSoftSystemGit/umair-taxi-and-limo` |
| Branch | `main` |
| Root directory | Repository root |
| Framework preset | Other |
| Node.js | 22.x or 24.x |
| Package manager | npm |
| Build command | `npm run build` |
| Entry file | `server.mjs` |
| Start command, if requested | `npm start` |

The server reads Hostinger’s `PORT` and defaults to port 3000 locally. The app requires no credentials or other environment variables. Deploy as a Node app to serve permanent redirects. The canonical origin is currently `https://umairtaxilimo.ie`, carried over from the previous sitemap. Set the intended production origin in `site/content.mjs` before deploying to a different domain.

After deployment, verify the homepage, `/book/`, `/robots.txt`, `/sitemap.xml` and a legacy redirect such as `/services/airport-transfers.html`. See the [Hostinger Web App deployment guide](https://www.hostinger.com/support/how-to-deploy-a-nodejs-website-in-hostinger/).

## Page inventory and search mapping

Each location page targets pickup needs in its own area. Tour pages describe itinerary ideas that visitors can ask about.

| Page | Search intent |
| --- | --- |
| `/` | Airport transfer and taxi from Youghal |
| `/services/` | Taxi and transfer services |
| `/airport-transfers/` | Cork Airport transfers from Youghal, Cork, Waterford and Dungarvan |
| `/local-taxi-youghal/` | Local taxi rides in Youghal |
| `/golf-tours/` | Irish golf transfers and transport with clubs |
| `/corporate-travel/` | Business travel and event transport |
| `/hospital-runs/` | Scheduled hospital and clinic taxi journeys |
| `/aircoach-transfers/` | Taxi connections to and from Aircoach stops |
| `/tours/` | Browse private tour ideas by region |
| `/tours/ireland/` | Private tours across Ireland |
| `/tours/cork/` | Private Cork tours |
| `/tours/waterford/` | Private Waterford and Copper Coast tours |
| `/tours/youghal/` | Youghal and East Cork tours |
| `/tours/dungarvan/` | Dungarvan and Greenway area tours |
| `/tours/west-cork/` | West Cork coastal tours |
| `/tours/scenic/` | Scenic Irish drives |
| `/tours/custom/` | Custom private tours in Ireland |
| `/service-areas/` | Taxi pickup and transfer coverage |
| `/taxi-youghal/` | Youghal pickups and airport journeys |
| `/taxi-cork/` | Cork City taxi and transfers |
| `/taxi-waterford/` | Waterford taxi and airport connections |
| `/taxi-dungarvan/` | Dungarvan taxi and airport connections |
| `/taxi-county-cork/` | Rural and town pickups across County Cork |
| `/taxi-west-waterford/` | West Waterford pickups |
| `/fleet/` | Saloon taxi, people carrier and group vehicle enquiries |
| `/about/` | Youghal business information |
| `/book/` | Start or complete a booking enquiry |
| `/contact/` | Phone, WhatsApp, email and address |
| `/how-it-works/` | Journey confirmation process |
| `/rates/` | Request a journey quote |
| `/faq/` | Common taxi and tour booking questions |
| `/privacy-policy/` | Enquiry information handling |
| `/terms/` | Booking confirmation and changes |

## Redesign and handoff

- The original horizontal road wordmark has dark and light variants, a monogram and a favicon in [site/assets/logo](site/assets/logo). The live palette uses charcoal, ivory and champagne gold. The published copy follows the airport, local taxi and tour hierarchy and excludes legacy VAT, chauffeur and unconfirmed pricing or availability claims.
- The Services, Tours and Service Areas menus link to dedicated pages. Area pages link to airport and local transport, relevant tours and prefilled quote requests. Popular routes open the full booking form with route details filled in. Twenty permanent redirects preserve the former public page URLs.
- The new fleet images are illustrative WebP assets matched to saloon, MPV and minibus categories. The Irish coastline visuals are also illustrative. Replace them with approved business and destination photos when available.
- Each page has unique metadata, a canonical URL, Open Graph metadata, a single H1 and relevant schema. The build emits `/sitemap.xml` and `/robots.txt`. Breadcrumbs and JSON-LD cover the business, site, individual pages, services and visible FAQs where applicable.
- The homepage form carries route, date and time forward to the full enquiry. The full form validates details, shows the flight field for airport trips and prepares a WhatsApp message. The customer sends the message in WhatsApp and the operator confirms by reply. Phone and direct WhatsApp links provide alternate enquiry paths.
- Mobile layouts reflow the hero, navigation, forms and cards. Keyboard navigation, focus indicators, native form validation and reduced-motion styles support accessible use. Responsive WebP media, local subset fonts, reserved image dimensions, lazy below-fold images and small CSS and JavaScript bundles support fast rendering.
- Before publishing, confirm the production domain, exact fleet and capacities, published tour options, and the privacy and terms wording against the business’s actual policies. Rates and availability are handled by individual enquiry.
