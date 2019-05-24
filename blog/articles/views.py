from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .models import Article
from .models import Article2
from django.http import Http404
def archive(request):    
    return render(request, 'archive.html', {"posts": Article.objects.all() })



def get_article(request, article_id):    
    try:        
        post = Article2.objects.get(id=article_id)        
        return render(request, 'article.html', {"post": post})    
    except Article2.DoesNotExist:        
        raise Http404
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':      #меняете на гет в вашем случае
            # обработать данные если метод POST
            form = {
                'text' : request.POST['text'],    #так же только request.GET т.к. <input type="text" name="text">  имя поля text и в request.GET оно лежит
                'title' : request.POST['title']     # тут вместо title из GET берите name="priority" 'priority' : request.POST['priority']
            }
            if(check(form['title'])==True):
                form['errors'] = u'Статья с таким название уже есть!'
                return render(request, 'create_post.html', {'form': form})
            else:
            # в словаре form будет храниться введенная информация
                if form['text'] and form['title']:
                # если поля заполнены без ошибок
                    Article.objects.create(          # создаете запись в бд 
                        text=form['text'],
                        title=form['title'],
                        author=request.user)
                #достаю только что созданную статью с целью получения ее id и редиректа на страницу с ней
                    article = Article.objects.get(title=form['title'])
                
                    return redirect('getart', article_id=article.id)
                else:
                # Если данные не корректны
                    form['errors'] = u'Не все поля заполнены'
                    return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
def check(nem):
    try:
        article=Article.objects.get(title=nem)
        if(nem==article.title):
            return True
        else:
            return False
    
    
    except Article.DoesNotExist:        
        return False
    