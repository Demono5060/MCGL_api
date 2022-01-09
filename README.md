# MCGL_api
Api для быстрого парсинга и работы с форумом и картой проекта https://minecraft-galaxy.ru/

## Установка
Для работы api потребуются библиотеки requests и beautifulsoup4
```
pip install requests
pip install beautifulsoup4
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

