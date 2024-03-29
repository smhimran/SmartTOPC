# Generated by Django 3.0.3 on 2020-04-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0011_auto_20200417_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='Campus',
            field=models.CharField(default='MC', max_length=10),
        ),
        migrations.AddField(
            model_name='contestant',
            name='Department',
            field=models.CharField(default='CSE', max_length=10),
        ),
        migrations.AddField(
            model_name='contestant',
            name='Name',
            field=models.CharField(default='No name', max_length=50),
        ),
        migrations.AddField(
            model_name='contestant',
            name='Section',
            field=models.CharField(default='A', max_length=10),
        ),
        migrations.AddField(
            model_name='contestant',
            name='Semester',
            field=models.CharField(default='1st', max_length=10),
        ),
        migrations.AddField(
            model_name='contestant',
            name='Shift',
            field=models.CharField(default='Day', max_length=10),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='ID',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='TShirt',
            field=models.CharField(default='M', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Campus',
            field=models.CharField(choices=[('MC', 'MC'), ('UC', 'UC')], default='MC', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('CSE', 'CSE'), ('SWE', 'SWE'), ('CIS', 'CIS'), ('Other', 'Other')], default='CSE', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Semester',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd')], default='1st', max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='Shift',
            field=models.CharField(choices=[('Day', 'Day'), ('Evening', 'Evening')], default='Day', max_length=10),
        ),
    ]
