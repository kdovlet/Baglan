# Generated by Django 3.0.7 on 2020-08-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baglan', '0004_auto_20200824_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[['Erkek', 'Erkek'], ['Aýal', 'Aýal']], default='male', max_length=10, verbose_name='Jynsy'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.CharField(choices=[['Hiç', 'Hiç'], ['Ýeke', 'Ýeke'], ['Gatnaşyklarda', 'Gatnaşyklarda'], ['Meşgul', 'Meşgul'], ['Çylşyrymly', 'Çylşyrymly']], default='none', max_length=20, verbose_name='Gatnaşyklar ýagdaýy'),
        ),
    ]