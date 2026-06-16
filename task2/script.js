// Кейс-задача №2. Простейший счётчик (counter) с использованием стилизации интерфейса

const plusBtn = document.getElementById('plus-btn');
const minusBtn = document.getElementById('minus-btn');
const resultBox = document.getElementById('result');
const messageBox = document.getElementById('message');

const MAX_VALUE = 10;
const MIN_VALUE = -10;

let count = 0;

function updateUI() {
  resultBox.textContent = count;

  // Обновление цвета фона окошка результата
  resultBox.classList.remove('positive', 'negative', 'zero');
  if (count === 0) {
    resultBox.classList.add('zero');
  } else if (count > 0) {
    resultBox.classList.add('positive');
  } else {
    resultBox.classList.add('negative');
  }

  // Блокировка кнопок при достижении предельных значений
  plusBtn.disabled = count >= MAX_VALUE;
  minusBtn.disabled = count <= MIN_VALUE;

  // Сообщение об экстремальном значении
  if (count === MAX_VALUE || count === MIN_VALUE) {
    messageBox.textContent = 'Вы достигли экстремального значения';
  } else {
    messageBox.textContent = '';
  }
}

plusBtn.addEventListener('click', () => {
  if (count < MAX_VALUE) {
    count += 1;
    updateUI();
  }
});

minusBtn.addEventListener('click', () => {
  if (count > MIN_VALUE) {
    count -= 1;
    updateUI();
  }
});

// Инициализация интерфейса при загрузке страницы
updateUI();
