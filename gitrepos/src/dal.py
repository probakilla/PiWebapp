from django.conf import settings

import requests

class Dal(object):

    def get_repo_list(self):
        r = requests.get(settings.GIT_REPOS_URL)
        return r.content