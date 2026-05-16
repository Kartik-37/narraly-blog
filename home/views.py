from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.urls import reverse
from django.db.models import Max,Sum,Count
from .models import Profile,View,Member,Pyment,Blogwrite,Comment,Save,Follow,Like,Contect

def index(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        posts = Blogwrite.objects.filter(author=cprofile).order_by('-created_at')
        
        for j in posts:
            word_count = len(j.content.split())  # Adjust field name if needed
            j.read_time = round(word_count / 200) or 1 
        
        context={
                    'data':data,
                    'data1':data1,
                    'posts':posts,
                }   
        return render (request,'../templates/index.html',context)
    else:
         return render (request,'../templates/home.html')
    
def serindex(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        posts = Blogwrite.objects.filter(author=cprofile).order_by('-created_at')
        
        for j in posts:
            word_count = len(j.content.split())  # Adjust field name if needed
            j.read_time = round(word_count / 200) or 1 

        query = request.GET.get('q', '')
        results = [] 
        if query:
            results = Blogwrite.objects.filter(Q(author=cprofile) & (Q(title__icontains=query) | Q(content__icontains=query))).order_by('-created_at')
        else:
            results = []
        
        context={
                    'data':data,
                    'data1':data1,
                    'posts':posts,
                    'results':results,
                }   
        return render (request,'../templates/serindex.html',context)
    else:
         return render (request,'../templates/home.html')
    
def firstpage(request):
    return render (request,'../templates/home.html')

def community(request):

    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        posts = Blogwrite.objects.select_related('author').all().order_by('-created_at')
        bwid = None  
        susername = None
        for j in posts:
            bwid=j.bwid
            susername=j.author.username
                       

        for j in posts:
            j.is_saved = Save.objects.filter(susername=cprofile, bwid=j).exists()
            

        data5 = Save.objects.filter(susername=cprofile) 
        sbwids = [i.bwid for i in data5] 
        data6 = Blogwrite.objects.filter(bwid__in=[b.bwid for b in sbwids])
        save = []
        for k in data6:
            save_profile = Profile.objects.filter(username=susername).first()
            if save_profile:
                save.append({
                    'bwid':k.bwid,
                    'title': k.title,
                    'date': k.created_at,
                    'name': k.author.name,
                    'uid': k.author.uid,
                    'username': k.author.username,
                    'image': k.author.image,
                })
        follow=Follow.objects.filter(follower=cprofile)

       
      
        context={
                'bwid':bwid,
                'data':data,
                'data1':data1,
                'data2':posts,
                'save':save,
                'follow':follow,
            }
        
        return render (request,'../templates/community.html',context)
    else:
        return redirect('register')

def sercomm(request):

    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        posts = Blogwrite.objects.select_related('author').all().order_by('-created_at')
        bwid = None  
        query = None  
        susername = None
        for j in posts:
            bwid=j.bwid
            susername=j.author.username
                       

        for u in posts:
            is_saved = Save.objects.filter(susername=cprofile, bwid=j).exists()
            

        data5 = Save.objects.filter(susername=cprofile) 
        sbwids = [i.bwid for i in data5] 
        data6 = Blogwrite.objects.filter(bwid__in=[b.bwid for b in sbwids])
        save = []
        for k in data6:
            save_profile = Profile.objects.filter(username=susername).first()
            if save_profile:
                save.append({
                    'bwid':k.bwid,
                    'title': k.title,
                    'date': k.created_at,
                    'name': k.author.name,
                    'uid': k.author.uid,
                    'username': k.author.username,
                    'image': k.author.image,
                })
        follow=Follow.objects.filter(follower=cprofile)

        query = request.GET.get('q', '')
        results = [] 
        if query:
            results = Blogwrite.objects.filter( Q(title__icontains=query) | Q(content__icontains=query)| Q(author__username__icontains=query) | Q(author__name__icontains=query)).order_by('-created_at')  
        else:
            results = []
        context={
                'bwid':bwid,
                'data':data,
                'data1':data1,
                'data2':posts,
                'save':save,
                'follow':follow,
                'query': query,
                'results': results,
                'is_saved': is_saved,
            }
        if request.method == "POST":
            qquery = request.POST.get('query', '')
            sercomm = request.POST.get('sercomm')
            sercommf = request.POST.get('sercommf')
            if sercomm == 'sercomm':
                return redirect(f"{reverse('sercomm')}?q={qquery}")
            if sercommf == 'sercommf':
                return redirect(f"{reverse('sercommf')}?q={qquery}")  
        else:  
            return render (request,'../templates/sercomm.html',context)
    else:
        return redirect('register')

def commfoll(request):

    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)

        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        follow=Follow.objects.filter(follower=cprofile)
        
        posts = []
        fprofile = None
        bwid = None
       
        susername = None
        if follow.exists():
            for i in follow:
                folluser=i.following.username
            
            fprofile = get_object_or_404(Profile, username=folluser)
            if follow.exists():
                followed_users = [i.following for i in follow]
                posts = Blogwrite.objects.filter(author__in=followed_users).order_by('-created_at')

                for j in posts:
                    bwid = j.bwid
                    susername = j.author.username
        
                       

        for j in posts:
            j.is_saved = Save.objects.filter(susername=cprofile, bwid=j).exists()
            

        data5 = Save.objects.filter(susername=cprofile) 
        sbwids = [i.bwid for i in data5] 
        data6 = Blogwrite.objects.filter(bwid__in=[b.bwid for b in sbwids])
        for j in data6:
                ssusername=j.author.username
        save = []
        for k in data6:
            save_profile = Profile.objects.filter(username=ssusername).first()
            if save_profile:
                save.append({
                    'bwid':k.bwid,
                    'title': k.title,
                    'date': k.created_at,
                    'name': k.author.name,
                    'uid': k.author.uid,
                    'username': k.author.username,
                    'image': k.author.image,
                })
       
        
        context={
                'bwid':bwid,
                'data':data,
                'data1':data1,
                'data2':posts,
                'save':save,
                'follow':follow,
            }
        
        return render (request,'../templates/commfoll.html',context)
    else:
        return redirect('register')

def sercommf(request):

    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)

        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        follow=Follow.objects.filter(follower=cprofile)
        
        posts = []
        fprofile = None
        bwid = None
        query = None  
        susername = None
        if follow.exists():
            for i in follow:
                folluser=i.following.username
            
            fprofile = get_object_or_404(Profile, username=folluser)
            posts = Blogwrite.objects.filter(author=fprofile).order_by('-created_at')
            for j in posts:
                bwid=j.bwid
                susername=j.author.username
        
                       

        for j in posts:
            j.is_saved = Save.objects.filter(susername=cprofile, bwid=j).exists()
            

        data5 = Save.objects.filter(susername=cprofile) 
        sbwids = [i.bwid for i in data5] 
        data6 = Blogwrite.objects.filter(bwid__in=[b.bwid for b in sbwids])
        for j in data6:
                ssusername=j.author.username
        save = []
        for k in data6:
            save_profile = Profile.objects.filter(username=ssusername).first()
            if save_profile:
                save.append({
                    'bwid':k.bwid,
                    'title': k.title,
                    'date': k.created_at,
                    'name': k.author.name,
                    'uid': k.author.uid,
                    'username': k.author.username,
                    'image': k.author.image,
                })
       
        query = request.GET.get('q', '')
        results = [] 
        if query:
            results = Blogwrite.objects.filter(Q(author=fprofile) & (Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query) | Q(author__name__icontains=query))).order_by('-created_at')
        else:
            results = []
        context={
                'bwid':bwid,
                'data':data,
                'data1':data1,   
                'save':save,
                'follow':follow,
                'query': query,
                'results': results,
            }
        if request.method == "POST":
            qquery = request.POST.get('query', '')
            sercomm = request.POST.get('sercomm')
            sercommf = request.POST.get('sercommf')
            if sercomm == 'sercomm':
                return redirect(f"{reverse('sercomm')}?q={qquery}")
            if sercommf == 'sercommf':
                return redirect(f"{reverse('sercommf')}?q={qquery}")  
        else: 
            return render (request,'../templates/sercommf.html',context)
    else:
        return redirect('register')

