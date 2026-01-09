## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2025-01-09 - Navigation Icon Accessibility
**Learning:** Icon-only navigation bars are a common pattern that often excludes screen reader users. Adding `aria-label` provides essential context, while `title` offers a native tooltip for mouse users.
**Action:** Ensure all icon-only interactive elements include `aria-label` and `title`. Add `aria-hidden="true"` to the internal SVG to prevent screen readers from announcing "image" or reading paths.
