from django.http import HttpResponse

from gitrepos.src.dal import Dal


def index (request):
    dal = Dal()
    content = dal.test()
    return HttpResponse(content)