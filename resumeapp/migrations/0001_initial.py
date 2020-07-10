# Generated by Django 3.0.8 on 2020-07-10 15:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=75)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resumeapp.Details')),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.TextField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=15)),
                ('role', models.CharField(max_length=75)),
                ('department', models.CharField(max_length=75)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resumeapp.Details')),
            ],
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(blank=True, max_length=75)),
                ('organization', models.TextField(blank=True, max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=3)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('summary', models.TextField(max_length=1000)),
                ('skills', models.TextField(blank=True, max_length=1000)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeapp.Education')),
                ('employment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeapp.Employment')),
                ('references', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumeapp.References')),
            ],
        ),
    ]
