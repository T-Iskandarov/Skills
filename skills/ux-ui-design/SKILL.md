---
name: ux-ui-design
description: >-
  Use this skill for any UX/UI design task: creating layouts, selecting color schemes,
  defining typographic hierarchies, crafting design systems, forms, buttons, cards,
  navigation, accessibility (WCAG), user research, wireframing, microinteractions, 
  and landing page conversion optimization. Grounded in 16 professional design books 
  and comprehensive guides (over 500,000 words analyzed).
---

# UX/UI Design Expert System

## Overview
This skill elevates the agent to a senior-level UX/UI designer and design systems architect. It strictly applies the empirical rules, psychological principles, and visual standards synthesized from **16 professional design books and resources** stored in `skills/ux-ui-design/references/`.

---

## The 16 Grounding References

| File | Source & Author | Focus & Key Insights |
|---|---|---|
| [ui-design-principles.md](./references/ui-design-principles.md) | **UI Design Principles** (Michael Filipiuk, 487 pgs) | Grids, 8pt spatial system, typography scale, saturation limit, soft shadows, microinteractions, design handoff |
| [ui-design-roadmap.md](./references/ui-design-roadmap.md) | **The Ultimate UI Roadmap** (Michael Filipiuk) | Step-by-step UI mastery, component tokens, practical workflows |
| [101-dos-and-donts.md](./references/101-dos-and-donts.md) | **101 Dos & Don'ts of UI Design** (Pixsel Academy) | Concrete visual dos/don'ts: human copy, input masks, Fitts's law, Gutenberg z-pattern |
| [ui-design-tips.md](./references/ui-design-tips.md) | **UI Design Tips** (Michal Malewicz) | Tested real-world rules: single-column forms, button padding, carousel tabs, label proximity |
| [practical-ui.md](./references/practical-ui.md) | **Practical UI** | Component anatomy, visual weight balance, responsive breakpoints |
| [ui-pedia.md](./references/ui-pedia.md) | **UI Pedia** | Complete UI element directory, interactive state definitions |
| [psychology-of-user.md](./references/psychology-of-user.md) | **Psychology of User** | Cognitive load reduction, Hick's Law, Miller's rule, mental models |
| [7-step-ux-process.md](./references/7-step-ux-process.md) | **7STEPUX** (Csaba Házi) | Plan → Discover → Explore → Define → Design → Validate → Deliver |
| [universal-principles-of-ux.md](./references/universal-principles-of-ux.md) | **Universal Principles of UX** (Irene Pereyra) | Core heuristics, error prevention, feedback loops, discoverability |
| [ux-buddy-workbook.md](./references/ux-buddy-workbook.md) | **UX Buddy Workbook** (Bojan Novakovic) | Paper-first sketching, user story mapping, finger-flow testing |
| [user-research-surveys.md](./references/user-research-surveys.md) | **User Researcher's Guide to Surveys** | Unbiased questions, quantitative & qualitative feedback synthesis |
| [selling-website-19-steps.md](./references/selling-website-19-steps.md) | **Sotuvchi Sayt 19 Qadami** (Aziz Axtamov) | Conversion copywriting, above-the-fold value prop, trust anchors |
| [design-systems-top7.md](./references/design-systems-top7.md) | **TOP 7 Design Systems** (Socially Academy) | IBM Carbon, Apple HIG, Google Material 3, Atlassian, Polaris |
| [free-fonts.md](./references/free-fonts.md) | **My Favorite Free Fonts** | Tested typeface pairings: Inter, Plus Jakarta Sans, Outfit, Cabinet Grotesk |
| [free-resources-list.md](./references/free-resources-list.md) | **Ultimate Free Resources List** | Verified vector icon sets, illustrations, 3D assets, contrast tools |
| [what-to-do-next.md](./references/what-to-do-next.md) | **What to do Next** | Design critique, design QA, developer collaboration |

---

## Core Design Laws & Implementation Rules

### 1. Spacing & Grid System (Filipiuk & Malewicz Rules)
- **Base 8pt Grid**: All margins, paddings, dimensions, and gaps MUST be multiples of 8 (8, 16, 24, 32, 40, 48, 64px). Use 4px only for tight micro-spacing (e.g. badges, small icons).
- **Proximity Law (Label to Input)**: The gap between a label and its corresponding input must be `8px`. The gap between an input and the *next* form group must be `24px` to `32px` (at least 3x larger) so relationships are unmistakable.
- **Card Breathing Space**: Never allow card contents to choke the edges. Internal card padding must be minimum `24px` on desktop, `16px` on mobile.

