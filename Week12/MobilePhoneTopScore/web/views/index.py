from django.shortcuts import render
from django.http import HttpResponse
from web.models import Comment

#前台首页
def index(request):
    return HttpResponse('欢迎进入商城网站前台首页！')

def comment(request):

    lists = Comment.objects.all()

    product_list = []

    for item in lists:
        product_list.append(item.product_name)
    
    product_list = list(set(product_list))


    return render(request, 'web/show.html', locals())