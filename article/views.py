from django.shortcuts import render
from  .models import Article
from .forms import ArticleForm

# Create your views here.
def listArticle(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/list.html', context)

def createArticle(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            article = form.save()
            return render(request, 'articles/detail.html', {'article': article})
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detailArticle(request, pk):
    article = Article.objects.get(id=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)