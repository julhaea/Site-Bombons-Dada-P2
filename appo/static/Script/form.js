//forms.js
 const form = document.getElementById('form');

  form.addEventListener('submit', function (event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!username || !password) {
      alert('Por favor, preencha todos os campos!');
      event.preventDefault();
    }
  });

// Seleciona todos os elementos com a classe 'alert'
const alerts = document.querySelectorAll('.alert');

// Define o tempo de exibição do alerta (em milissegundos)
const alertTimeout = 5000; // 5 segundos

// Itera sobre cada alerta e remove após o tempo definido
alerts.forEach(alert => {
    setTimeout(() => {
        alert.remove(); // Remove o alerta do DOM
    }, alertTimeout);
});