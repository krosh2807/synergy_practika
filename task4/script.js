// Кейс-задача №4. Интерактивный калькулятор

const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const resultBox = document.getElementById('result');

function getNumbers() {
  const a = parseFloat(num1Input.value.replace(',', '.'));
  const b = parseFloat(num2Input.value.replace(',', '.'));
  return { a, b };
}

function showResult(value) {
  resultBox.classList.remove('error');
  resultBox.textContent = value;
}

function showError(message) {
  resultBox.classList.add('error');
  resultBox.textContent = message;
}

function isValidInput(a, b) {
  return !Number.isNaN(a) && !Number.isNaN(b);
}

document.getElementById('sum-btn').addEventListener('click', () => {
  const { a, b } = getNumbers();
  if (!isValidInput(a, b)) {
    showError('Ошибка: введите корректные числа');
    return;
  }
  showResult(a + b);
});

document.getElementById('diff-btn').addEventListener('click', () => {
  const { a, b } = getNumbers();
  if (!isValidInput(a, b)) {
    showError('Ошибка: введите корректные числа');
    return;
  }
  showResult(a - b);
});

document.getElementById('mult-btn').addEventListener('click', () => {
  const { a, b } = getNumbers();
  if (!isValidInput(a, b)) {
    showError('Ошибка: введите корректные числа');
    return;
  }
  showResult(a * b);
});

document.getElementById('div-btn').addEventListener('click', () => {
  const { a, b } = getNumbers();
  if (!isValidInput(a, b)) {
    showError('Ошибка: введите корректные числа');
    return;
  }
  if (b === 0) {
    showError('Ошибка: деление на ноль');
    return;
  }
  showResult(a / b);
});
