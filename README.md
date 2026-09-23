# 🧠 AI Agent Skills Repository

A curated collection of production-ready, battle-tested custom skills for [Antigravity](https://antigravity.dev) and compatible AI developer assistants (Gemini CLI, Claude Code, Codex).

Each skill packages deep domain mastery, systematic operating procedures, and authoritative reference materials.

---

## 📦 Available Skills Catalog

### 1. `ux-ui-design`
> **Senior UX/UI Design & Design Systems Architect**

Grounded in **16 professional UI/UX books and resources** (over 500,000 words analyzed):
- Layouts, 8pt spatial grid system, visual rhythm (Michael Filipiuk & Michal Malewicz rules)
- Component physics (action buttons, single-column forms, visible boundary inputs)
- Color theory (no pure black `#000000`, dual light/dark palettes, WCAG contrast)
- Typography scale and readability measures
- End-to-end 7-step UX process (from paper sketches to dev handoff)

👉 **Slash Command**: `/ux-ui-design`  
👉 **Details**: [skills/ux-ui-design/SKILL.md](./skills/ux-ui-design/SKILL.md)

---

### 2. `general-design`
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

### 3. `landing-page`
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

### 4. `grill-me`
> **Relentless Plan & Architecture Stress-Tester**

Inspired by Matt Pocock's [skills/grill-me](https://github.com/mattpocock/skills):
- Iterative, single-question-at-a-time technical interview to stress-test designs before code is written
- Dissects failure modes, edge cases, data integrity, and security boundaries
- Constructively skeptical persona that exposes hidden assumptions and prevents costly rework

👉 **Slash Command**: `/grill-me`  
👉 **Details**: [skills/grill-me/SKILL.md](./skills/grill-me/SKILL.md)

---

## 🚀 Installation

### Global Installation (All Projects on your Machine)
```powershell
# Copy all skills to global configuration
Copy-Item -Recurse -Force "skills\*" "$env:USERPROFILE\.gemini\config\skills\"
```

### Local Installation (Specific Project Only)
```powershell
# Copy into your repository
Copy-Item -Recurse -Force "skills\*" ".agents\skills\"
```

---

## 📁 Repository Structure

```text
Skills/
├── README.md                      ← Catalog & documentation
├── .gitignore                     ← Clean git tracking
├── scripts/                       ← Extraction & OCR pipelines
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