### 2. Button Architecture & Hierarchy
- **Action Clarity**: Button copy must be action-oriented and explicit (`Save Changes`, `Delete Account`, `Create Team`). Never use ambiguous labels like `OK`, `Yes`, or `Submit`.
- **Button Padding Ratio**: Horizontal padding must be `1.5x` to `2x` the vertical padding (e.g., `padding: 12px 24px`). Buttons with equal or tight horizontal padding feel amateurish.
- **Hierarchy Split**:
  - **Primary**: Solid high-contrast background (brand color). Exactly ONE per view.
  - **Secondary**: Outlined or soft tinted background.
  - **Tertiary/Ghost**: Text-only with hover background fill.
  - **Destructive**: Red hue (`#DC2626` or darker) with clear warning confirmation dialog.

### 3. Color & Elevation Physics
- **Never Pure Black**: Do not use `#000000` for dark themes or dark text. Use tinted deep grays (e.g., `#121214`, `#18181B`, `#0F172A`). Pure black creates eye strain and destroys layer elevation.
- **Light & Dark Mode Dual Palettes**: Never invert colors mechanically. Dark mode requires desaturated tones (tone levels 200–500) to prevent retina-burn and contrast vibration.
- **Natural Shadows**:
  - Avoid software defaults (e.g., `0px 4px 8px rgba(0,0,0,0.5)`).
  - Use multi-layered, ultra-soft shadows: e.g., `box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 10px 15px -3px rgba(0,0,0,0.08)`.
  - Ensure light direction is consistent across every component on the page (always from top-center).

### 4. Form UX & Cognitive Load
- **Single-Column Rule**: Default to vertical single-column forms. Multi-column forms disrupt the natural downward scanning momentum (Z/F pattern).
- **Visible Input Boundaries**: Always use full rectangular boxes with subtle borders (`1px solid #E2E8F0`). Underline-only inputs have 30% slower visual recognition.
- **Smart Labels**: Mark only `(optional)` fields explicitly. Eliminate redundant required asterisks (`*`) when almost all fields are mandatory.
- **Inline Validation**: Trigger validation on `blur` or after user pause, not on first keystroke. Show *where* the error is and *how* to solve it.

### 5. Typography Hierarchy & Readability
- **Type Scale Ratio**: Adhere to Major Second (1.125) or Minor Third (1.200) scales:
  - Display / H1: 32px–40px (Bold)
  - H2: 24px–28px (Semi-bold)
  - H3 / Subtitle: 18px–20px (Medium)
  - Body: 15px–16px (Regular) — Never drop body text below 14px.
  - Caption / Helper: 12px–13px (Regular)
- **Line Length (Measure)**: Keep line length between `45` and `75` characters per line (optimal ~65 chars) for long-form reading.

### 6. Design System Alignment (IBM Carbon & Apple HIG)
- **Tokens over Hardcoded Values**: Use design tokens for colors, spacing, and typography (`$color-primary`, `$spacing-md`, `$radius-lg`).
- **Icon Consistency**: Stick to a single stroke-weight and style across the application (all 1.5px outlined or all filled). Never mix icon sets.
- **Empty States & Skeletons**: Always provide informative empty states with a direct CTA. Replace loading spinners with structural skeleton loaders.

---

## 7-Step UX Execution Protocol
When designing an end-to-end interface:
1. **Plan & Goal**: Define user persona and conversion outcome (Aziz Axtamov / Csaba Házi framework).
2. **User Flow & Paper Prototype**: Sketch screen states on paper first; test finger-flow before touching high-fidelity tools.
3. **Information Architecture**: Group features logically; apply Hick's law (reduce choices per screen).
4. **Wireframe**: Establish grid, spacing, and real microcopy (NO lorem ipsum).
5. **Visual Design**: Apply design tokens, WCAG contrast compliance, and typography scale.
6. **Prototype & Validate**: Conduct 5-second impression tests and click-target audits.
7. **Developer Handoff**: Provide exact tokens, interactive states (:hover, :focus, :active, :disabled), and responsive breakpoints.
