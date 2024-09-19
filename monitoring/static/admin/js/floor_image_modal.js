// monitoring/static/admin/js/floor_image_modal.js

function showModal(imageUrl) {
  // Создаем элементы модального окна
  const modal = document.createElement('div');
  modal.style.position = 'fixed';
  modal.style.top = '0';
  modal.style.left = '0';
  modal.style.width = '100%';
  modal.style.height = '100%';
  modal.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
  modal.style.display = 'flex';
  modal.style.justifyContent = 'center';
  modal.style.alignItems = 'center';
  modal.style.zIndex = '10000';
  modal.id = 'floorModal';

  const modalContent = document.createElement('div');
  modalContent.style.position = 'relative';
  modalContent.style.padding = '20px';
  modalContent.style.backgroundColor = '#fff';
  modalContent.style.borderRadius = '5px';
  modalContent.style.width = '70%';  // Размер модального окна (60% ширины экрана)
  modalContent.style.maxWidth = '1000px';  // Максимальная ширина модального окна
  modalContent.style.textAlign = 'center';

  const closeBtn = document.createElement('span');
  closeBtn.innerHTML = '&times;';
  closeBtn.style.position = 'absolute';
  closeBtn.style.top = '10px';
  closeBtn.style.right = '15px';
  closeBtn.style.fontSize = '24px';
  closeBtn.style.cursor = 'pointer';
  closeBtn.onclick = function() {
      document.body.removeChild(modal);
  };

  // Заголовок модального окна
  const title = document.createElement('h2');
  title.innerText = 'Просмотр схемы этажа';
  title.style.marginBottom = '20px';

  const image = document.createElement('img');
  image.src = imageUrl;
  image.style.maxWidth = '100%';
  image.style.maxHeight = '800px';  // Максимальная высота изображения

  // Добавляем элементы в модальное окно
  modalContent.appendChild(closeBtn);
  modalContent.appendChild(title);
  modalContent.appendChild(image);
  modal.appendChild(modalContent);
  document.body.appendChild(modal);

  // Закрытие модального окна при клике на фон
  modal.addEventListener('click', function(event) {
      if (event.target === modal) {
          document.body.removeChild(modal);
      }
  });
}
