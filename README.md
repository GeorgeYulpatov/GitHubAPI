# GitHub API Test
## Описание

Этот проект содержит автоматический тест для работы с GitHub API на языке Python. Тест проверяет создание, наличие и удаление репозитория на GitHub.

## Требования

- Python 3.x

## Установка и использование

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/GeorgeYulpatov/GitHubAPI.git
   cd GitHubAPI
2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # для Windows
    source venv/bin/activate  # для Linux / macOS
   
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt

4. Для дальнейшего использования требуется присвоить собственные значения переменным(в файле .env):  
  - GITHUB_USERNAME
  - GITHUB_TOKEN
  - REPO_NAME  

5. Запуск:  

    ```bash
    python test_api.py

## Логирование  
Логирование настроено с помощью модуля ```logging```. Отображение в консоль с указанием времени и уровня логирования.

## Лицензия  
Этот проект лицензирован под лицензией MIT.
