# News site with weather forecast

### Technology stack

* Python
* Flask
* SQLAlchemy
* Celery
* Redis
* BS4

### Project Functionality

- Parses news from Habr site and displays it on its page
- It shows the weather in Moscow. For the forecast API from World Weather Online was used.
- There are two admin sections, for standard user and admin
- news comments are include
- It is possible to set a suitable timing for news updates on the site.


### Installation
1. Clone the repository from GitHub
2. Create a virtual environment
3. Install the pip install -r requirements.txt dependencies
4. Use Linux to install and work with Redis. If you use MacOS use - [*homebrew*](https://brew.sh/index_ru) ([*инструкция*](https://medium.com/@djamaldg/install-use-redis-on-macos-sierra-432ab426640e)). For Windows - [*Windows-подсистему для Linus (WSL)*](https://www.comss.ru/page.php?id=4897)

### Starting the project
* To start your project, enter /env.
* At the command console or IDLE start `run.bat`
* P.S Don't forget to add the config.py file to the project root, and add Weather_API_KEY, Weather_URL values to it, and run news parsing before that.

# Новостной сайт с прогнозом погоды

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
4. Для установки и работы с Redis используйте Linux. Если у вас MacOS используйте - [*homebrew*](https://brew.sh/index_ru) ([*инструкция*](https://medium.com/@djamaldg/install-use-redis-on-macos-sierra-432ab426640e)). Если Windows - используйте [*Windows-подсистему для Linus (WSL)*](https://www.comss.ru/page.php?id=4897)

### Запуск проекта
* Для запуска проекта войдите в виртуальное окружение.
* В командной строке или треминале интерпретатора запустите файл `run.bat`
* P.S Не забудьте перед этим добавить файл `config.py` в корень проекта, и добавить в него значения Weather_API_KEY, Weather_URL, а также запустить парсинг новостей.
