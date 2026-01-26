## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Icon-only Navigation Accessibility
**Learning:** Navigation bars with icon-only links are unusable for screen reader users without explicit accessible names.
**Action:** Always add `aria-label` to icon-only links and `aria-hidden="true"` to the decorative SVG icons inside them. Also use `aria-current="page"` for the active link.
