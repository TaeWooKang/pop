# Generated by Django 2.1.2 on 2018-11-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20181102_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='data',
            field=models.DateTimeField(null=True, verbose_name='등록일'),
        ),
        migrations.AddField(
            model_name='book',
            name='up',
            field=models.IntegerField(blank=True, default=0, verbose_name='추천'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, verbose_name='글쓴이'),
        ),
    ]
