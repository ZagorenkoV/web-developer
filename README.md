# Новостной сайт с прогнозом погоды

Новостной сайт с прогнозом погоды в Москве.

### Используемый стек технологий

* Python
* Flask
* SQLAlchemy
* Celery
* Redis
* BS4

### Функционал проекта

- парсит новости с сайта Habr и показывает на своей странице
- показывает погоду в Москве. Для прогноза использовался API из World Weather Online. 
- реализовано две админки, для обычного пользователя и admin
- можно оставлять комментарии под новостями
- в Celery можно выставить подходящий тайминг для обновления новостей на сайте. 

### Установка
1. Клонируйте репозиторий с GitHub
2. Создайте виртуальное окружение
3. Установите зависимости `pip install -r requirements.txt`
4. Для установки и работы с Redis используйте Linux. Если у вас MacOS используйте - homebrew (инструкция). Если Windows - используйте Windows-подсистему для Linus (WSL)

### Запуск проекта
* Для запуска проекта войдите в виртуальное окружение.
* В командной строке или треминале интерпретатора запустите файл `run.bat`
* P.S Не забудьте перед этим добавить файл `config.py` в корень проекта, и добавить в него значения Weather_API_KEY, Weather_URL, а также запустить парсинг новостей.