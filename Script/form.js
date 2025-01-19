  const form = document.getElementById('form');

  form.addEventListener('submit', function (event) {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();

    if (!username || !password) {
      alert('Por favor, preencha todos os campos!');
      event.preventDefault();
    }
  });