# Generated by Django 2.2.5 on 2019-10-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0002_auto_20191009_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nguoidung',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]
