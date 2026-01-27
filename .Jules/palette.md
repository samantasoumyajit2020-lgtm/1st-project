## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2026-01-27 - Accessible Bottom Navigation
**Learning:** Icon-only navigation bars are completely invisible to screen readers without `aria-label` attributes. `aria-current="page"` is critical for indicating the active route in static sites where URL changes might not be announced.
**Action:** Always verify icon-only links with `aria-label` and ensure SVG icons are hidden (`aria-hidden="true"`) to prevent "graphic" announcements.
