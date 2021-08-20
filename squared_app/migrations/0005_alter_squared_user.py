# Generated by Django 3.2.6 on 2021-08-18 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squared_app', '0004_auto_20210818_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squared',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
