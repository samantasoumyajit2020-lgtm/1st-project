## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Accessible Icon Navigation
**Learning:** Icon-only navigation links require `aria-label` for context and `aria-hidden='true'` on the SVG to prevent redundant announcements. `aria-current='page'` provides essential context for the active state.
**Action:** Audit all icon-only buttons/links for these attributes during implementation.
