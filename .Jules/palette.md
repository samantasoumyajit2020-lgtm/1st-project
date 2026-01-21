## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Icon-Only Navigation Accessibility
**Learning:** Icon-only navigation links require `aria-label` to be accessible, and inner SVGs must be hidden from screen readers to avoid noise.
**Action:** Ensure all icon-only links in navigation bars have `aria-label` describing the destination and `aria-current="page"` for the active item.
