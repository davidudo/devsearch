# Generated by Django 4.0.1 on 2022-03-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]