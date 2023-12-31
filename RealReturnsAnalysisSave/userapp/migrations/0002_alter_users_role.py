# Generated by Django 4.1.7 on 2023-04-21 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userapp.roles",
            ),
        ),
    ]
