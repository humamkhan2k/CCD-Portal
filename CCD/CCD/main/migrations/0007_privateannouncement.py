# Generated by Django 2.2.5 on 2020-02-16 11:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200215_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poc_company', models.CharField(default='', max_length=40)),
                ('Announcement', models.TextField()),
                ('AnnouncementTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.UserProfile')),
            ],
        ),
    ]
