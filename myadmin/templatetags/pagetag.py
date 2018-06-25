from django import template
from django.utils.html import format_html

register = template.Library()

 
# 自定义过滤器
@register.simple_tag
def PageShow(count,request):
    p = int(request.GET.get('p',1))

    a = p-2
    b = p+3

    if p < 3:
        a = 1 
        b = 6

    if p > count -3:
        a = count - 5
        b = count

    if a <= 0:
        a = 1

    u = ''
    for x in request.GET:
    # 排除p参数
        if x != 'p':
            u+= '&'+x+'='+request.GET[x]

    s = ''
    s += '<li><a href="?p=1'+u+'">首页</a></li>'
    if p - 1 <=0:
        s += '<li class="am-disabled"><a href="?p=1'+u+'">上一页</a></li>'
    else:
        s += '<li><a href="?p='+str(p-1)+u+'">上一页</a></li>'

    for i in range(a,b+1):
        if p == i:
            s += '<li class="am-active"><a href="?p='+str(i)+u+'">'+str(i)+'</a></li>'
        else :
            s += '<li><a href="?p='+str(i)+u+'">'+str(i)+'</a></li>'

    if p +1 >= b:
        s += '<li class="am-disabled"><a href="?p='+str(count)+u+'">下一页</a></li>'
    else:
        s += '<li><a href="?p='+str(p+1)+u+'">下一页</a></li>'

    s += '<li><a href="?p='+str(count)+u+'">尾页</a></li>'


    return format_html(s)
