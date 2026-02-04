## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2025-02-04 - Icon-Only Navigation Accessibility
**Learning:** Icon-only navigation bars are common but often inaccessible. Explicitly adding `aria-label` to links and `aria-current="page"` to the active item makes them usable for screen readers without changing the visual design.
**Action:** Always check icon-only buttons/links for `aria-label` and `aria-hidden` on the SVG.
