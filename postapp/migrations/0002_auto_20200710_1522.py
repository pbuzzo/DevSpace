# Generated by Django 3.0.8 on 2020-07-10 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('r', 'React'), ('h', 'HTML'), ('js', 'JavaScript'), ('p', 'Python'), ('d', 'Django')], default='h', max_length=10),
        ),
    ]