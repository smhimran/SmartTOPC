# Generated by Django 3.0.3 on 2020-04-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0009_delete_userprofileinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='TShirt',
            field=models.CharField(choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='M', max_length=10),
        ),
    ]
