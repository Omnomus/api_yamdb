# Generated by Django 3.0.5 on 2021-06-23 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_yauser_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yauser',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='yauser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
