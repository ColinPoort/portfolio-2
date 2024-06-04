const inputs = document.querySelectorAll('.form-group input,.form-group textarea');

inputs.forEach((input) => {
  input.addEventListener('focus', () => {
    input.classList.add('active');
  });

  input.addEventListener('blur', () => {
    if (input.value === '') {
      input.classList.remove('active');
    }
  });

  input.addEventListener('input', () => {
    if (input.value !== '') {
      input.classList.add('active');
    } else {
      input.classList.remove('active');
    }
  });
});