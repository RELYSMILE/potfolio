# Generated by Django 4.2 on 2023-05-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daberechi', '0009_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
