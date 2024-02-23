<b>Codefiner</b>

Запуск HTTP-сервера:
<b>python -m src.main start-api</b>

<i>Method</i>: POST

<i>Path</i>: /api/get_language

<i>Request Body</i>: { "link": "https://gitlab.com/<file_path>" }

<i>Response Body</i>: { "language": "python", "languages": { "python": 0.98, "java": 0.30, "javascript": 0.15 } }

Команда: <b>python -m src.main get-language-for-local FILEPATH</b> выводит язык программирования для файла.

Arguments: FILEPATH  [required]
 
