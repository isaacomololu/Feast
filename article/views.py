from django.shortcuts import render, get_object_or_404
from .models import Article, Tag




# Create your views here.
def index(request):
    articles = Article.objects.order_by('-publication_date')[:5]
    older_articles = Article.objects.order_by('-publication_date')[3:12]
    most_read_articles = Article.objects.order_by('-views_count')[:5]
    context = {
        'articles': articles,
        'most_read_articles': most_read_articles,
        'older_articles': older_articles
    }
    return render(request, 'index.html', context)

def post(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.views_count += 1
    post.save()
    article_id = post.id
    user = post.author
    context = {
        'post': post,
        'article_id': article_id,
        'user': user
    }
    return render(request, 'post.html', context)

def tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    article = Article.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'article': article
    }

    return render(request, 'tags.html', context)




