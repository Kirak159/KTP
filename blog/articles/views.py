from django.shortcuts import render

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