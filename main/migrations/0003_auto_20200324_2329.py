# Generated by Django 3.0.4 on 2020-03-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200324_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cover',
            field=models.ImageField(default='/about/mini-startrail.jng', upload_to='about'),
        ),
        migrations.AlterField(
            model_name='about',
            name='photo',
            field=models.ImageField(default='/about/profilna.jng', upload_to='about'),
        ),
    ]
