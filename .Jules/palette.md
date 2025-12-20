## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-22 - Icon-Only Navigation
**Learning:** Icon-only navigation bars are common in modern UI but are completely invisible to screen readers without explicit labeling. Adding `aria-label` to the container links and `aria-hidden="true"` to the decorative SVGs restores context.
**Action:** Always audit bottom navigation bars for text alternatives. Use `aria-current="page"` to indicate the active state programmatically, not just visually with color.
