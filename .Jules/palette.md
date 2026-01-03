## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-10-27 - Icon-Only Navigation
**Learning:** Icon-only navigation bars are completely invisible to screen readers without `aria-label`. Relying on visual metaphors alone excludes users.
**Action:** Always pair `aria-label` with `aria-hidden="true"` on the SVG itself. Use `aria-current="page"` to programmatically indicate the active state, not just a CSS class.
