// script.js

const loginForm = document.getElementById('login-form');
const loginMessage = document.getElementById('login-message');

const users = [
    { username: 'admin', password: 'admin123', role: 'admin' },
    { username: 'user', password: 'user123', role: 'user' },
    { username: 'recycler', password: 'recycler123', role: 'recycler' }
];

loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    const user = users.find((user) => user.username === username && user.password === password && user.role === role);

    if (user) {
        if (role === 'admin') {
            // Admin login successful, redirect to admin dashboard
            window.location.href = 'admin-dashboard.html';
        } else if (role === 'user') {
            // User login successful, redirect to user dashboard
            window.location.href = 'user-dashboard.html';
        } else if (role === 'recycler') {
            // Moderator login successful, redirect to moderator dashboard
            window.location.href = 'recycler-dashboard.html';
        }
    } else {
        loginMessage.textContent = 'Invalid username or password or role';
    }
});