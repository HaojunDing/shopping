from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import Types


def gettypesorder(): 
    # 获取所有分类信息
    # select *,concat(path,id) as paths from myadmin_types order by paths;
    # 拼接 路径和id 按照拼接后的结果进行排序

    tlist = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')

    for i in tlist: 
        if i.pid == 0 :
            i.pname = '顶级分类'
        else :
            t = Types.objects.get(id=i.pid)
            i.pname = t.name
        num = i.path.count(',') - 1 
        i.name = (num*'|----') + i.name
    return tlist

def add(request):
    if request.method == 'GET':
        # 如果 以get方式请求数据,那么 就返回一个添加的页面

        tlist = gettypesorder()

        context = {'tlist':tlist}

        return render(request,'myadmin/types/add.html',context)

    elif request.method =='POST':

        # 执行分类的添加
        ob = Types()
        ob.name = request.POST['name']
        ob.pid = request.POST['pid']
        if ob.pid == 0:
            ob.path = '0,'  
            print(ob.path)
        else:
            # 根据当前父级id获取path,在添加当前父级id
            t = Types.objects.get(id=ob.pid)
            ob.path = t.path+str(ob.pid)+','
        ob.save()
        return HttpResponse('<script>alert("添加成功");location.href = "'+reverse('typesadd')+'"</script>')

def lists(request):
    tlist = gettypesorder()

    context = {'tlist':tlist}

    return render(request,'myadmin/types/lists.html',context)


def delete():
    tid = request.GET.get('uid',None)

    # 判断当前类下是否子类
    num = Types.objects.filter(pid=tid).count()

    if num != 0:
         data = {'msg':'当前类下有子类,不能删除','code':1}
    else:
        # 判断当前类下是否商品,
        ob = Types.objects.get(id=tid)
        ob.delete()

        data = {'msg':'删除成功','code':0}

def edit():
    pass