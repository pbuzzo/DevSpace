# Generated by Django 3.0.8 on 2020-07-10 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('messagesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('d', 'Django'), ('h', 'HTML'), ('js', 'JavaScript'), ('p', 'Python'), ('r', 'React')], default='h', max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('proj_url', models.URLField()),
                ('screen_shot', models.ImageField(upload_to='')),
                ('up_vote', models.IntegerField(default=0)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ManyToManyField(blank=True, to='messagesapp.Comment')),
            ],
        ),
    ]
