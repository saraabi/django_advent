# Generated by Django 3.2.9 on 2021-11-17 02:45

from django.db import migrations, models
import django.db.models.deletion
import django_advent.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('advent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django_advent.storage_backends.PublicMediaStorage(), upload_to='files/'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advent.date')),
            ],
        ),
    ]
