import requests

def info():
    return "AdrianDevProjects Online Services Python SDK Authentication Module v1.0.2 by Adrian Albrecht"


def login(username, password, return_mode):
    url = "https://onlineservices.adriandevprojects.com/v1/auth/login/"

    credentials = {
        "username": username,
        "password": password
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=credentials, headers=headers)

    if return_mode in ("content+code", "code+content"):
        return f"{response.status_code}\n{response.text}"
    elif return_mode == "content":
        return response.text
    elif return_mode == "code":
        return response.status_code
    else:
        return "Invalid return configuration in request"
