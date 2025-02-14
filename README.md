# Шаблон бота на Aiogram + Mysql
## Структура проекта
```
aiogram_template
├── data
│  └── config.py # Основной конфиг
├── handlers # Папка с обработчиками
│  ├── errors # Обработчики ошибок
│  │  └── error_handler.py
│  ├── groups # Обработчики групп
│  └── users # Обработчики пользователей
│    ├── admin.py
│    ├── help.py
│    ├── start.py
│    └── __init__.py # Здесь инициализируются обработчики
├── keyboards # Клавиатуры
│  ├── inline
│  │  ├── __init__.py
│  │  └── buttons.py
│  └── reply
├── middlewares
│  ├── __init__.py
│  └── throttling.py
├── states # Состояния
│  ├── admin.py
│  └── users.py
└── utils # Здесь дополнительные функции
  ├── db
  │  └── mysql.py # Класс базы данных
  ├── set_bot_commands.py # Список команд внутри тг
  ├── app.py # Основной код для запуска
  └── loader.py # Здесь инициализируется база данных и основные переменные
```

## Установка
### Linux
```
git clone https://github.com/mart4err/aiogram_template.git
cd aiogram_template
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### Windows
```
git clone https://github.com/mart4err/aiogram_template.git
cd aiogram_template
pip install -r requirements.txt
```
