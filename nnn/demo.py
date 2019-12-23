from django.http import HttpResponse


def index():
    print(123)
    return HttpResponse()
def demo(request):
    print("我是在demo新增的demo试图")
    return HttpResponse()