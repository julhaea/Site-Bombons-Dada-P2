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

document.addEventListener('DOMContentLoaded', () => {
  const modal = document.getElementById('popupconfirma');
  const confirmButton = document.getElementById('confirmaexc');
  const cancelButton = document.getElementById('cancelaexc');
  const modalMessage = document.getElementById('popup-p');

  let deleteForm;

  document.querySelectorAll('.btn-excluir').forEach(button => {
      button.addEventListener('click', (event) => {
          event.preventDefault(); // Impede o comportamento padrão do botão

          modal.style.display = 'flex';

          const productName = button.getAttribute('data-produto-name');
          modalMessage.textContent = `Tem certeza de que deseja excluir o produto "${productName}"?`;

          
          deleteForm = button.closest('form');
      });
  });

  confirmButton.addEventListener('click', () => {
      if (deleteForm) {
          deleteForm.submit(); // Manda o form e fecha
      }
      modal.style.display = 'none';
  });

  cancelButton.addEventListener('click', () => {
      modal.style.display = 'none'; // Fecha sem excluir
  });
});