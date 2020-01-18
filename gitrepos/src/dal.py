import requests
from django.conf import settings

from .git_repo import GitRepo


def get_repo_list():
    response = requests.get(settings.GIT_REPOS_URL)
    return json_parser(response.json())


def json_parser(response):
    repos_list = list()
    for obj in response:
        repos_list.append(create_gitrepo(obj))
    print(repos_list)
    return repos_list


def create_gitrepo(json_object):
    repo_name = json_object["name"]
    repo_http = json_object["clone_url"]
    repo_ssh = json_object["ssh_url"]
    return GitRepo(repo_name, repo_http, repo_ssh)
