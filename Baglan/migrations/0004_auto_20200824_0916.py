# Generated by Django 3.0.7 on 2020-08-24 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Baglan', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Awtor'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sene'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Baglan.Post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Tekst'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Awtor'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Sene'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Surat'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Tekst'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Awatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Öz barada'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Doglan guni'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Şäher'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[['male', 'Erkek'], ['female', 'Aýal']], default='male', max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.CharField(choices=[['none', 'Hiç'], ['single', 'Ýeke'], ['in_a_rel', 'Gatnaşyklarda'], ['engaged', 'Meşgul'], ['complicated', 'Çylşyrymly']], default='none', max_length=20, verbose_name='Статус отношений'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ulanyjy ady'),
        ),
    ]
