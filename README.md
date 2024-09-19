### README.md

# RedEye

## Описание проекта

**RedEye** — это система мониторинга и видеоаналитики, предназначенная для классификации и учета краснокнижных видов животных и растений. Проект разработан для ведения наблюдений за редкими и исчезающими видами с помощью интерактивной карты и видеоматериалов. Система предоставляет удобный интерфейс для добавления новых наблюдений и управления ими.

Проект включает:
- Отображение интерактивной карты с использованием **Яндекс Карт** для размещения меток краснокнижных видов.
- Возможность добавления новых записей о краснокнижных животных и растениях с указанием геометки, загрузкой фото или видео и добавлением текстового комментария.
- Классификацию видов на основе загруженных видеоматериалов с использованием методов видеоаналитики.
- Удобное меню для добавления объектов наблюдения при нажатии правой кнопкой мыши на карту.

## Основные возможности

1. **Добавление и управление наблюдениями**:
   - Возможность добавления краснокнижного животного или растения через контекстное меню при нажатии правой кнопкой мыши на карте.
   - Административный интерфейс для управления ролями пользователей, доступами и профилями разрешений.

2. **Отображение наблюдений на карте**:
   - Интерактивная карта с возможностью фильтрации по видам: животные или растения.
   - Отображение информации о каждом объекте при клике на метку.
   - Возможность редактирования или удаления добавленных записей.

3. **Видеоаналитика**:
   - Классификация краснокнижных видов на основе загруженных видеофайлов.
   - Автоматическое определение видов и их характеристик с помощью алгоритмов машинного обучения.

4. **Интеграция с Яндекс Картами**:
   - Использование **Яндекс Карт** в качестве единственного типа подложки для отображения данных.
   - Поддержка всех стандартных возможностей Яндекс Карт: масштабирование, панорамы и т.д.

## Используемые технологии

Проект строится на использовании следующих технологий:

### Backend:
- **Python**: Основной язык для разработки серверной части.
- **Django**: Веб-фреймворк для создания API и управления данными.
- **Django REST Framework**: Реализация REST API для взаимодействия с фронтендом.
- **PostgreSQL**: Хранение данных о наблюдениях и пользователях.
- **Kafka и Redis**: Передача данных видеоаналитики в реальном времени.

### Frontend:
- **Yandex Maps API**: Для отображения карты и работы с геометками.

### Видеоаналитика:
- **OpenCV**: Для обработки и анализа видеоматериалов.
- **TensorFlow/PyTorch**: Для классификации объектов на основе загруженных видеоматериалов.

## Установка и развертывание

### Требования:

1. **Python 3.8+**
2. **PostgreSQL**

### Шаги установки:

1. **Клонирование репозитория**:
   ```bash
   git clone https://github.com/sergeychernyakov/redeye.git
   cd redeye
   ```

2. **Создание виртуального окружения**:
   ```bash
   python3 -m venv venv
   ```

3. **Активация виртуального окружения**:
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
   createdb redeye_db
   ```

   Примените миграции для настройки схемы базы данных:
   ```bash
   python manage.py migrate
   ```

6. **Запуск Django сервера**:
   Для запуска сервера разработки:
   ```bash
   python manage.py runserver 8001
   ```

7. **Export the Installed Packages**:
    ```bash
    pip freeze > requirements.txt
    ```


8. **Изменения в базе данных**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
9. ** Seeds **
    ```bash
    python manage.py seeder
    ```
10 ** Пересоздать базу данных **
    ```bash
    dropdb redeye_db 
    createdb redeye_db
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
DATABASE_URL=postgres://username:password@localhost/redeye_db
```

---

## Автор

Sergey Chernyakov  
Telegram: [@AIBotsTech](https://t.me/AIBotsTech)




Национальный парк «Куршская коса» 

Кого можно увидеть: перелетных птиц

Куршская коса, расположенная в Калининградской области, — это уникальный природный объект, одна из самых больших песчаных кос в мире протяженностью почти 100 км. Ее часто называют птичьим мостом, так как она находится на пути птиц, ежегодно мигрирующих из Европы в Африку и обратно. Весной и осенью над Куршской косой пролетают миллионы пернатых, многие из них приземляются на берегу, чтобы отдохнуть. Здесь можно увидеть цапель, аистов, журавлей, лебедей, мелких певчих птиц и многих других. Очень удобно наблюдать за ними с высоты песчаных дюн, в бинокль или подзорную трубу. Бердвотчинг можно совместить с экскурсией на орнитологическую станцию «Фрингилла», где посетителям расскажут об изучении птиц, покажут, как происходит кольцевание и учет пернатых.


Измени seeder чтобы создать объект "Национальный парк «Куршская коса»"