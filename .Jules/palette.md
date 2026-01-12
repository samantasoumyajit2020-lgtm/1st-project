## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2025-05-23 - Analytics Navigation Accessibility
**Learning:** Icon-only navigation links must have descriptive `aria-label` attributes and internal SVGs must be hidden with `aria-hidden="true"` to prevent screen reader redundancy and confusion.
**Action:** When working with icon-only nav bars, always verify `aria-label` presence and use `aria-current="page"` to indicate the active state programmatically.
