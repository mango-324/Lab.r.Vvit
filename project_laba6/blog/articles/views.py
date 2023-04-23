from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {'text': request.POST["text"], 'title': request.POST["title"]}
            if form["text"] and form["title"]:
                tmp = [x.id for x in Article.objects.all()]
                checked = True
                for x in Article.objects.all():
                    if x.title == form["title"]:
                        form['errors'] = u"Статья с таким названием уже существует"
                        checked = False
                        return render(request, 'create_post.html', {'form': form})
                if checked:
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    for x in Article.objects.all():
                        if x.id not in tmp:
                            idid = x.id
                    return redirect('get_article', article_id=idid)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
    
def auth_user(request):
    if not request.user.is_anonymous:
        return redirect("/archive/")
    else:
        if request.method == "POST":
            log, password = request.POST["login"], request.POST["password"]
            if log and password:
                try:
                    User.objects.get(username=log)
                    try:
                        trtlg = authenticate(username=log, password=password)
                        login(request, trtlg)
                        return redirect("/archive/")
                    except:
                        error = "Вы ввели неверный пароль"
                        return render(request, 'authorization.html', {'err': error, 'oldlog': log})
                except:
                    error = "Данный пользователь не существует"
                    return render(request, 'authorization.html', {'err': error})
            else:
                 error = "Не все поля заполнены"
                 return render(request, 'authorization.html', {'err': error})
        elif request.method == "GET":
            return render(request, 'authorization.html', {})


def reg_user(request):
    if not request.user.is_anonymous:
        return redirect("/archive/")
    else:
        if request.method == "POST":
            log, mail, pas = request.POST["login"], request.POST['email'], request.POST["password"]
            if log and mail and pas:
                try:
                    User.objects.get(username=log)
                    error = "Такое имя пользователя уже занято"
                    return render(request, 'registration.html', {'err': error})
                except User.DoesNotExist:
                    User.objects.create_user(log, mail, pas)
                    return redirect("/author/")
            else:
                error = "Не все поля заполнены"
                return render(request, 'registration.html', {'err': error})
        elif request.method == "GET":
            return render(request, 'registration.html', {})

def logoutting(request):
    if not request.user.is_anonymous:
        logout(request)
    return redirect("/archive/")


