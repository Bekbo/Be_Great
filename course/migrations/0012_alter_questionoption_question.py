# Generated by Django 3.2.12 on 2022-04-18 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_usercourse_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionoption',
            name='question',
            field=models.ForeignKey(max_length=256, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='course.question', verbose_name='Текст вопроса'),
        ),
    ]
