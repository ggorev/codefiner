import base64

import requests

from src.service.exceptions import InvalidGitlabLinkException


def encode_url_path(path: str):
    return path.replace('/', '%2F')


def get_url_for_request(link: str):
    if link.startswith("https://gitlab.com"):
        split_link = link.split('/-/blob/')
        username = split_link[0].split('/')[3]
        project_name = split_link[0].split('/')[4]
        branch_name = split_link[1].split('/')[0]
        file_path = split_link[1].split('?ref_type')[0].split('/', maxsplit=1)[1]
    else:
        raise InvalidGitlabLinkException
    return f"https://gitlab.com/api/v4/projects/{username}%2F{project_name}/repository/files/{encode_url_path(file_path)}?ref={branch_name}"


def get_text_from_repository(link: str, token: str = None):
    if token:
        headers = {"PRIVATE-TOKEN": token}
        request = requests.get(get_url_for_request(link), headers=headers)
    else:
        request = requests.get(get_url_for_request(link))
    decoded_data = base64.b64decode(request.json()["content"])
    text_content = decoded_data.decode('utf-8')
    return text_content


def get_file_from_repository(link: str, token: str = None, output: str = "downloads/gitlab-file.txt"):
    try:
        text = get_text_from_repository(link, token)
        with open(output, 'w+', encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print("Error:", e)
