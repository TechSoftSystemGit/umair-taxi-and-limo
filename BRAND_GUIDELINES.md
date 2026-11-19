# UMAIR TAXI & LIMO — BRAND IDENTITY & LOGO GUIDELINES

## 1. Executive Summary

This document defines the official visual identity, logo assets, color standards, typography, and website header implementation rules for **Umair Taxi and Limo** (Executive Chauffeur & Private Hire Transport, Ireland).

The identity is built around a bespoke **Horizontal Landscape Mark** (5.28:1 to 6.0:1 ratio) engineered specifically for compact, modern website headers, preventing vertical bloat while maintaining an unmistakable air of exclusivity, discreet luxury, and Irish hospitality.

---

## 2. Core Brand Mark Anatomy

The logo comprises three harmonious elements:

1. **The Chauffeur U Monogram**:
   - **Architectural Stems**: Chiseled 45° beveled summit reflecting structural integrity, reliability, and precision.
   - **Aerodynamic Winglets & Horizon Track**: Subtle hydrodynamic lines evoking highway cruising, smooth transit, and vehicle motion without relying on generic car silhouettes.
   - **Central Chauffeur Waypoint Star**: A discreet 4-point diamond star symbolizing precision navigation, 24/7 airport meet-and-greet, and VIP destination service.
2. **Primary Wordmark**:
   - **`UMAIR`**: High-contrast, tracked classical Roman serif letterforms with refined serifs.
3. **Secondary Wordmark**:
   - **`TAXI & LIMO`**: Modern, geometric sans-serif small-caps with wide letter-spacing (`0.38em`) in muted champagne gold.

---

## 3. Asset Registry

