# Generated by Django 5.1.7 on 2025-03-26 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campanha', '0002_campanha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lideranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('metas', models.TextField()),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liderancas', to='campanha.campanha')),
            ],
        ),
    ]
