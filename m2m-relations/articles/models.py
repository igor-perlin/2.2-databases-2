from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название раздела")

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField(verbose_name="Содержание статьи")
    sections = models.ManyToManyField(Section, through='ArticleSection', related_name='articles')
    # publication_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    publication_date = models.DateTimeField(verbose_name='Дата публикации', null=True, blank=True)



    def __str__(self):
        return self.title

class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name="Основной раздел")

    def __str__(self):
        return f"{self.article.title} - {self.section.title}"

