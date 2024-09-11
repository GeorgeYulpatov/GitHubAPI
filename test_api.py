import os
import requests
import logging
import time
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')

GITHUB_API_URL = "https://api.github.com/user/repos"


def create_repository():
    """Создает новый публичный репозиторий на GitHub"""
    response = requests.post(
        GITHUB_API_URL,
        json={"name": REPO_NAME, "private": False},
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    if response.status_code == 201:
        logging.info("Репозиторий успешно создан.")
        return True
    else:
        logging.error(f"Ошибка при создании репозитория: {response.status_code} - {response.json().get('message')}")
        return False


def check_repository_exists():
    """Проверяет наличие репозитория"""
    response = requests.get(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    if response.status_code == 200:
        logging.info("Репозиторий существует.")
        return True
    elif response.status_code == 404:
        logging.warning("Репозиторий не найден.")
        return False
    else:
        logging.error(f"Ошибка при проверке репозитория: {response.status_code} - {response.json().get('message')}")
        return False


def delete_repository():
    """Удаляет репозиторий"""
    response = requests.delete(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",
        auth=(GITHUB_USERNAME, GITHUB_TOKEN)
    )
    if response.status_code == 204:
        logging.info("Репозиторий успешно удален.")
        return True
    else:
        logging.error(f"Ошибка при удалении репозитория: {response.status_code} - {response.json().get('message')}")
        return False


def main():
    # Создание репозитория
    logging.info("Создание репозитория...")
    if create_repository():
        time.sleep(2)

        # Проверка существования репозитория
        logging.info("Проверка существования репозитория...")
        if check_repository_exists():
            time.sleep(2)

            # Удаление репозитория
            logging.info("Удаление репозитория...")
            delete_repository()


if __name__ == "__main__":
    main()
