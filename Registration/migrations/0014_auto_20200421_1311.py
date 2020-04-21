# Generated by Django 3.0.3 on 2020-04-21 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0013_auto_20200420_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contestant',
            name='Campus',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='Department',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='ID',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='Section',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='contestant',
            name='Shift',
        ),
        migrations.AddField(
            model_name='contestant',
            name='basic_info',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Student'),
        ),
    ]
