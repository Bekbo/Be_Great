# Generated by Django 3.2.12 on 2022-04-10 15:11

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя категории')),
                ('level', models.CharField(choices=[('Легкий', 'Легкий'), ('Средний', 'Средний'), ('Сложный', 'Сложный')], max_length=100, verbose_name='Уровень сложности')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование курса')),
                ('grade', models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)], verbose_name='Класс для которого предназначен курс')),
                ('priority', models.IntegerField(blank=True, default=0, verbose_name='Приоритетность курсов')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Заголовок вопроса')),
                ('description', models.CharField(max_length=100, verbose_name='Описание вопроса')),
                ('priority', models.IntegerField(default=0, verbose_name='Приоритет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='course.category', verbose_name='Категория к которому относится вопрос')),
                ('images', models.ManyToManyField(blank=True, to='api.Image', verbose_name='Изображении')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['priority'],
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Курс закончен?')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='Оценка по окончанию')),
                ('note', models.TextField(verbose_name='Заметки юзера')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.category', verbose_name='Текущая категория курса')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_courses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Прохождение курса',
                'verbose_name_plural': 'Прохождение курсов',
            },
        ),
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveSmallIntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='Приоритет')),
                ('option_text', models.CharField(blank=True, max_length=256, verbose_name='Вариант ответа')),
                ('result_text', models.CharField(blank=True, max_length=256, verbose_name='Результат выбора ответа')),
                ('value', models.CharField(blank=True, max_length=1, verbose_name='Буква ответа')),
                ('question', models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='course.question', to_field='title', verbose_name='Текст вопроса')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
                'ordering': ['priority'],
                'unique_together': {('priority', 'question')},
            },
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.questionoption', verbose_name='Вариант ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.question', verbose_name='Вопрос')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='course.course', verbose_name='Курс'),
        ),
    ]