def profile(request):
    if request.user.is_authenticated:
            username = request.user.username
            data = Profile.objects.filter(username=username)
            for i in data:
                uid=i.uid
            cprofile = get_object_or_404(Profile, uid=uid)
            data1=Member.objects.filter(username=username)
            blog=Blogwrite.objects.filter(author=uid).order_by('-created_at')
            duser = User.objects.get(username=username)
            join_date = duser.date_joined
            foprofile=Follow.objects.filter(following=cprofile)
            frprofile=Follow.objects.filter(follower=cprofile)
            if not data.exists():
                Profile.objects.create(username=username)
                data = Profile.objects.filter(username=username)
            context={
                'data':data,
                'data1':data1,
                'blog':blog,
                'join_date':join_date,
                'foprofile':foprofile,
                'frprofile':frprofile,
            }
            return render (request,'../templates/profileu.html',context)
    else:
         return redirect('home')
    
def pedit(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(username=username)
        data1 = Member.objects.filter(username=username)
        profile = data.first()
        if request.method == "POST":
            name = request.POST.get("name")
            image = request.FILES.get("profimg")
            email = request.POST.get("email")
            about = request.POST.get("about")
            twitter = request.POST.get("twitter")
            instagram = request.POST.get("instagram")
            github = request.POST.get("github")
            youtube = request.POST.get("youtube")

            if profile is None:
                profile = Profile(username=username)
            profile.name = name
            profile.email = email
            profile.profilbio = about
            profile.twitter = twitter
            profile.instagram = instagram
            profile.github = github
            profile.youtube = youtube
            if image:
                profile.image = image
            profile.save()
            return redirect('profile')
        else:
            context = {
                'data': data,
                'data1': data1,
            }
            return render(request, '../templates/pedit.html', context)
    else:
        return redirect('register')
    
def follow_toggle(request, uid):
    source = request.POST.get('source')
    hi = request.POST.get('hi')
    bi = request.POST.get('bi')
    current_profile = Profile.objects.get(username=request.user.username)
    target_user = get_object_or_404(Profile, pk=uid)

    follow_relation, created = Follow.objects.get_or_create(follower=current_profile, following=target_user)

    if not created:
        follow_relation.delete()  # unfollow
    if source == 'following':
            return redirect('ufollowing')
    if hi == 'hi':
            return redirect('followersi',uid)
    if bi == 'bi':
            return redirect('followingi',uid)
    return redirect('feedprofile',uid)

def feedprofile(request,uid):
    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(uid=uid)
        data2=Profile.objects.filter(username=username)
        cprofile = get_object_or_404(Profile, uid=uid)
        for i in data:
            dusername=i.username
        if dusername==username:
            return redirect('profile')
        else:
            data1=Member.objects.filter(username=username)
            blog=Blogwrite.objects.filter(author=uid).order_by('-created_at')
            for i in blog:
                uname=i.author.username
            duser = User.objects.get(username=uname)
            join_date = duser.date_joined
            user_profile = get_object_or_404(Profile, pk=uid)
            current_profile = Profile.objects.get(username=request.user.username)
            followers = Follow.objects.filter(following=current_profile).count()
            following = Follow.objects.filter(follower=current_profile).count()
            following_ids = Follow.objects.filter(follower=current_profile).values_list('following__uid', flat=True)
            foprofile=Follow.objects.filter(following=cprofile)
            frprofile=Follow.objects.filter(follower=cprofile)
            context={
                    'uid':uid,
                    'data':data,
                    'data1':data1,
                    'user_profile': user_profile,
                    'followers': followers,
                    'following': following,
                    'following_ids': following_ids,
                    'blog': blog,
                    'join_date': join_date,
                    'data2': data2,
                    'foprofile':foprofile,
                    'frprofile':frprofile,
                }
        return render (request,'../templates/feedprofile.html',context)
    else:
        return redirect('register')

def comment(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == "POST":
            comment= request.POST.get("comment")
            bwid=request.POST.get("bwid")
            blog_instance = Blogwrite.objects.get(pk=bwid)
            sql=Comment(cusername=username,comment=comment,bwid=blog_instance)
            sql.save()
    
    
            return redirect ('blog',bwid=bwid)
    return redirect('home') 

def blog(request,bwid):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
    # Blog post
        data2 = Blogwrite.objects.filter(pk=bwid)
        
        for j in data2:
            puser=j.author
            content=j.content
            bwusername = j.author.username
        word_count = len(content.split())  # Adjust field name if needed
        read_time = round(word_count / 200) or 1  # Avoid 0 min

        # Author info of blog
        data4 = Profile.objects.filter(username=bwusername)
        for i in data4:
            name = i.name
            image = i.image

        # Viewer profile info
        data = Profile.objects.filter(username=username)
        data1 = Member.objects.filter(username=username)

        # Fetch comments for this blog post only
        data3 = Comment.objects.filter(bwid=bwid).order_by('-cdate')
        comments = []
        for k in data3:
            commenter_profile = Profile.objects.filter(username=k.cusername).first()
            liked = Like.objects.filter(user=request.user, comment=k).exists()
            if commenter_profile:
                comments.append({
                    'cid':k.cid,
                    'comment': k.comment,
                    'date': k.cdate,
                    'name': commenter_profile.name,
                    'username': commenter_profile.username,
                    'image': commenter_profile.image,
                    'uid': commenter_profile.uid,
                    'liked': liked,
                })
        blog_instance = get_object_or_404(Blogwrite, bwid=bwid)
        blog_save=Blogwrite.objects.get(pk=bwid)
        liked_blog = Like.objects.filter(user=request.user, blog=blog_instance).exists()
        save = Save.objects.filter(susername=cprofile, bwid=blog_save).exists()

        comment_likes = {}
        for c in data3:
            comment_likes[c.cid] = Like.objects.filter(user=request.user, comment=c).exists()

        context = {
            'bwid': bwid,
            'name': name,
            'image': image,
            'data': data,
            'data1': data1,
            'data2': data2,
            'comments': comments,
            'read_time': read_time,
            'liked_blog': liked_blog,
            'comment_likes': comment_likes,
            'save': save,
        }
        return render (request,'../templates/blog.html',context)
    else:
        return redirect('register')
    
def like_blog(request, bwid):
    blog = get_object_or_404(Blogwrite, bwid=bwid)
    like, created = Like.objects.get_or_create(user=request.user, blog=blog)
    if not created:
        like.delete()  # toggle unlike
    return redirect('blog', bwid=bwid)

def like_comment(request, cid):
    comment = get_object_or_404(Comment, cid=cid)
    like, created = Like.objects.get_or_create(user=request.user, comment=comment)
    if not created:
        like.delete()
    return redirect('blog', bwid=comment.bwid.bwid)

def save(request, bwid):
        if not request.user.is_authenticated:
            return redirect('login')
        source = request.POST.get('source')
        commfoll = request.POST.get('commfoll')
        bookmark = request.POST.get('bookmark')
        sercomm = request.POST.get('sercomm')
        sercommf = request.POST.get('sercommf')
        bbwid = Blogwrite.objects.get(pk=bwid)
        current_user = request.user.username
        profile = get_object_or_404(Profile, username=current_user)
        save, created = Save.objects.get_or_create(susername=profile, bwid=bbwid)
        query = request.POST.get('query', '')
        if not created:
            save.delete()
        if source == 'community':
            return redirect('community')
        if bookmark == 'bookmark':
            return redirect('bookmark')
        if commfoll == 'commfoll':
            return redirect('commfoll')
        if sercomm == 'sercomm':
            return redirect(f"{reverse('sercomm')}?q={query}")
        if sercommf == 'sercommf':
            return redirect(f"{reverse('sercommf')}?q={query}")
        return redirect('blog', bwid=bwid)

def membership(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        context={
                    'data':data,
                    'data1':data1,
                }
        return render (request,'../templates/membership.html',context)
    else:
        return redirect('register')

def payment(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == "POST":
                cardno = request.POST.get("cardno") 
                carddate = request.POST.get("carddate") 
                secucode = request.POST.get("secucode")
                sql = Pyment(username=username,cardno=cardno,carddate=carddate,secucode=secucode)
                sql.save()
                sql1 = Member(username=username)
                sql1.save()
                return redirect ('home')

        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        context={
                'data':data,
                'data1':data1,
            }
        return render (request,'../templates/payment.html',context)
    else:
        return redirect('register')

def writeblog(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(username=username)
        for i in data:
            uid=i.uid
        data2 = Profile.objects.get(pk=uid)
        if request.method == "POST":
             cimage= request.FILES.get("cover_image") 
             title= request.POST.get("title") 
             subtitle= request.POST.get("subtitle") 
             content= request.POST.get("content") 
             sql=Blogwrite(author=data2,cimage=cimage,title=title,subtitle=subtitle,content=content)
             sql.save()
             return redirect ('home')
        
        data1=Member.objects.filter(username=username)
        if data1:
            context={
                    'data':data,
                    'data1':data1,
                }
            return render (request,'../templates/writeblog.html',context)
        else:
            return redirect ('membership')
    else:
        return redirect('register')

def register(request):
    if request.method == "POST":
        name = request.POST.get("name") 
        email = request.POST.get("email") 
        password = request.POST.get("password") 
        sql = User.objects.create_user(username=name,email=email,password=password)
        sql.save()
        obj=Profile(username=name,email=email)  
        obj.save()
        obj1=View(username=name)
        obj1.save()
        return redirect ('home')
    else:
        return render (request,'../templates/login.html')

def login_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

    user = authenticate(request,username=name, password=password)

    if user is not None:
            login(request,user)
            return redirect ('home')
    else:
            return render (request,'../templates/login.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

def bookmark(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        posts = Blogwrite.objects.filter(author=cprofile).order_by('-created_at')
        data5 = Save.objects.filter(susername=cprofile) 
        sbwids = [i.bwid for i in data5] 
        data6 = Blogwrite.objects.filter(bwid__in=[b.bwid for b in sbwids])
        for j in data6:
            j.is_saved = Save.objects.filter(susername=cprofile, bwid=j).exists()   

        
        context={
                    'data':data,
                    'data1':data1,
                    'data6':data6,
                    'posts':posts,
                } 
        return render (request,'../templates/bookmark.html',context)
    else:
        return redirect('register')

def ufollowing(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        duser = User.objects.get(username=username)
        join_date = duser.date_joined
        cprofile = get_object_or_404(Profile, username=current_user)
        current_profile = Profile.objects.get(username=request.user.username)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        fprofile=Follow.objects.filter(follower=cprofile)
        foprofile=Follow.objects.filter(following=cprofile)
        following_ids = Follow.objects.filter(follower=current_profile).values_list('following__uid', flat=True)

        context={
                    'data':data,
                    'data1':data1,
                    'join_date':join_date,
                    'fprofile':fprofile,
                    'foprofile':foprofile,
                    'following_ids':following_ids,  
                } 
        return render (request,'../templates/ufollowing.html',context)
    else:
        return redirect('register')

def ufollowers(request):
    if request.user.is_authenticated:
        username = request.user.username
        current_user = request.user.username
        duser = User.objects.get(username=username)
        join_date = duser.date_joined
        cprofile = get_object_or_404(Profile, username=current_user)
        current_profile = Profile.objects.get(username=request.user.username)
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        fprofile=Follow.objects.filter(follower=cprofile)
        foprofile=Follow.objects.filter(following=cprofile)
        following_ids = Follow.objects.filter(follower=current_profile).values_list('following__uid', flat=True)

        context={
                    'data':data,
                    'data1':data1,
                    'join_date':join_date,
                    'fprofile':fprofile,
                    'foprofile':foprofile,
                    'following_ids':following_ids,  
                } 
        return render (request,'../templates/ufollowers.html',context)
    else:
        return redirect('register')

def followersi(request,uid):
    if request.user.is_authenticated:
        username = request.user.username
        data2=Profile.objects.filter(uid=uid)
        for i in data2:
            fuser=i.username
        if fuser == username:
            return redirect('ufollowers')
        else:
            duser = User.objects.get(username=username)
            join_date = duser.date_joined
            cprofile = get_object_or_404(Profile, uid=uid)
            current_profile = Profile.objects.get(username=request.user.username)
            data = Profile.objects.filter(username=username)
            data1=Member.objects.filter(username=username)
            
            fprofile=Follow.objects.filter(follower=cprofile)
            foprofile=Follow.objects.filter(following=cprofile)
            following_ids = Follow.objects.filter(follower=current_profile).values_list('following__uid', flat=True)

            context={
                        'uid':uid,
                        'data':data,
                        'data1':data1,
                        'data2':data2,
                        'join_date':join_date,
                        'fprofile':fprofile,
                        'foprofile':foprofile,
                        'following_ids':following_ids,  
                    }  
            return render (request,'../templates/followersi.html',context)
    else:
        return redirect('register')
        
def followingi(request,uid):
    if request.user.is_authenticated:
        username = request.user.username
        data2=Profile.objects.filter(uid=uid)
        for i in data2:
            fuser=i.username
        if fuser == username:
            return redirect('ufollowers')
        else:
            duser = User.objects.get(username=username)
            join_date = duser.date_joined
            cprofile = get_object_or_404(Profile, uid=uid)
            current_profile = Profile.objects.get(username=request.user.username)
            data = Profile.objects.filter(username=username)
            data1=Member.objects.filter(username=username)
            fprofile=Follow.objects.filter(follower=cprofile)
            foprofile=Follow.objects.filter(following=cprofile)
            following_ids = Follow.objects.filter(follower=current_profile).values_list('following__uid', flat=True)

            context={
                        'uid':uid,
                        'data':data,
                        'data1':data1,
                        'data2':data2,
                        'join_date':join_date,
                        'fprofile':fprofile,
                        'foprofile':foprofile,
                        'following_ids':following_ids,  
                    }  
            return render (request,'../templates/followingi.html',context)
    else:
            return redirect('register')
        
def about(request):

    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(username=username)
        data1=Member.objects.filter(username=username)
        query = None  
        current_profile = Profile.objects.get(username=request.user.username)

        query = request.GET.get('q', '')
        results = [] 
        if query:
            results = Blogwrite.objects.filter( Q(title__icontains=query) | Q(content__icontains=query)| Q(author__username__icontains=query) | Q(author__name__icontains=query)).order_by('-created_at')  
        else:
            results = []
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            message = request.POST["message"]
            sql = Contect(user=current_profile,name=name,email=email,message=message)
            sql.save()
        context={
                'data':data,
                'data1':data1,
                'query': query,
                'results': results,
            }
        return render (request,'../templates/about.html',context)
    else:
        return redirect ('register')

def notification(request):
    if request.user.is_authenticated:
        username = request.user.username
        data = Profile.objects.filter(username=username)
        data1 = Member.objects.filter(username=username)
        current_user = request.user.username
        cprofile = get_object_or_404(Profile, username=current_user)

        notifications = []

        # Get all blogs by this user
        ublogs = Blogwrite.objects.filter(author=cprofile)

        for ublog in ublogs:
            # Comments
            bcomment = Comment.objects.filter(bwid=ublog).order_by('-cdate')
            for k in bcomment:
                commenter_profile = Profile.objects.filter(username=k.cusername).first()
                liked = Like.objects.filter(user=request.user, comment=k).exists()
                if commenter_profile:
                    notifications.append({
                        'cid': k.cid,
                        'bwid': k.bwid.bwid,
                        'cbname': k.bwid.title,
                        'comment': k.comment,
                        'date': k.cdate,
                        'name': commenter_profile.name,
                        'username': commenter_profile.username,
                        'image': commenter_profile.image,
                        'uid': commenter_profile.uid,
                        'liked': liked,
                        'notif_type': 'comment',
                    })

            # Likes
            blike = Like.objects.filter(blog=ublog)
            for l in blike:
                liker_profile = Profile.objects.filter(username=l.user.username).first()
                if liker_profile:
                    notifications.append({
                        'bwid': l.blog.bwid,
                        'bname': l.blog.title,
                        'name': liker_profile.name,
                        'username': liker_profile.username,
                        'image': liker_profile.image,
                        'date': l.ldate,
                        'uid': liker_profile.uid,
                        'notif_type': 'like',
                    })
        notifications.sort(key=lambda x: x.get('date'), reverse=True)

    
        context = {
            'data': data,
            'data1': data1,
            'notifications': notifications
        }
        return render(request, '../templates/notification.html', context)
    else:
        return redirect('register')
    
