from django.shortcuts import render
from articles.models import Article


# def articles_list(request):
#     template = 'articles/news.html'
#     articles = Article.objects.all()
#
#     context = {
#         'articles': articles
#     }
#
#     return render(request, template, context)

def articles_list(request):
    articles = Article.objects.all()

    for article in articles:
        article.main_section = article.articlesection_set.filter(is_main=True).first().section
        article.other_sections = list(article.articlesection_set.filter(is_main=False).order_by('section__title'))

    return render(request, 'articles/news.html', {'articles': articles})

