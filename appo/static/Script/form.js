const form = document.getElementById('form');

if (form) {
    form.addEventListener('submit', function (event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!username || !password) {
      alert('Por favor, preencha todos os campos!');
      event.preventDefault();
    }
  });
}

const alerts = document.querySelectorAll('.alert');

const alertTimeout = 5000; 

alerts.forEach(alert => {
    setTimeout(() => {
        alert.remove();
    }, alertTimeout);
});