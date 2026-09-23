# 🧠 AI Agent Skills Repository

<p align="center">
  <b><a href="#-english">English</a></b> • <b><a href="#-ozbek-tilida">O'zbek tili</a></b>
</p>

---

<a name="-ozbek-tilida"></a>
## 🇺🇿 O'zbek Tilida

Google Antigravity va boshqa zamonaviy sun'iy intellekt agentlari (Gemini CLI, Claude Code, Codex) uchun maxsus ishlab chiqilgan professional **mahoratlar (skillar)** to'plami.

Har bir skill o'z ichiga nufuzli manbalar, kitoblar tahlili, tizimli operatsion qoidalar va amaliy kod namunalarini qamrab olgan.

---

### 📦 Mavjud Skillar Katalogi

#### 1. `ux-ui-design`
> **Katta darajadagi (Senior) UI/UX Dizayner va Dizayn Tizimlari Me'mori**

Ushbu skill **16 ta professional UI/UX kitoblari** (500 000 dan ortiq so'z tahlili) asosida yaratilgan:
- **8pt To'r (Grid) Tizimi**: Barcha margin, padding va masofalar 8 ga karrali (Filipiuk & Malewicz qoidalari).
- **Komponentlar Anatomiyasi**: Tugmalar ierarxiyasi (horizontal padding 2x katta), bir ustunli formalar va chegaralangan to'rtburchak inputlar.
- **Ranglar Fizikasi**: Mutlaq qora rangdan saqlanish (`#000000` emas, `#18181B`), Dark Mode uchun desaturatsiya qilingan palitra va WCAG 2.1 kontrasti.
- **Tipografika**: 1.125 / 1.200 shkalasi va o'qish qulayligi o'lchovlari.
- **7 Bosqichli UX Jarayoni**: Qog'ozdagi eskizlardan tortib dasturchiga topshirishgacha (Csaba Házi).
- **Jonli Namunalar**: `examples/` papkasida tayyor CSS tokenlar va HTML komponentlar; `scripts/` papkasida WCAG kontrastini tekshiruvchi skript.

👉 **Buyruq (Slash Command)**: `/ux-ui-design`  
👉 **Batafsil**: [skills/ux-ui-design/SKILL.md](./skills/ux-ui-design/SKILL.md)

---

#### 2. `general-design`
> **Universal Vizual Dizayn, Kompozitsiya va Grafik Asoslar Me'mori**

Grafik dizayn olamining **8 ta klassik durdona kitoblari** asosida shakllantirilgan:
- **Robin Uilyamsning CRAP Qonuniyati**:
  - *Contrast (Kontrast)* — Agar ikki element bir xil bo'lmasa, ularni tubdan farqlang.
  - *Repetition (Takrorlash)* — Ritm va brend birligi uchun elementlarni takrorlang.
  - *Alignment (Tekislash)* — Tasodifiy joylashtirish taqiqlanadi; har bir element ko'rinmas chiziqqa ulanishi shart.
  - *Proximity (Yaqinlik)* — Bog'liq narsalarni bir guruhga jamlang.
- **To'rlar va Setkalar (Grid Architecture)**: 12 ustunli modulli to'rlar, baseline grid (vertikal ritm), margin va gutterlar.
- **Kompozitsiya Qonunlari**: Uchlik qoidasi (Rule of Thirds), Oltin kesim va negativ fazo (Negative Space).
- **Logo Modernism (Taschen)**: Minimalist geometrik logotiplar va Gestalt ramzlari.
- **Dizayn Tafakkuri (Bryan Lawson)**: Dizaynerlar qanday fikrlaydi va ijodiy muammolarni tizimli yechish.

👉 **Buyruq (Slash Command)**: `/general-design`  
👉 **Batafsil**: [skills/general-design/SKILL.md](./skills/general-design/SKILL.md)

---

#### 3. `landing-page`
> **Yuqori Konversiyali Sotuvchi Saytlar va Kopirayting Me'mori**

Aziz Axtamovning (Obsess Marketing) amaliyotda sinalgan **19 ta qadamli sotuvchi sayt metodologiyasi** asosida:
- **Dastlabki 3 Soniyada E'tibor Qozonish**: 1-ekranda auditoriya chaqiruvi, asosiy sarlavha (Headline) va Jon Keypls (John Caples) qoidasi bo'yicha ikkinchi darajali sarlavha (Subheadline).
- **Og'riq va Qutqaruv**: Auditoriya og'rig'ini kuchaytirish va yagona mantiqiy yechim taqdim etish.
- **Rad Etib Bo'lmas Taklif (Grand Offer)**: Bonuslar to'plami, narx qiymatini ochib berish (Value Stacking) va aniq raqamlarda ROI hisoblash.
- **Psixologik To'siqlar**: Xavfni yo'qotuvchi 100% kafolat, "Bu hamma uchun emas" qat'iy filtri va sun'iy bo'lmagan cheklovlar.
- **Kuchli Tugmalar (CTA)**: Derek Xelpern (Derek Halpern) qoidasi bo'yicha foyda keltiruvchi faol tugmalar ("Yuborish" emas, "Ma'lumotni qo'lga kiritish").
- **Mijozlarni Qaytarish**: Retargeting piksellari va e'tirozlarni yo'q qiluvchi FAQ bloki.

👉 **Buyruq (Slash Command)**: `/landing-page`  
👉 **Batafsil**: [skills/landing-page/SKILL.md](./skills/landing-page/SKILL.md)

---

#### 4. `grill-me`
> **Reja va Loyiha Arxitekturasini Sinovdan O'tkazuvchi Qat'iy Intervyuer**

Mett Pokokning (Matt Pocock) mashhur arxitektura testi tizimi asosida:
- Kod yozishdan oldin texnik reja, arxitektura yoki loyiha g'oyasini bosqichma-bosqich, **bittadan savol berish** orqali chuqur tahlil qiladi.
- Kutilmagan xatoliklar (edge cases), xavfsizlik chegaralari, ma'lumotlar yaxlitligi va zaif nuqtalarni oldindan aniqlaydi.
- Shoshilinch va xom rejalarni amalga oshirishdan saqlab, qimmatli vaqt va resurslarni tejaydi.

👉 **Buyruq (Slash Command)**: `/grill-me`  
👉 **Batafsil**: [skills/grill-me/SKILL.md](./skills/grill-me/SKILL.md)

---

### 🚀 O'rnatish Qo'llanmasi

#### 1. Kompyuteringizdagi Barcha Loyihalar Uchun (Global)
PowerShell terminalida ushbu buyruqni bajaring:
```powershell
Copy-Item -Recurse -Force "skills\*" "$env:USERPROFILE\.gemini\config\skills\"
```

#### 2. Alohida Bitta Loyiha Ichiga O'rnatish (Lokal)
O'z loyihangiz papkasida:
```powershell
Copy-Item -Recurse -Force "skills\*" ".agents\skills\"
```

#### 3. `npx skills` Orqali Dunyo Bo'ylab O'rnatish
Istalgan dasturchi terminal orqali to'g'ridan-to'g'ri o'rnatib olishi mumkin:
```bash
# UI/UX dizayn skillini yuklash
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "ux-ui-design"

# Umumiy dizayn (CRAP) skillini yuklash
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "general-design"

# Sotuvchi sahifalar skillini yuklash
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "landing-page"

# Arxitektura tekshiruvchisini yuklash
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "grill-me"
```

---
---

<a name="-english"></a>
## 🇬🇧 English

A curated collection of production-ready, battle-tested custom skills for [Antigravity](https://antigravity.dev) and compatible AI developer assistants (Gemini CLI, Claude Code, Codex).

Each skill packages deep domain mastery, systematic operating procedures, and authoritative reference materials.

---

### 📦 Available Skills Catalog

#### 1. `ux-ui-design`
> **Senior UX/UI Design & Design Systems Architect**

Grounded in **16 professional UI/UX books and resources** (over 500,000 words analyzed):
- Layouts, 8pt spatial grid system, visual rhythm (Michael Filipiuk & Michal Malewicz rules)
- Component physics (action buttons, single-column forms, visible boundary inputs)
- Color theory (no pure black `#000000`, dual light/dark palettes, WCAG contrast)
- Typography scale and readability measures
- End-to-end 7-step UX process (from paper sketches to dev handoff)
- Live design tokens, HTML components demo, and WCAG contrast ratio script

👉 **Slash Command**: `/ux-ui-design`  
👉 **Details**: [skills/ux-ui-design/SKILL.md](./skills/ux-ui-design/SKILL.md)

---

#### 2. `general-design`
> **Universal Visual Foundations, Grids & Graphic Design Architect**

Grounded in **8 foundational design masterpieces**:
- **Robin Williams's CRAP Laws**: Contrast, Repetition, Alignment, Proximity
- **Grid Architecture**: 12-column modular grids, baseline rhythm, margins & gutters
- **Composition Systems**: Rule of Thirds, Golden Spiral, negative space mastery
- **Logo Modernism**: Geometric reduction, Gestalt negative space, timeless symbols
- **Design Thinking (Bryan Lawson)**: Cognitive problem solving and creative constraints

👉 **Slash Command**: `/general-design`  
👉 **Details**: [skills/general-design/SKILL.md](./skills/general-design/SKILL.md)

---

#### 3. `landing-page`
> **High-Conversion Selling Website & Funnel Copywriting Architect**

Grounded in **Aziz Axtamov's proven 19-step selling website framework** (Obsess Marketing):
- **First 3 Seconds**: Audience callout, hero visual anchor, high-converting headline & subheadline (John Caples rule)
- **Emotional Agitation**: Pain-amplification and single-solution positioning
- **The Grand Offer**: High-value bonus packaging, value stacking with price breakdown, and quantifiable ROI
- **Psychological Triggers**: Risk-reversal guarantees, "not for everyone" audience filters, and ethical scarcity
- **High-Impact CTA**: Benefit-driven action buttons (Derek Halpern rule)
- **Lead Capture & Retention**: Pixel tracking and objection-crushing FAQ

👉 **Slash Command**: `/landing-page`  
👉 **Details**: [skills/landing-page/SKILL.md](./skills/landing-page/SKILL.md)

---

#### 4. `grill-me`
> **Relentless Plan & Architecture Stress-Tester**

Inspired by Matt Pocock's [skills/grill-me](https://github.com/mattpocock/skills):
- Iterative, single-question-at-a-time technical interview to stress-test designs before code is written
- Dissects failure modes, edge cases, data integrity, and security boundaries
- Constructively skeptical persona that exposes hidden assumptions and prevents costly rework

👉 **Slash Command**: `/grill-me`  
👉 **Details**: [skills/grill-me/SKILL.md](./skills/grill-me/SKILL.md)

---

### 🚀 Installation

#### Global Installation (All Projects on your Machine)
```powershell
# Copy all skills to global configuration
Copy-Item -Recurse -Force "skills\*" "$env:USERPROFILE\.gemini\config\skills\"
```

#### Local Installation (Specific Project Only)
```powershell
# Copy into your repository
Copy-Item -Recurse -Force "skills\*" ".agents\skills\"
```

#### Install via `npx skills` (Global CLI)
```bash
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "ux-ui-design"
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "general-design"
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "landing-page"
npx skills use "https://github.com/T-Iskandarov/Skills" --skill "grill-me"
```

---

## 📁 Repository Structure

```text
Skills/
├── README.md                      ← Bilingual documentation & catalog
├── .gitignore                     ← Clean git tracking
└── skills/
    ├── ux-ui-design/              ← UX/UI Design Expert (16 books)
    │   ├── SKILL.md
    │   ├── examples/              ← Live CSS tokens & components
    │   ├── scripts/               ← Contrast ratio checker
    │   └── references/
    ├── general-design/            ← Visual Foundations & CRAP (8 books)
    │   ├── SKILL.md
    │   └── references/
    ├── landing-page/              ← 19-Step Selling Landing Page Architect
    │   ├── SKILL.md
    │   └── references/
    └── grill-me/                  ← Architecture Stress-Tester
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

---

## 📄 License
MIT — Free to use, share, and scale.
