document.addEventListener('DOMContentLoaded', () => {
    console.log('Zerospoil app loaded');

    // Password Toggle Functionality
    const togglePassword = document.querySelector('.toggle-password');
    const passwordInput = document.querySelector('#password');

    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function () {
            // Toggle the type attribute
            const isPassword = passwordInput.getAttribute('type') === 'password';
            const type = isPassword ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // Toggle accessibility attribute
            this.setAttribute('aria-label', isPassword ? 'Hide password' : 'Show password');

            // Toggle the eye icon style (optional visual feedback)
            this.style.opacity = type === 'text' ? '1' : '0.5';
        });
    }
});
