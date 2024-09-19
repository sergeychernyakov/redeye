№## README.md

# SurvEye

## Описание проекта

**SurvEye** — это система управления камерами видеонаблюдения, созданная с использованием Python и open-source решений. Проект разработан для торговых центров и промышленных объектов, предоставляя удобный интерфейс для управления камерами, просмотра видеопотоков и мониторинга инцидентов на объекте.

Проект включает:
- Отображение интерактивной схемы объекта с возможностью размещения иконок камер.
- Панель управления для добавления/редактирования камер, пользователей и ролей.
- Реализацию получения данных от видеоаналитики в реальном времени.
- Таблицу инцидентов с фото и возможностью клика для просмотра подробностей.
- Управление видеопотоками камер через интеграцию с **Frigate** (open-source решение).

## Основные возможности

1. **Авторизация и управление пользователями**:
   - Регистрация и авторизация по логину и паролю.
   - Административный интерфейс для управления ролями пользователей, доступами и профилями разрешений.

2. **Отображение схемы объекта**:
   - Отображение карты или пользовательской схемы объекта с помощью **OpenLayers** или **Leaflet**.
   - Возможность добавления камеры на карту через интерфейс (правый клик мыши).
   - Поддержка различных типов подложек (например, Яндекс карты и пользовательские схемы).

3. **Мониторинг событий**:
   - Онлайн-таблица с сообщениями от видеоаналитики (например, нарушения, такие как курение, драки и т.д.).
   - В реальном времени отображаются события с возможностью клика для подробного просмотра инцидента.

4. **Видеоаналитика**:
   - Интеграция с **Kafka** и **Redis** для передачи данных видеоаналитики.
   - Хранение данных в **ClickHouse** (фото инцидентов) и **PostgreSQL** (статистика и настройки).

5. **Управление камерами**:
   - Поддержка видеопотоков камер через **Frigate**.
   - Панель управления камерой с отображением всех параметров.

## Используемые технологии

Проект строится на использовании следующих технологий:

### Backend:
- **Python**: Основной язык для разработки серверной части.
- **Django**: Веб-фреймворк для создания API и управления данными.
- **Django REST Framework**: Реализация REST API для взаимодействия с фронтендом.
- **Kafka и Redis**: Передача данных видеоаналитики в реальном времени.
- **ClickHouse**: Хранение фото инцидентов.
- **PostgreSQL**: Хранение настроек, статистики и данных пользователей.
- **Frigate**: Open-source решение для работы с видеопотоками камер наблюдения.

### Frontend:
- **React.js** или **Vue.js**: Для создания интерактивного пользовательского интерфейса.
- **OpenLayers** или **Leaflet**: Для работы с картами и схемами объекта.

### Интеграции:
- **Frigate**: Для работы с видеопотоками камер.
- **Yandex Maps**: Для использования карт в качестве подложек.
  
## Установка и развертывание

### Требования:

1. **Python 3.8+**
2. **PostgreSQL**
3. **ClickHouse**
4. **Kafka** и **Redis**
5. **Node.js** (для фронтенда, если используете React или Vue.js)

### Шаги установки:

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/yourusername/surveye.git
   cd surveye
   ```

2. **Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. **Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

4. **Установка зависимостей**:
   Убедитесь, что у вас установлен `pipenv` или используйте `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

5. **Настройка базы данных**:
   Создайте базу данных PostgreSQL:
   ```bash
   createdb surveye_db
   ```

   Примените миграции для настройки схемы базы данных:
   ```bash
   python manage.py migrate
   ```

6. **Настройка ClickHouse**:
   Установите ClickHouse для хранения данных инцидентов:
   ```bash
   sudo apt-get install clickhouse-server clickhouse-client
   ```

7. **Запуск Django сервера**:
   Для запуска сервера разработки:
   ```bash
   python manage.py runserver 8001
   ```

8. **Export the Installed Packages**:
    ```bash
    pip freeze > requirements.txt
    ```

9. **Изменения в базе данных**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
10. ** Seeds **
    ```bash
    python manage.py seeder
    ```
11 ** Пересоздать базу данных **
    ```bash
    dropdb surveye_db 
    createdb surveye_db
    python manage.py makemigrations
    python manage.py migrate
    python manage.py seeder

    python manage.py flush # очистить
    ```

### Переменные окружения

Перед запуском проекта, создайте файл `.env` в корневой папке и добавьте туда следующие переменные:

```bash
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL=postgres://username:password@localhost/surveye_db
REDIS_URL=redis://localhost:6379
KAFKA_BROKER_URL=kafka://localhost:9092
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=9000
```

---

## Author

Sergey Chernyakov  
Telegram: [@AIBotsTech](https://t.me/AIBotsTech)



план:

  create map

Структура должа быть такой:
  create Объект (Торговый центр, склад или другое помещение) - может имть несколько карт
  карта Map может быть нескольких типов - подложка или яндекс карта
  карта типа подложка может иметь несколько этажей
  Детектор принадлежик карте Map, карта может иметь много детекторов
  Событие - инцидент принадлежит камере

  этаж может иметь много камер
  карта может иметь много камер если тип - яндекс


  при добавлении подложки - давать выбор фона


rtsp://admin:campass911@192.168.9.161:554/stream1
pptp 178.209.97.254 argo1 X9eDB@Mxp_

