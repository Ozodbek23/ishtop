# Generated by Django 4.2.5 on 2023-09-09 12:13

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_telegramstate_alter_user_role_telegramuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramstate',
            name='logs',
            field=models.JSONField(default=users.models.default_logs),
        ),
    ]
