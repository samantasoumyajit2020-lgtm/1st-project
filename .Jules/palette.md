## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Navigation Semantics
**Learning:** Initial auditing revealed primary navigation actions implemented as buttons with `onclick` events. This restricts user control (no new tab support) and degrades accessibility.
**Action:** Systematically refactor navigation buttons to semantic `<a>` tags. Ensure CSS supports this by explicitly setting `display: inline-block` and `text-decoration: none` on the targeted classes/IDs to maintain the visual "button" aesthetic.
