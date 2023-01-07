//Login js

const password = document.querySelector('#password');
const togglePassword = document.querySelector('.show_password');

togglePassword.addEventListener('click', function () {
    if (password.type === 'password') {
        password.type = 'text'
        togglePassword.src = './assets/icons/eye-off 1.svg'
    } else {
        password.type = 'password'
        togglePassword.src = './assets/icons/eye.svg'
    }
})