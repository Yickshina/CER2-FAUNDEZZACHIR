# Generated by Django 4.1.3 on 2022-11-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_correspondecia_conserje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondecia',
            name='conserje',
            field=models.CharField(max_length=50),
        ),
    ]
