from django.contrib import admin
from django.forms import BaseInlineFormSet
from .models import Article, Category, CategoryArticle
from django.core.exceptions import ValidationError


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        val_count = 0
        for form in self.forms:
            new_dict = form.cleaned_data
            main_section = new_dict.get('is_main')
            if main_section:
                val_count += 1
        if val_count > 1:
            raise ValidationError('Укажите основной раздел')
        elif val_count == 0:
            raise ValidationError('No_tags')
        return super().clean()


class RelationshipInline(admin.TabularInline):
    extra = 1
    model = CategoryArticle
    formset = RelationshipInlineFormset
    fields = ['Category', 'is_main',]


@admin.register(Article)
class ArticleItems(admin.ModelAdmin):
    inlines = [RelationshipInline]


admin.site.register(Category, CategoryAdmin)

