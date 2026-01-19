## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2026-01-19 - Icon-Only Navigation Accessibility
**Learning:** Icon-only navigation bars are common patterns that often fail accessibility checks because they lack text alternatives.
**Action:** Always ensure icon-only links have `aria-label` describing the destination and `aria-hidden="true"` on the decorative SVG. Use `aria-current="page"` to programmatically indicate the active link.
