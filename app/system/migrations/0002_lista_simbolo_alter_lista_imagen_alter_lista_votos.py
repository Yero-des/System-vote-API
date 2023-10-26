# Generated by Django 4.2.5 on 2023-10-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='simbolo',
            field=models.ImageField(null=True, upload_to='symbol'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='lista',
            name='votos',
            field=models.IntegerField(default=0),
        ),
    ]
