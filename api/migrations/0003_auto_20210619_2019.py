# Generated by Django 3.0.5 on 2021-06-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210617_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='yauser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='yauser',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='yauser',
            name='bio',
            field=models.TextField(blank=True, max_length=1000, verbose_name='About myself'),
        ),
        migrations.AlterField(
            model_name='yauser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='yauser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]