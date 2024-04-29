# Generated by Django 4.2.3 on 2023-07-20 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('author_rank', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Справочник Авторов',
                'verbose_name_plural': 'Справочник Авторов',
                'ordering': ['author_rank'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryTitle', models.CharField(db_index=True, max_length=250, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Справочник категорий',
                'ordering': ['categoryID'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('ART', 'Статья'), ('NEWS', 'Новость')], default='ART', max_length=4)),
                ('date_and_time_created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('post_title', models.CharField(max_length=150, unique=True, verbose_name='Заголовок')),
                ('post_content', models.CharField(max_length=250, unique=True, verbose_name='Текст')),
                ('post_rank', models.IntegerField(default=0, verbose_name='Рейтинг ')),
                ('author_ID_FK', models.ForeignKey(db_column='author_ID_FK', on_delete=django.db.models.deletion.PROTECT, to='Portal.author', to_field='user_id')),
            ],
            options={
                'verbose_name': 'Статья/Новость',
                'verbose_name_plural': 'Статьи/Новости',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_ID_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.category')),
                ('post_ID_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Portal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category_ID_FK',
            field=models.ManyToManyField(through='Portal.PostCategory', to='Portal.category', verbose_name='связь многие ко многим'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('commend_ID', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=250, unique=True, verbose_name='Текст')),
                ('comment_created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
                ('comment_rank', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('post_ID_FK', models.ForeignKey(db_column='post_ID_FK', on_delete=django.db.models.deletion.PROTECT, to='Portal.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Статья/Новость',
                'verbose_name_plural': 'Статьи/Новости',
            },
        ),
    ]
