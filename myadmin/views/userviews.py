from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
# Create your views here.
from .. models import Users
import os

def add(request):
    if request.method == 'GET':
        # show add 
        return render(request,'myadmin/users/add.html')
    else:
        # 接收表单提交的数据 且转为字典格式
        data = request.POST.copy().dict()
        del data['csrfmiddlewaretoken']

        # 进行密码加密
        from django.contrib.auth.hashers import make_password, check_password
        data['password'] = make_password(data['password'],None,'pbkdf2_sha256')


        # 上传头像
        try:
            if request.FILES.get('pic',None):
                data['pic'] = uploads(request)
                print(data['pic'])
                if data['pic'] ==  1:
                    return HttpResponse('<script>alert("上传的文件类型不符合要求");location.href="'+reverse('useradd')+'"</script>')
            else:
                del data['pic'] 

            # print(data)
            ob = Users.objects.create(**data)
        # print(ob)
        # return HttpResponse('aa')
            return HttpResponse('<script>alert("添加成功");location.href="'+reverse('userlists')+'"</script>')
        except:
            return HttpResponse('<script>alert("添加失败");location.href="'+reverse('useradd')+'"</script>')


# 列表
def lists(request):

    # 获取搜索条件,通过lists.html获取类别name
    types = request.GET.get('type',None)
    keywords = request.GET.get('keywords',None)
    print(types)
    print(keywords)
    if types:
    # 判断是否有搜索条件
        if types == 'all':
            
            # 全局搜索
            from django.db.models import Q
            userlist = Users.objects.filter(
                Q(username__contains=keywords)|
                Q(name__contains=keywords)|
                Q(phone__contains=keywords)|
                Q(email__contains=keywords)|
                Q(sex__contains=keywords)
                )
        elif types=='username':
            userlist = Users.objects.filter(username__contains=keywords)

        elif types == 'name':
            userlist = Users.objects.filter(name__contains=keywords)
        elif types == 'phone':
            userlist = Users.objects.filter(phone__contains=keywords)
        elif types == 'email':
            userlist = Users.objects.filter(email__contains=keywords)
        print(userlist)

    else:
        userlist = Users.objects.filter()

# 任务 给所有标签添加排序 
    # 导入分页类
    from django.core.paginator import Paginator
    # 实例化分类对象,参数1 数据集合,参数2 显示条数

    paginator = Paginator(userlist,10)

    p = request.GET.get('p',1) 

    userlists = paginator.page(p)

    print(paginator.page(p))


    
    # userlist = Users.objects.all()[:10]
    context = {'userlist':userlists}
    
    return render(request,'myadmin/users/lists.html',context)

# 删除
def delete(request):
    try:
        # 获取id号
        uid = request.GET.get('uid',None)
        # 通过id获取数据
        ob = Users.objects.get(id=uid)
        # print(ob)
        # 检查头像是否存在,存在则删除
        if ob.pic:
            os.remove('.'+ob.pic)
            print('111')
        # 执行删除
        ob.delete()
        data = {'msg':'删除成功','code':0}
    except:
        data = {'msg':'删除失败','code':1}
        
    return JsonResponse(data)


# 会员修改和编辑
def edit(request):
    # 接收id
    uid = request.GET.get('uid',None)
    print(uid)
    # 通过id获取对象
    ob = Users.objects.get(id=uid)
    if request.method == 'GET':
       
        # 分配数据
        context = {'uinfo':ob}
        # 显示编辑页面
        return render(request,'myadmin/users/edit.html',context)

    elif request.method == 'POST':
        try:
            # 判断是否上传了新的图片
            if request.FILES.get('pic',None):
                # 判断是否使用的默认图
                if ob.pic:
                    # 如果使用的不是默认图,则删除之前上传的头像
                    os.remove('.'+ob.pic)

                # 执行上传
                ob.pic = uploads(request)
                

            ob.username = request.POST['username']
            ob.email = request.POST['email']
            ob.age = request.POST['age']
            ob.sex = request.POST['sex']
            ob.phone = request.POST['phone']
            ob.save()

            return HttpResponse('<script>alert("更新成功");location.href="'+reverse('userlists')+'"</script>')
        except:
            return HttpResponse('<script>alert("更新失败");location.href="'+reverse('useredit')+'?uid='+str(ob.id)+'"</script>')




def uploads(request):
    # 获取请求中的文件
    myfile = request.FILES.get('pic',None)
    # 获取上传文件的后缀名 myfile.name.spilt('.').pop()
    p = myfile.name.split('.').pop()
    # print(p)
    arr = ['jpg','jpg','jpeg','gif']
    if p not in arr:
        return 1
    import time,random
    # 生成新文件名
    filename = str(time.time()) + str (random.randint(1,999))+'.'+p
    # 打开文件
    openfile = open('./static/pics/'+filename,'wb+')

    # 分块写入文件
    for i in myfile.chunks():
        openfile.write(i)

    # 关闭文件
    openfile.close()

    return '/static/pics/'+filename
