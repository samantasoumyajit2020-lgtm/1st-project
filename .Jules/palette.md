## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2026-02-02 - Icon-only Navigation Accessibility
**Learning:** Icon-only navigation links (like bottom nav bars) are completely invisible to screen readers without explicit `aria-label`s.
**Action:** Always verify bottom navigation bars and icon-only buttons with a screen reader or accessibility tool. Ensure internal SVGs are hidden with `aria-hidden="true"` to avoid noise.
