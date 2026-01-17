## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-22 - Icon-Only Navigation Accessibility
**Learning:** Icon-only navigation bars are completely inaccessible to screen readers without text alternatives. Adding `aria-label` provides the missing context, while `aria-current="page"` is essential for indicating the active state which color alone cannot convey.
**Action:** For all icon-only interactive elements, strictly mandate `aria-label` and ensure internal SVGs are marked `aria-hidden="true"` to prevent redundant "graphic" announcements.
