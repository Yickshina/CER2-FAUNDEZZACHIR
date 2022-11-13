# Generated by Django 4.1.3 on 2022-11-13 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_alter_correspondecia_conserje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correspondecia',
            name='conserje',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
