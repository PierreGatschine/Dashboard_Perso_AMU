# svgs.py

FACILIT_AMU = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect width="64" height="64" fill="#ccc"/>
  <text x="32" y="40" font-size="20" text-anchor="middle" fill="#000">AMU</text>
</svg>
"""

ENT = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect width="64" height="64" fill="#ccc"/>
  <text x="32" y="40" font-size="20" text-anchor="middle" fill="#000">🔧</text>
</svg>
"""

SESAME = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <circle cx="32" cy="32" r="32" fill="#cc000c"/>
  <text x="32" y="40" font-size="20" text-anchor="middle" fill="#000">AMU</text>
</svg>
"""

GRAFANA = "https://raw.githubusercontent.com/grafana/grafana/main/public/img/grafana_icon.svg"

GESTION = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none">
  <path d="M19.14 12.936c.036-.304.06-.612.06-.936 0-.324-.024-.632-.07-.936l2.03-1.578a.478.478 0 0 0 .114-.62l-1.92-3.32a.48.48 0 0 0-.58-.22l-2.39.96a7.93 7.93 0 0 0-1.62-.936l-.36-2.54A.488.488 0 0 0 13.96 2h-3.92a.488.488 0 0 0-.486.42l-.36 2.54a7.93 7.93 0 0 0-1.62.936l-2.39-.96a.48.48 0 0 0-.58.22l-1.92 3.32c-.156.27-.078.61.114.62l2.03 1.578c-.046.304-.07.612-.07.936 0 .324.024.632.07.936l-2.03 1.578a.478.478 0 0 0-.114.62l1.92 3.32c.144.252.456.34.73.22l2.39-.96c.504.384 1.05.696 1.62.936l.36 2.54c.048.276.276.48.486.48h3.92c.21 0 .438-.204.486-.48l.36-2.54c.57-.24 1.116-.552 1.62-.936l2.39.96c.274.12.586.032.73-.22l1.92-3.32a.478.478 0 0 0-.114-.62l-2.03-1.578ZM12 15.6A3.6 3.6 0 1 1 12 8.4a3.6 3.6 0 0 1 0 7.2Z" fill="currentColor"/>
</svg>
"""

DASHBOARD = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
  <rect x="3" y="3" width="7" height="7"/>
  <rect x="14" y="3" width="7" height="7"/>
  <rect x="3" y="14" width="7" height="7"/>
  <rect x="14" y="14" width="7" height="7"/>
</svg>
"""

ENVELOPE = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Corps de l'enveloppe avec coins arrondis -->
  <rect x="2" y="5" width="20" height="14" rx="2" ry="2"/>
  <!-- Flap de l'enveloppe, décalé pour éviter de chevaucher le bord supérieur -->
  <polyline points="3,6 12,13 21,6"/>
</svg>

"""

GRAPH = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="currentColor" stroke="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Axe horizontal -->
  <line x1="3" y1="21" x2="21" y2="21"></line>
  <!-- Axe vertical -->
  <line x1="3" y1="21" x2="3" y2="3"></line>
  <!-- Barres du graphique -->
  <rect x="5" y="14" width="3" height="7"></rect>
  <rect x="10" y="10" width="3" height="11"></rect>
  <rect x="15" y="6" width="3" height="15"></rect>
</svg>
"""

PROFILES = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="currentColor">
  <path d="M0 0h24v24H0z" fill="none"/>
  <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
</svg>
"""

PC = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Moniteur -->
  <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
  <!-- Socle du moniteur -->
  <line x1="12" y1="17" x2="12" y2="21"></line>
  <line x1="8" y1="21" x2="16" y2="21"></line>
</svg>
"""

CALENDAR = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Corps du calendrier -->
  <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
  <!-- Traits indiquant les anneaux du haut -->
  <line x1="16" y1="2" x2="16" y2="6"></line>
  <line x1="8" y1="2" x2="8" y2="6"></line>
  <!-- Ligne séparant l'en-tête du contenu -->
  <line x1="3" y1="10" x2="21" y2="10"></line>
</svg>
"""

TICKET = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Corps du ticket avec coins arrondis -->
  <rect x="2" y="7" width="20" height="10" rx="2" ry="2"/>
  <!-- Ligne de perforation -->
  <line x1="2" y1="12" x2="22" y2="12"/>
</svg>
"""

PHONE = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M22 16.92v3.08a2 2 0 0 1-2.18 2 19.86 19.86 0 0 1-8.63-2.52 19.84 19.84 0 0 1-6.18-6.18A19.86 19.86 0 0 1 1 4.18 2 2 0 0 1 3 2h3.08a2 2 0 0 1 2 1.72l.7 4.2a2 2 0 0 1-.55 1.82l-2.2 2.2a16 16 0 0 0 6.84 6.84l2.2-2.2a2 2 0 0 1 1.82-.55l4.2.7A2 2 0 0 1 22 16.92z"/>
</svg>
"""
PHONE2 = """
<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cadran extérieur -->
  <circle cx="32" cy="32" r="20" stroke="currentColor" stroke-width="2" fill="none"/>
  <!-- Chiffres du cadran (approximés) -->
  <circle cx="32" cy="18" r="1.5" fill="currentColor"/>   <!-- 12 -->
  <circle cx="40" cy="21" r="1.5" fill="currentColor"/>   <!-- 1 -->
  <circle cx="45" cy="28" r="1.5" fill="currentColor"/>   <!-- 2 -->
  <circle cx="45" cy="36" r="1.5" fill="currentColor"/>   <!-- 3 -->
  <circle cx="40" cy="43" r="1.5" fill="currentColor"/>   <!-- 4 -->
  <circle cx="32" cy="46" r="1.5" fill="currentColor"/>   <!-- 5 -->
  <circle cx="24" cy="43" r="1.5" fill="currentColor"/>   <!-- 6 -->
  <circle cx="19" cy="36" r="1.5" fill="currentColor"/>   <!-- 7 -->
  <circle cx="19" cy="28" r="1.5" fill="currentColor"/>   <!-- 8 -->
  <circle cx="24" cy="21" r="1.5" fill="currentColor"/>   <!-- 9 -->
  <!-- Combiné (handset) représenté par un arc -->
  <path d="M20,40 Q32,10 44,40" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>
</svg>

"""