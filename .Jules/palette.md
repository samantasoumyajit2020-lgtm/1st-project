## 2024-05-22 - Login Form Accessibility
**Learning:** Adding explicit `<label>` tags and converting `<span>` triggers to `<button>` elements significantly improves accessibility without compromising visual design if CSS is carefully scoped.
**Action:** Always prefer semantic HTML (`<button>`, `<label>`) over ARIA patches on generic elements. When adding labels to existing designs, ensure wrapper elements maintain relative positioning contexts for internal icons.

## 2024-05-23 - Semantic Navigation
**Learning:** Replacing JavaScript-based navigation buttons with semantic `<a>` tags improves accessibility and enables native browser features (like "Open in new tab") without breaking existing styles if CSS selectors are robust (e.g., ID-based).
**Action:** Always verify that CSS selectors for buttons (e.g., `#cta-button`) are tag-agnostic or updated to support `<a>` tags when refactoring for semantics.
