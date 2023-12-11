from django.shortcuts import render

from articles.models import Article, Category, CategoryArticle


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    object_list = Article.objects.all().order_by(ordering)
    scopes = Category.objects.all()
    context = {
        'object_list': object_list,
        'scopes': scopes
    }
    return render(request, template, context)