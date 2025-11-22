from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from auction.models import Item, User  # Import specific models explicitly
from datetime import date
today=date.today()
global_var = None # Initialize it with a default value
# Function to set the global variable to a dynamic value
def set_global_variable(value):
    global global_var
    global_var = value
# Function to access the global variable
def access_global_variable():
    return global_var
def maxbid(id):
    li=[]
    global maximum
    item = Item.objects.get(id=id)
    print("item id-->", item.id)
    user = User.objects.all().values()
    # item = Item.objects.all().values()
    for i in user:
        a = i['bid_amt']
        print("-->", a)
        li.append(a)
        maximum = max(li)
    print(li)
    print("maximum", maximum)
    item.max_bid = maximum
    item.save()
    print("Item Saved")
    return maximum
        # print(a)
        # li.append(i)
        # print(&quot;list--&gt;&quot;,li)
        # print(max(li))
        # return a
def bid(request):
    item = Item.objects.all()
    # user = User.objects.all()
    maxbid()
    # print(item.item_name.values)
    return render(request, 'base.html', {"item": item})
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        item = Item.objects.all()
        try:
            user = User.objects.get(email=email)
            print("userpass-->", user.password)
            if user is not None:
                if password == user.password:
                    global mailid
                    # print(&quot;Mail id here---&gt;&quot;,item.item_status)
                    set_global_variable(email)
                    mailid = email
                    mail= email
                    # print(&quot;Ye rhi dates--&gt;&quot;,item.start_date)
                    # print(&quot;ye print ho gyi---&gt;&quot;,mailid)
                    # print(&quot;outer funciton global ---&gt;&quot;,mail)
                    return render(request, 'base.html', {"item": item, "mailid": mailid})
                else:
                    print("Wrong pass")
                    return HttpResponse("Wrong Password")
        except:
            return HttpResponse("email id Not exist")
            print("email id Not exist")
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        email = request.POST['email']
        print(email)
        phone = request.POST['phone']
        print(phone)
        password = request.POST['password']
        print(password)
        user = User.objects.all().values()
        for i in user:
            flag=0
            dataemail = i['email']
            if dataemail == email:
                flag=1
                return HttpResponse("Email id Already Exist")
        if flag!=1:
            new=User.objects.create(name=name,email=email,phone=phone,password=password )
            new.save()
            print(f"User Create with email {email}")
            return HttpResponse(f"User Created Successfully with email {email}")
    return render(request,'register.html')
def applybid(request,id):
    mail = access_global_variable()
    print("Yaha pe ye mail ai h applybid mei --&gt;", mail)
    item = Item.objects.get(id=id)
    user = User.objects.get(email=mail)
    print("user---&gt;", user.email)
    # for i in user:
    #     # print(&quot;i--&gt;&quot;,i)
    #     if i.email == mail:
    #         print(&quot;mail id--&gt;&quot;,i.email)
    if request.method == "POST":
        maximum=request.POST['max_bid']
        item.max_bid = maximum
        user.bid_amt = maximum
        print("user.status---&gt;", user.status)
        user.status = "Applied"
        print("user.status---&gt;", user.status)
        item.save()
        user.save()
        print("Hogya save")
        maxbid(id)       
        return redirect('/')
    return render(request, 'applybid.html', {"item": item, "user": user})
def home(request):
    item = Item.objects.all()
    return render(request, 'home.html', {"item": item})
