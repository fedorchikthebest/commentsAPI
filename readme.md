<h1>Использование API</h1>
<a name="Создание своего id"><h2>Создание своего id</h2></a>
Для создания своего id вам нужно сгенерировать набор чисел и отправить <br>
get запрос по адресу http://92.51.38.221:5000/api/"ваш набор чисел".<br>
Если вы получили json в виде пустого массива("[]"), то вы можете спокойно занять этот id.
<a name="Получение комментариев"><h2>Получение комментариев</h2></a>
Все просто, вам нужно отправить get запрос на по адресу http://92.51.38.221:5000/api/"ваш набор чисел".
В ответ вы получите json формата: "[{"name": "comment"}, {"name": "comment"}]"
<a name="Написание комментариев"><h2>Написание комментариев</h2></a>
Для написания комментария вам нужно: перейти по ссылке http://92.51.38.221:5000/add_comment/"ваш набор чисел" и оставить
ваш комментарий.