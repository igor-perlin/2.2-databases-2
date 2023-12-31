# Generated by Django 4.2.5 on 2023-09-21 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_section_alter_article_options_remove_article_image_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='articlesection',
            name='unique_main_section',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='articlesection',
            name='is_main',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='Содержание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок статьи'),
        ),
    ]
