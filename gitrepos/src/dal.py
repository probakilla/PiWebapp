from django.conf import settings

import requests

class Dal(object):

    def test(self):
        r = requests.get(settings.GIT_REPOS_URL)
        return r.content