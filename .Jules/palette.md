## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2026-02-05 - Icon-Only Button Accessibility
**Learning:** Icon-only buttons and links are invisible to screen readers without explicit text labels. `aria-label` is a lightweight solution that fixes this without altering the visual design.
**Action:** Always ensure icon-only interactive elements have `aria-label` describing the action, and `aria-hidden="true"` on the SVG icon to prevent redundant or confusing announcements.
