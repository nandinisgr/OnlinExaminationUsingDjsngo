# Generated by Django 2.1 on 2018-10-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineapp', '0003_auto_20181024_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_Name', models.CharField(max_length=25)),
                ('Admin_Id', models.CharField(max_length=25, unique=True)),
                ('Password', models.CharField(max_length=25)),
                ('Confirm_PassWord', models.CharField(max_length=25)),
                ('Email_ID', models.EmailField(max_length=254, unique=True)),
                ('Contact_No', models.IntegerField(unique=True)),
                ('Password_Key', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='questions',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]