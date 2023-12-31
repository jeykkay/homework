# Generated by Django 5.0.1 on 2024-01-08 12:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0001_initial'),
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('articles', models.ManyToManyField(to='Article.article')),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Author.author')),
            ],
        ),
    ]
