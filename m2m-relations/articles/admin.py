from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Section, ArticleSection

class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_section_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_section_count += 1
        if main_section_count != 1:
            raise ValidationError('Должен быть один и только один основной раздел')
        return super().clean()

class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
