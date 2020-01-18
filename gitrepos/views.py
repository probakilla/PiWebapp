from django.http import HttpResponse
from django.template import loader

from gitrepos.src.dal import get_repo_list


def index(request):
    content = get_repo_list()
    template = loader.get_template('gitrepos/index.html')
    context = {
        'repos_list': content
    }
    return HttpResponse(template.render(context, request))
