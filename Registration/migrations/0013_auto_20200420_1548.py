# Generated by Django 3.0.3 on 2020-04-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0012_auto_20200417_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='Token',
            field=models.IntegerField(default=1001, primary_key=True, serialize=False),
        ),
    ]
