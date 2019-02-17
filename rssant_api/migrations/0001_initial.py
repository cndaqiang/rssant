# Generated by Django 2.1.7 on 2019-02-16 07:18

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RssFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'pending'), ('updating', 'updating'), ('ready', 'ready'), ('error', 'error')], help_text='状态', max_length=20)),
                ('url', models.URLField(help_text='供稿地址')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=200)),
                ('link', models.URLField(blank=True, help_text='网站链接')),
                ('author', models.CharField(blank=True, help_text='作者', max_length=200)),
                ('icon', models.URLField(blank=True, help_text='网站Logo或图标')),
                ('description', models.TextField(blank=True, help_text='描述或小标题')),
                ('version', models.CharField(blank=True, help_text='供稿格式/RSS/Atom', max_length=200)),
                ('dt_created', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('dt_updated', models.DateTimeField(auto_now=True, help_text='更新时间')),
                ('encoding', models.CharField(blank=True, help_text='编码', max_length=200)),
                ('etag', models.CharField(blank=True, help_text='HTTP response header ETag', max_length=200)),
                ('last_modified', models.CharField(blank=True, help_text='HTTP response header Last-Modified', max_length=200)),
                ('headers', django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='HTTP response headers, JSON object')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RssStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='标题', max_length=200)),
                ('link', models.URLField(blank=True, help_text='文章链接')),
                ('dt_published', models.DateTimeField(blank=True, help_text='发布时间')),
                ('dt_updated', models.DateTimeField(blank=True, help_text='更新时间')),
                ('summary', models.TextField(blank=True, help_text='摘要或较短的内容')),
                ('content', models.TextField(blank=True, help_text='文章内容')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rssant_api.RssFeed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='rssstory',
            index=models.Index(fields=['user', 'dt_updated'], name='rssant_api__user_id_45c533_idx'),
        ),
        migrations.AddIndex(
            model_name='rssstory',
            index=models.Index(fields=['feed', 'dt_updated'], name='rssant_api__feed_id_3b59a1_idx'),
        ),
        migrations.AddIndex(
            model_name='rssstory',
            index=models.Index(fields=['link'], name='rssant_api__link_88b5a7_idx'),
        ),
        migrations.AddIndex(
            model_name='rssfeed',
            index=models.Index(fields=['user', 'dt_updated'], name='rssant_api__user_id_ae71fd_idx'),
        ),
        migrations.AddIndex(
            model_name='rssfeed',
            index=models.Index(fields=['url'], name='rssant_api__url_c0c409_idx'),
        ),
    ]