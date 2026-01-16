## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-24 - Icon-Only Navigation Accessibility
**Learning:** The application uses icon-only navigation bars which lack text alternatives, making them inaccessible to screen readers. SVGs inside these links can also create "noisy" output if not hidden.
**Action:** Ensure all icon-only interactive elements have descriptive `aria-label` attributes and internal SVGs are marked with `aria-hidden="true"`. Use `aria-current="page"` for active navigation states.
