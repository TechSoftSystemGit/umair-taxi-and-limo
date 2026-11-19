import os

os.makedirs("assets/logo", exist_ok=True)

# --------------------------------------------------------------------------
# DESIGN SYSTEM COLOR SPECIFICATIONS
# Primary Gold: #C5A059 (Warm Muted Champagne Gold)
# Light Gold:   #F5E2B3 (Champagne Sheen)
# Dark Gold:    #9A7835 (Deep Bronze Gold)
# Rich Black:   #0B0D12 (Obsidian Chauffeur Black)
# Crisp White:  #FFFFFF
# --------------------------------------------------------------------------

FONT_IMPORT = "@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Montserrat:wght@500;600;700&display=swap');"

# ==========================================================================
# 1. MAIN HORIZONTAL LOGO - DARK HEADER VERSION (White + Champagne Gold)
# Proportions: 380x72 => 5.28:1 (Target: 4:1 to 6:1)
# Transparent background
# ==========================================================================
svg_horizontal_dark = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 72" width="380" height="72">
  <defs>
    <linearGradient id="champagneGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE8B3"/>
      <stop offset="25%" stop-color="#E2C275"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="75%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
    <filter id="subtleGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="1" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <style>
    {FONT_IMPORT}
    .brand-title {{
      font-family: 'Cinzel', 'Trajan Pro', 'Baskerville', 'Playfair Display', 'Georgia', serif;
      font-size: 27px;
      font-weight: 700;
      letter-spacing: 0.16em;
      fill: #FFFFFF;
    }}
    .brand-subtitle {{
      font-family: 'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.38em;
      fill: url(#champagneGold);
      text-transform: uppercase;
    }}
    .divider-line {{
      stroke: url(#champagneGold);
      stroke-width: 1.25;
      stroke-linecap: round;
      opacity: 0.65;
    }}
  </style>

  <!-- Monogram Symbol -->
  <g id="brand-symbol" transform="translate(10, 10)">
    <!-- Architectural Chiseled U Monogram -->
    <path d="M 11 8 L 20 13 L 20 34.5 C 20 40.5 24 45 28.5 45 C 33 45 37 40.5 37 34.5 L 37 13 L 46 8 L 46 34.5 C 46 44.5 38 51.5 28.5 51.5 C 19 51.5 11 44.5 11 34.5 Z" 
          fill="url(#champagneGold)" filter="url(#subtleGlow)"/>

    <!-- Terminal Chauffeur Facets -->
    <path d="M 39 10 L 46 6 L 49.5 14 L 46 15.5 Z" fill="url(#champagneGold)" opacity="0.95"/>
    <path d="M 11 8 L 17.5 4.5 L 20 13 Z" fill="url(#champagneGold)" opacity="0.95"/>

    <!-- Central Chauffeur Waypoint Diamond Star -->
    <path d="M 28.5 12 C 28.5 17.5 29.8 19.5 34 19.5 C 29.8 19.5 28.5 21.5 28.5 27 C 28.5 21.5 27.2 19.5 23 19.5 C 27.2 19.5 28.5 17.5 28.5 12 Z" fill="#FFFFFF"/>

    <!-- Streamlined Aerodynamic Horizon Track -->
    <path d="M 15 55 C 23.5 57 33.5 57 42 55" stroke="url(#champagneGold)" stroke-width="1.6" stroke-linecap="round" fill="none"/>
  </g>

  <!-- Elegant Vertical Separator -->
  <line class="divider-line" x1="72" y1="18" x2="72" y2="54"/>

  <!-- Brand Typography -->
  <g id="brand-text">
    <text x="88" y="38" class="brand-title">UMAIR</text>
    <text x="89" y="55" class="brand-subtitle">TAXI &amp; LIMO</text>
  </g>
</svg>"""

# ==========================================================================
# 2. MAIN HORIZONTAL LOGO - LIGHT HEADER VERSION (Obsidian Black + Muted Gold)
# Proportions: 380x72 => 5.28:1
# Transparent background
# ==========================================================================
svg_horizontal_light = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 72" width="380" height="72">
  <defs>
    <linearGradient id="champagneGoldLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="25%" stop-color="#B88E3E"/>
      <stop offset="60%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#8F6B2A"/>
    </linearGradient>
  </defs>

  <style>
    {FONT_IMPORT}
    .brand-title-dark {{
      font-family: 'Cinzel', 'Trajan Pro', 'Baskerville', 'Playfair Display', 'Georgia', serif;
      font-size: 27px;
      font-weight: 700;
      letter-spacing: 0.16em;
      fill: #0B0D12;
    }}
    .brand-subtitle-dark {{
      font-family: 'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.38em;
      fill: url(#champagneGoldLight);
      text-transform: uppercase;
    }}
    .divider-line-dark {{
      stroke: url(#champagneGoldLight);
      stroke-width: 1.25;
      stroke-linecap: round;
      opacity: 0.75;
    }}
  </style>

  <!-- Monogram Symbol -->
  <g id="brand-symbol" transform="translate(10, 10)">
    <path d="M 11 8 L 20 13 L 20 34.5 C 20 40.5 24 45 28.5 45 C 33 45 37 40.5 37 34.5 L 37 13 L 46 8 L 46 34.5 C 46 44.5 38 51.5 28.5 51.5 C 19 51.5 11 44.5 11 34.5 Z" 
          fill="url(#champagneGoldLight)"/>
    <path d="M 39 10 L 46 6 L 49.5 14 L 46 15.5 Z" fill="url(#champagneGoldLight)" opacity="0.95"/>
    <path d="M 11 8 L 17.5 4.5 L 20 13 Z" fill="url(#champagneGoldLight)" opacity="0.95"/>
    <path d="M 28.5 12 C 28.5 17.5 29.8 19.5 34 19.5 C 29.8 19.5 28.5 21.5 28.5 27 C 28.5 21.5 27.2 19.5 23 19.5 C 27.2 19.5 28.5 17.5 28.5 12 Z" fill="#0B0D12"/>
    <path d="M 15 55 C 23.5 57 33.5 57 42 55" stroke="url(#champagneGoldLight)" stroke-width="1.6" stroke-linecap="round" fill="none"/>
  </g>

  <!-- Divider -->
  <line class="divider-line-dark" x1="72" y1="18" x2="72" y2="54"/>

  <!-- Brand Typography -->
  <g id="brand-text">
    <text x="88" y="38" class="brand-title-dark">UMAIR</text>
    <text x="89" y="55" class="brand-subtitle-dark">TAXI &amp; LIMO</text>
  </g>
</svg>"""

# ==========================================================================
# 3. SINGLE-LINE HORIZONTAL LOGO: [U] UMAIR | TAXI & LIMO
# Proportions: 420x70 => 6.0:1 (Exact 6:1 Landscape)
# ==========================================================================
svg_horizontal_single_line = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 70" width="420" height="70">
  <defs>
    <linearGradient id="champagneGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE8B3"/>
      <stop offset="25%" stop-color="#E2C275"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="75%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
  </defs>

  <style>
    {FONT_IMPORT}
    .brand-title-inline {{
      font-family: 'Cinzel', 'Trajan Pro', 'Baskerville', 'Playfair Display', 'Georgia', serif;
      font-size: 24px;
      font-weight: 700;
      letter-spacing: 0.18em;
      fill: #FFFFFF;
    }}
    .brand-subtitle-inline {{
      font-family: 'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.32em;
      fill: url(#champagneGold);
      text-transform: uppercase;
    }}
    .divider-inline {{
      stroke: url(#champagneGold);
      stroke-width: 1.25;
      stroke-linecap: round;
      opacity: 0.65;
    }}
  </style>

  <!-- Monogram -->
  <g id="brand-symbol" transform="translate(10, 11)">
    <path d="M 10 7 L 18 11.5 L 18 30 C 18 35.5 21.5 39 25.5 39 C 29.5 39 33 35.5 33 30 L 33 11.5 L 41 7 L 41 30 C 41 39 34 45 25.5 45 C 17 45 10 39 10 30 Z" 
          fill="url(#champagneGold)"/>
    <path d="M 35 9 L 41 5.5 L 44 12 L 41 13.5 Z" fill="url(#champagneGold)" opacity="0.95"/>
    <path d="M 10 7 L 16 4 L 18 11.5 Z" fill="url(#champagneGold)" opacity="0.95"/>
    <path d="M 25.5 10 C 25.5 15 26.5 16.5 30 16.5 C 26.5 16.5 25.5 18 25.5 23 C 25.5 18 24.5 16.5 21 16.5 C 24.5 16.5 25.5 15 25.5 10 Z" fill="#FFFFFF"/>
    <path d="M 13 48 C 21 50 30 50 38 48" stroke="url(#champagneGold)" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  </g>

  <!-- Single-Line Lockup -->
  <text x="68" y="43" class="brand-title-inline">UMAIR</text>
  <line class="divider-inline" x1="194" y1="22" x2="194" y2="48"/>
  <text x="210" y="42" class="brand-subtitle-inline">TAXI &amp; LIMO</text>
</svg>"""

# ==========================================================================
# 4. LUXURY ALL-GOLD MONOCHROME HORIZONTAL LOGO
# Proportions: 380x72 => 5.28:1
# ==========================================================================
svg_horizontal_gold = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 72" width="380" height="72">
  <defs>
    <linearGradient id="pureGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE8B3"/>
      <stop offset="25%" stop-color="#E2C275"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="75%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
  </defs>

  <style>
    {FONT_IMPORT}
    .brand-title-gold {{
      font-family: 'Cinzel', 'Trajan Pro', 'Baskerville', 'Playfair Display', 'Georgia', serif;
      font-size: 27px;
      font-weight: 700;
      letter-spacing: 0.16em;
      fill: url(#pureGold);
    }}
    .brand-subtitle-gold {{
      font-family: 'Montserrat', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 0.38em;
      fill: url(#pureGold);
      text-transform: uppercase;
      opacity: 0.92;
    }}
    .divider-gold {{
      stroke: url(#pureGold);
      stroke-width: 1.25;
      stroke-linecap: round;
      opacity: 0.65;
    }}
  </style>

  <!-- Monogram Symbol -->
  <g id="brand-symbol" transform="translate(10, 10)">
    <path d="M 11 8 L 20 13 L 20 34.5 C 20 40.5 24 45 28.5 45 C 33 45 37 40.5 37 34.5 L 37 13 L 46 8 L 46 34.5 C 46 44.5 38 51.5 28.5 51.5 C 19 51.5 11 44.5 11 34.5 Z" 
          fill="url(#pureGold)"/>
    <path d="M 39 10 L 46 6 L 49.5 14 L 46 15.5 Z" fill="url(#pureGold)" opacity="0.95"/>
    <path d="M 11 8 L 17.5 4.5 L 20 13 Z" fill="url(#pureGold)" opacity="0.95"/>
    <path d="M 28.5 12 C 28.5 17.5 29.8 19.5 34 19.5 C 29.8 19.5 28.5 21.5 28.5 27 C 28.5 21.5 27.2 19.5 23 19.5 C 27.2 19.5 28.5 17.5 28.5 12 Z" fill="#FFFFFF"/>
    <path d="M 15 55 C 23.5 57 33.5 57 42 55" stroke="url(#pureGold)" stroke-width="1.6" stroke-linecap="round" fill="none"/>
  </g>

  <!-- Divider -->
  <line class="divider-gold" x1="72" y1="18" x2="72" y2="54"/>

  <!-- Typography -->
  <g id="brand-text">
    <text x="88" y="38" class="brand-title-gold">UMAIR</text>
    <text x="89" y="55" class="brand-subtitle-gold">TAXI &amp; LIMO</text>
  </g>
</svg>"""

# ==========================================================================
# 5. MONOGRAM / ICON - TRANSPARENT (1:1, 64x64)
# Suitable for embedding directly anywhere without background card
# ==========================================================================
svg_monogram_transparent = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="transpGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE8B3"/>
      <stop offset="25%" stop-color="#E2C275"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="75%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
  </defs>

  <g transform="translate(3.5, 2)">
    <!-- Architectural Chiseled U -->
    <path d="M 11 8 L 20 13 L 20 34.5 C 20 40.5 24 45 28.5 45 C 33 45 37 40.5 37 34.5 L 37 13 L 46 8 L 46 34.5 C 46 44.5 38 51.5 28.5 51.5 C 19 51.5 11 44.5 11 34.5 Z" 
          fill="url(#transpGold)"/>
    <path d="M 39 10 L 46 6 L 49.5 14 L 46 15.5 Z" fill="url(#transpGold)" opacity="0.95"/>
    <path d="M 11 8 L 17.5 4.5 L 20 13 Z" fill="url(#transpGold)" opacity="0.95"/>
    <path d="M 28.5 12 C 28.5 17.5 29.8 19.5 34 19.5 C 29.8 19.5 28.5 21.5 28.5 27 C 28.5 21.5 27.2 19.5 23 19.5 C 27.2 19.5 28.5 17.5 28.5 12 Z" fill="#FFFFFF"/>
    <path d="M 15 55 C 23.5 57 33.5 57 42 55" stroke="url(#transpGold)" stroke-width="1.8" stroke-linecap="round" fill="none"/>
  </g>
</svg>"""

# ==========================================================================
# 6. MONOGRAM BADGE - DARK (1:1, 120x120)
# ==========================================================================
svg_monogram_dark = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="badgeGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FCE8B3"/>
      <stop offset="25%" stop-color="#E2C275"/>
      <stop offset="50%" stop-color="#C5A059"/>
      <stop offset="75%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#C5A059"/>
    </linearGradient>
    <filter id="badgeShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <rect width="120" height="120" rx="24" fill="#0B0D12"/>
  <rect width="118" height="118" x="1" y="1" rx="23" fill="none" stroke="url(#badgeGold)" stroke-width="1" opacity="0.35"/>

  <g transform="translate(18, 16)" filter="url(#badgeShadow)">
    <path d="M 18 14 L 32 21 L 32 54 C 32 64 38 71 45 71 C 52 71 58 64 58 54 L 58 21 L 72 14 L 72 54 C 72 70 60 81 45 81 C 30 81 18 70 18 54 Z" 
          fill="url(#badgeGold)"/>
    <path d="M 61 17 L 72 11 L 78 23 L 72 25 Z" fill="url(#badgeGold)" opacity="0.95"/>
    <path d="M 18 14 L 28 8.5 L 32 21 Z" fill="url(#badgeGold)" opacity="0.95"/>
    <path d="M 45 19 C 45 27.5 47 30.5 53.5 30.5 C 47 30.5 45 33.5 45 42 C 45 33.5 43 30.5 36.5 30.5 C 43 30.5 45 27.5 45 19 Z" fill="#FFFFFF"/>
    <path d="M 24 87 C 37 90.5 53 90.5 66 87" stroke="url(#badgeGold)" stroke-width="2.6" stroke-linecap="round" fill="none"/>
  </g>
</svg>"""

# ==========================================================================
# 7. MONOGRAM BADGE - LIGHT (1:1, 120x120)
# ==========================================================================
svg_monogram_light = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="badgeGoldDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D4AF37"/>
      <stop offset="25%" stop-color="#B88E3E"/>
      <stop offset="60%" stop-color="#A57F35"/>
      <stop offset="100%" stop-color="#8F6B2A"/>
    </linearGradient>
  </defs>

  <rect width="120" height="120" rx="24" fill="#FFFFFF"/>
  <rect width="118" height="118" x="1" y="1" rx="23" fill="none" stroke="url(#badgeGoldDark)" stroke-width="1" opacity="0.25"/>

  <g transform="translate(18, 16)">
    <path d="M 18 14 L 32 21 L 32 54 C 32 64 38 71 45 71 C 52 71 58 64 58 54 L 58 21 L 72 14 L 72 54 C 72 70 60 81 45 81 C 30 81 18 70 18 54 Z" 
          fill="url(#badgeGoldDark)"/>
    <path d="M 61 17 L 72 11 L 78 23 L 72 25 Z" fill="url(#badgeGoldDark)" opacity="0.95"/>
    <path d="M 18 14 L 28 8.5 L 32 21 Z" fill="url(#badgeGoldDark)" opacity="0.95"/>
    <path d="M 45 19 C 45 27.5 47 30.5 53.5 30.5 C 47 30.5 45 33.5 45 42 C 45 33.5 43 30.5 36.5 30.5 C 43 30.5 45 27.5 45 19 Z" fill="#0B0D12"/>
    <path d="M 24 87 C 37 90.5 53 90.5 66 87" stroke="url(#badgeGoldDark)" stroke-width="2.6" stroke-linecap="round" fill="none"/>
  </g>
</svg>"""

# ==========================================================================
# 8. FAVICON (Ultra-Crisp 32x32 / High Contrast)
# ==========================================================================
svg_favicon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <defs>
    <linearGradient id="favGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE094"/>
      <stop offset="50%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#A8833C"/>
    </linearGradient>
  </defs>

  <rect width="32" height="32" rx="7" fill="#0A0B0E"/>

  <g transform="translate(1, 1)">
    <path d="M 6 5 L 10.5 7.5 L 10.5 17 C 10.5 20.2 12.5 22.5 15 22.5 C 17.5 22.5 19.5 20.2 19.5 17 L 19.5 7.5 L 24 5 L 24 17 C 24 23 19.8 26.5 15 26.5 C 10.2 26.5 6 23 6 17 Z" 
          fill="url(#favGold)"/>
    <polygon points="15,6.5 16.5,10.5 20.5,12 16.5,13.5 15,17.5 13.5,13.5 9.5,12 13.5,10.5" fill="#FFFFFF"/>
  </g>
</svg>"""

# Write all SVGs
assets = {
    "assets/logo/logo-horizontal-dark.svg": svg_horizontal_dark,
    "assets/logo/logo-horizontal-light.svg": svg_horizontal_light,
    "assets/logo/logo-horizontal-single-line.svg": svg_horizontal_single_line,
    "assets/logo/logo-horizontal-gold.svg": svg_horizontal_gold,
    "assets/logo/logo-monogram-transparent.svg": svg_monogram_transparent,
    "assets/logo/logo-monogram-dark.svg": svg_monogram_dark,
    "assets/logo/logo-monogram-light.svg": svg_monogram_light,
    "assets/logo/favicon.svg": svg_favicon,
}

for path, content in assets.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Asset created: {path}")

