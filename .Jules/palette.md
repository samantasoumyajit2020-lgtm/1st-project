# 1st-project

## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Icon-Only Navigation
**Learning:** Icon-only navigation links are invisible to screen readers without explicit labels. Using `aria-current="page"` is essential for indicating the active route in a static site structure.
**Action:** Always pair `aria-label` with `aria-hidden="true"` on the internal SVG for icon-only buttons to prevent redundant announcements.
