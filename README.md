<h1> Решение тестового задания "Сервис управления картами" </h1>

## Тестовое задание:

### Необходимо создать веб-приложение для управления базой данных бонусных карт.

### Список полей: серия карты, номер карты, дата выпуска карты, дата окончания активности карты, дата использования, сумма, статус карты (не активирована/активирована/просрочена).

### Функционал приложения:

```
1.список карт с полями: серия, номер, дата выпуска, дата окончания активности, статус
2.поиск по этим же полям
3.просмотр профиля карты с историей покупок по ней
4.активация/деактивация карты
5.удаление карты
```

### Реализовать генератор карт, с указанием серии и количества генерируемых карт, а также "срок окончания активности" со значениями "1 год", "6 месяцев" "1 месяц". После истечения срока активности карты, у карты проставляется статус "просрочена".

## Детали реализации:

### Реализован API проекта c помощью DRF. Документация (swagger) доступна по адрусу http://127.0.0.1:8000/docs/.

### Задача управления картами (активация/деактивация, просмотр статистики, удаление) реализована с помощью связки DRF + JS. Отображение карт осуществляется в табличном виде в DataTables.

### Генератор карт реализован в файле application/cards/management/commands/cards_gen.py

### Проверка на истечение срока действия производится на уровне JS в браузере. При истечении срока статус карты меняется на expired и поле статуса закрашивается в карсный цвет.

# Как установить проект

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AKafer/Test-rask-CARDS.git
cd Test-task-CARDS
```

### Создать и активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
cd application
python manage.py migrate
```

### Переопределеить при необходимости константы в файле cards_gen.py и выпустить необходимое число карт:

```
python manage.py cards_gen
```

### Запустить проект:

```
python manage.py runserver
```

### Перейти на главную страницу http://127.0.0.1:8000.

## Стек технологий: Python 3, Django 4.1, DRF, JS, jQuery, DataTables

## Автор проекта - Сергей Сторожук
