## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2026-01-28 - Icon-Only Navigation
**Learning:** Icon-only navigation bars in static HTML often lack accessible names and state indicators, making them invisible or confusing to screen readers.
**Action:** Always append `aria-label` to icon-only links and `aria-current="page"` to the active link in static navigation menus.