All vector assets are located in [`assets/logo/`](file:///c:/Users/l3691/Desktop/Umairtaxi%20and%20Limo/assets/logo):

| Asset Filename | ViewBox / Ratio | Colors | Intended Usage |
| :--- | :--- | :--- | :--- |
| `logo-horizontal-dark.svg` | `380x72` (5.28:1) | White + Champagne Gold | **Primary Web Header** (Dark/Obsidian backgrounds), Footers |
| `logo-horizontal-light.svg` | `380x72` (5.28:1) | Obsidian Black + Muted Gold | **Light Backgrounds**, Print Invoices, Booking Confirmations |
| `logo-horizontal-single-line.svg` | `420x70` (6.0:1) | White + Gold | Single-line horizontal format for ultra-compact headers |
| `logo-horizontal-gold.svg` | `380x72` (5.28:1) | Pure Champagne Gold | Luxury foil stamping, vehicle decals, VIP credentials |
| `logo-monogram-transparent.svg` | `64x64` (1:1) | Champagne Gold | In-app icons, watermarks, UI badges |
| `logo-monogram-dark.svg` | `120x120` (1:1) | Gold on Obsidian Badge | Social avatars (Instagram, LinkedIn, WhatsApp Business) |
| `logo-monogram-light.svg` | `120x120` (1:1) | Gold on White Badge | Light app launchers, paper tags, vehicle key fobs |
| `favicon.svg` | `32x32` (1:1) | Gold + White on Black | Browser tab favicon, PWA icon, mobile bookmark |

---

## 4. Color Palette Specifications

To guarantee brand consistency across all website components (hero, cards, buttons, forms, footers), use the following standardized color tokens:

### Primary Brand Gold
- **Champagne Gold (Base)**: `#C5A059`
  - `rgb(197, 160, 89)` | `hsl(40, 48%, 56%)`
- **Champagne Sheen (Light / Highlight)**: `#FCE8B3`
  - `rgb(252, 232, 179)` | `hsl(44, 91%, 85%)`
- **Bronze Gold (Deep / Shadow)**: `#9E782E`
  - `rgb(158, 120, 46)` | `hsl(40, 55%, 40%)`

### Neutral Obsidian & Black
- **Obsidian Black (Dark Mode Base)**: `#0B0D12`
  - `rgb(11, 13, 18)` | `hsl(223, 24%, 6%)`
- **Chauffeur Charcoal (Card Surfaces)**: `#141720`
  - `rgb(20, 23, 32)` | `hsl(225, 23%, 10%)`
- **Subtle Surface Border**: `#1E2330`
  - `rgb(30, 35, 48)` | `hsl(223, 23%, 15%)`

### High-Contrast Text
- **Crisp Platinum White**: `#FFFFFF`
- **Muted Silver Text**: `#8E94A5`

### CSS Custom Properties
```css
:root {
  --color-gold-primary: #C5A059;
  --color-gold-light: #FCE8B3;
  --color-gold-deep: #9E782E;
  --color-gold-gradient: linear-gradient(135deg, #FCE8B3 0%, #C5A059 50%, #9E782E 100%);
  
  --color-black-obsidian: #0B0D12;
  --color-black-surface: #141720;
  --color-black-border: #1E2330;
  
  --color-text-primary: #FFFFFF;
  --color-text-muted: #8E94A5;
}
```

---

## 5. Typography Standards

- **Primary Display / Wordmark Font**:
  - `Cinzel`, `'Trajan Pro'`, `'Baskerville'`, `'Georgia'`, `serif`
  - Weight: 700 (Bold)
  - Tracking: `0.16em` to `0.20em`
- **Secondary / Body & UI Font**:
  - `'Montserrat'`, `'Inter'`, `-apple-system`, `sans-serif`
  - Tracking: `0.35em` for uppercase subtitles, `0.02em` for body prose

---

## 6. Website Header Implementation Rules

The horizontal logo was specifically calibrated for compact website headers:

1. **Header Height Boundaries**:
   - **Desktop**: 72px – 84px (Recommended: `78px`)
   - **Mobile**: 60px – 72px (Recommended: `64px`)
2. **Logo Dimensions Inside Header**:
   - Desktop: `height: 40px; width: auto;` (Renders at ~211px wide, falling perfectly inside the 180–240px desktop specification).
   - Mobile: `height: 30px; width: auto;` (Renders at ~158px wide, falling perfectly inside the 130–170px mobile specification).
3. **Mandatory CSS Rule**:
   - **Always set `height` and leave `width: auto;`** with `object-fit: contain;`.
   - **Never stretch, skew, or distort the aspect ratio.**

### Copy-Paste Header Snippet:
```html
<header class="site-header">
  <a href="/" class="brand-link" aria-label="Umair Taxi and Limo Home">
    <img 
      src="assets/logo/logo-horizontal-dark.svg" 
      alt="Umair Taxi and Limo" 
      class="brand-logo"
      width="380" 
      height="72"
    >
  </a>
  
  <nav class="site-nav">
    <!-- Links -->
  </nav>
</header>
```

```css
.site-header {
  height: 78px;
  background-color: var(--color-black-obsidian);
  border-bottom: 1px solid rgba(197, 160, 89, 0.2);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 clamp(16px, 4vw, 36px);
}

.site-header .brand-logo {
  height: 40px;
  width: auto;
  display: block;
}

@media (max-width: 768px) {
  .site-header {
    height: 64px;
  }
  .site-header .brand-logo {
    height: 30px;
  }
}
```

---

## 7. Prohibited Uses (Anti-Patterns)

- ❌ DO NOT use yellow taxi roof boxes, checkers, cartoon vehicle outlines, or fake Mercedes/BMW stars.
- ❌ DO NOT enclose the logo in a heavy circular stamp or towering medieval shield for the header mark.
- ❌ DO NOT substitute the champagne gold `#C5A059` with saturated school-bus yellow (`#FFCC00`) or fluorescent yellow.
- ❌ DO NOT vertically stretch the logo.
- ❌ DO NOT allow the header height to exceed 84px on desktop.

---

## 8. Interactive Verification Harness

To view and interact with all logo variations, responsive desktop and mobile headers, favicon matrices, and color tokens, open [`index.html`](file:///c:/Users/l3691/Desktop/Umairtaxi%20and%20Limo/index.html) in your browser.

