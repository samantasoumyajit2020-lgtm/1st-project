## 2025-01-26 - Password Visibility Accessibility
**Learning:** Interactive elements like password toggles must be semantic `<button>` elements, not `<span>` or `<div>`, to ensure keyboard accessibility and proper screen reader support. Dynamic `aria-label` updates are essential for stateful buttons.
**Action:** When implementing toggles, always use `<button type="button">`, manage `aria-label` state in JS, and ensure icons reflect the current state (e.g., eye vs eye-off).
