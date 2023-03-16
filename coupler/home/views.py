from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Social,Post,Blog, Preference1,Preference2,Signup, Detail ,Detaila

# Create your views here.

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        global val
        def val():
            return username

        if Signup.objects.filter(username=username,email=email):
            messages.error(request,"User already exist")
            return render(request,"signup.html")

        #messages.success(request,"Your account has created successfully")
        myprofile=Signup(username=username,email=email,password=password)
        myprofile.save()
        messages.success(request,"Your account has created successfully")
        
        return render(request,"details.html")
    
    return render(request,"signup.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        credential=Signup.objects.all()
        flag=0
        for i in credential:
            if i.username==username and i.password==password:
                flag=1
                global val
                def val():
                    return username
                return render(request,"dashboard.html")
        if flag==0:
            messages.error(request,"Bad Credentials")
            return redirect('home')

    return render(request,"login.html")

def signout(request):
    messages.success(request,"Logged Out successfully!")
    return redirect('home')

def dashboard(request):
    return redirect(request, 'dashboard.html')

def detail(request):
    if request.method=="POST":
        fullname=request.POST['fullname']
        email=request.POST['email']
        dob=request.POST['dob']
        mobno=request.POST['mobno']
        role=request.POST['role']
        weight=request.POST['weight']
        height=request.POST['height']
        address=request.POST['address']
        addtype=request.POST['addtype']
        idtype=request.POST['idtype']
        idno=request.POST['idno']
        job=request.POST['job']
        if len(request.FILES) !=0:
            image=request.FILES['image']

        username=val()

        #messages.success(request,"Your account has created successfully")
        det=Detail(username=username,fullname=fullname,email=email,dob=dob,mobno=mobno,role=role,weight=weight,height=height,address=address,addtype=addtype,idtype=idtype,idno=idno,job=job,image=image)
        det.save()
        messages.success(request,"Details added successfully")
        return render(request,"details1.html")
        

    return render(request, "details.html")


def detaila(request):
    if request.method=="POST":
        describeu=request.POST['describeu']
        age=request.POST['age']
        qualification=request.POST['qualification']
        education=request.POST['education']
        professionalexp=request.POST['professionalexp']
        mothertongue=request.POST['mothertongue']
        describeurfamily=request.POST['describeurfamily']
        familytype=request.POST['familytype']
        familyvalue=request.POST['familyvalue']
        familystatus=request.POST['familystatus']
        maritalstatus=request.POST['maritalstatus']
        hobbiesandinterest=request.POST['hobbiesandinterest']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']

        username=val()

        #messages.success(request,"Your account has created successfully")
        deta=Detaila(username=username,describeu=describeu,age=age,qualification=qualification,education=education,professionalexp=professionalexp,mothertongue=mothertongue,describeurfamily=describeurfamily,familytype=familytype,familyvalue=familyvalue,familystatus=familystatus,maritalstatus=maritalstatus,hobbiesandinterest=hobbiesandinterest,country=country,state=state,city=city)
        deta.save()
        messages.success(request,"Details added successfully")
        return render(request,"preference1.html")
        

    return render(request,'details1.html')

def preference1(request):
    if request.method=="POST":
        personallyf=request.POST['personallyf']
        adoptchild=request.POST['adoptchild']
        lifewithdiv=request.POST['lifewithdiv']
        ambitious=request.POST['ambitious']
        superstitious=request.POST['superstitious']
    
        username=val()

        #messages.success(request,"Your account has created successfully")
        pref1=Preference1(username=username,personallyf=personallyf,adoptchild=adoptchild,lifewithdiv=lifewithdiv,ambitious=ambitious,superstitious=superstitious)
        pref1.save()
        messages.success(request,"Details added successfully")
        return render(request,"preference2.html")
        

    return render(request, "preference1.html")

def preference2(request):
    if request.method=="POST":
        socialcom=request.POST['socialcom']
        partnertalent=request.POST['partnertalent']
        partnerindep=request.POST['partnerindep']
        drinkorsmoke=request.POST['drinkorsmoke']
        hangout=request.POST['hangout']
    
        username=val()
        #messages.success(request,"Your account has created successfully")
        pref2=Preference2(username=username,socialcom=socialcom,partnertalent=partnertalent,partnerindep=partnerindep,drinkorsmoke=drinkorsmoke,hangout=hangout)
        pref2.save()
        messages.success(request,"Details added successfully")
        return render(request,"dashboard.html")
        

    return render(request, "preference2.html")


def blog(request):
    return render(request,'blog.html')

def blogcontact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phno=request.POST['phno']
        message=request.POST['message']

        username=val()
        blogdet=Blog(usrname=username,name=name,email=email,phno=phno,message=message)
        blogdet.save()
        messages.success(request,"Query sent successfully")
        return render(request,'/blog')
    return render(request,'blog_contact.html')

def blogpost(request):
    if request.method=="POST":
        posts=request.POST['posts']

        user=val()

        postdet=Post(username=user,posts=posts)
        postdet.save()
    return render(request,'blog_post.html')


def blogabout(request):
    return render(request,'blog_about.html')


def social(request):
    if request.method=="POST":
        instagram=request.POST['instagram']
        fb=request.POST['fb']
        twitter=request.POST['twitter']

        users=val()

        socials=Social(username=users,instagram=instagram,fb=fb,twitter=twitter)
        socials.save()
    messages.success(request,"Details added successfully")   
    return render(request,'social.html')

def profile_list(request):
    profiles = Detail.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})

def match_list(request, username):
    profilee=Detail.objects.get(username)
    matches = sorted(Detail.objects.exclude(username=username), key=lambda p: profilee.compatibility_score(p), reverse=True)
    return render(request, 'match_list.html', {'profilee': profilee, 'matches': matches})