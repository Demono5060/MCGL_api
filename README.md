# MCGL_api
Api для быстрого парсинга и работы с форумом и картой проекта https://minecraft-galaxy.ru/
<!-- 
## Установка
Для работы api потребуются библиотеки requests и beautifulsoup4
```
pip install requests
pip install beautifulsoup4
``` -->
## Использование
1. Склонировать репозиторий в папку с проектом `git clone https://github.com/Demono5060/MCGL_api.git`
2. Подключить к своему проекту основной класс MCGL
 ```python
 from mcgl import MCGL
 ```
3. Создать экземпляр класса (где взять `fcode` и `recap` описано в пункте `Данные для авторизации`) 
```python
 mcgl = MCGL('login', 'pass', 'fcode','recap')
```


## Данные для авторизации
Для авторизации используются 4 параметра:
* `login` - логин на форуме/в игре;
* `pass` - пароль на форуме;
* `fcode` и `recap` параметры генерируемые браузером, их мы получаем, авторизуясь на форуме и перехватывая запрос, направленый к странице login.php:
![fcode and recap](https://i.imgur.com/9me8YAG.png)
## Быстрый старт
```python
from mcgl import MCGL

mcgl = MCGL('login', 'pass', 'fcode','recap')
fortress_id = mcgl.forum.fortress.get_fortress_list()[1].get("fortress_url")[-4:]
log_url = mcgl.forum.fortress.get_fortress_logs_list(fortress_id)[0].get('url')
for i in mcgl.forum.fortress.get_fortress_log_capture(log_url):
    print(i)

```

# Основной класс
## MCGL
MCGL - является основным классом, который создает сессию, а так же инициализирует все остальные, дочерние классы.
Использование:
```python
 from mcgl import MCGL
 mcgl = MCGL('login', 'pass', 'fcode','recap')
```
# Классы коннекторы
## Forum, Map
Классы Forum и Map - являются классами коннекторами, основной задачей которых является разграничевать остальные классы, для более простого и понятного обращения к ним.

# Forum
Класс Forum имеет в себе на текущий момент 2  подкласса (разумеется в дальнейшем их станет больше)
Это классы `Fortress` и `Players`, обращение к ним осуществляется с помощью экземпляра класса форума `forum`

## Fortress
Fortress - класс, предназначеный для работы с логами крепостей, он имеет в себе (на текущий момент), следующие методы:
* `get_fortress_list(self)` - возвращает список крепостей, отображаемых на текущий момент на форуме.
* `get_fortress_logs_list(self, fortress_id)` - возвращает список доступных для просмотра логов. `fortress_id` - id крепости, можно получить из ссылки, возвращаемой предидущим методом.
* `get_fortress_log_pvp(self, log_url)` и `get_fortress_log_capture(self, log_url)` - возвращают логи со страниц, посвященным PVP и захватам. `log_url` - ссылка на лог в формате `/fortressbattlelog/**********`

## Players
Players - класс, предназначеный для работы с профилями игроков, методы:
* `get_user_by_id(self, user_id)` - возвращает информацию со странички пользователя с ID, указанным в `user_id`
* `get_user_by_nickname(self, nickname)` - возвращает информацию со странички пользователя, с указанным `nickname`, обратите внимание, что `nickname` должен быть таким же, как и nickname игрока на форуме, без учета регистра.
* `get_user_clan_by_id(self, user_id)` и `get_user_clan_by_nickname(self, nickname)` - возвращают информацию о клане игрока, чей ID или Nickname был передан в качестве аргумента.
