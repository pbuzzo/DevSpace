# Generated by Django 3.0.8 on 2020-07-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0003_auto_20200719_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('h', 'HTML'), ('js', 'JavaScript'), ('d', 'Django'), ('r', 'React'), ('p', 'Python')], default='h', max_length=10),
        ),
    ]
