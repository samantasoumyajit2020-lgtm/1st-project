document.addEventListener('DOMContentLoaded', () => {
    console.log('Zerospoil app loaded');

    // Password Toggle Functionality
    const togglePassword = document.querySelector('.toggle-password');
    const passwordInput = document.querySelector('#password');

    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function () {
            // Toggle the type attribute
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // Toggle aria-label
            const newLabel = type === 'text' ? 'Hide password' : 'Show password';
            this.setAttribute('aria-label', newLabel);

            // Toggle the eye icon style (optional visual feedback)
            this.style.opacity = type === 'text' ? '1' : '0.5';
        });
    }
});
