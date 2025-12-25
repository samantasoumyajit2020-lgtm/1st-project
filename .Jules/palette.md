## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Icon-Only Navigation Accessibility
**Learning:** Icon-only navigation links and buttons are invisible to screen readers without explicit text alternatives.
**Action:** Always add `aria-label` to icon-only interactive elements and `aria-hidden="true"` to the internal decorative SVGs. Use `aria-current="page"` for active navigation states.
