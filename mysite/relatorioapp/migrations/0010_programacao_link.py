# Generated by Django 4.2 on 2023-05-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relatorioapp", "0009_programacao_subtipo"),
    ]

    operations = [
        migrations.AddField(
            model_name="programacao",
            name="link",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
