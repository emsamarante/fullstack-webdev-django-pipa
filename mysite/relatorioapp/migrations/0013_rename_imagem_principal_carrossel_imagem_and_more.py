# Generated by Django 4.2 on 2023-05-29 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("relatorioapp", "0012_alter_carrossel_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="carrossel",
            old_name="imagem_principal",
            new_name="imagem",
        ),
        migrations.RemoveField(
            model_name="carrossel",
            name="imagem_secundaria",
        ),
        migrations.RemoveField(
            model_name="carrossel",
            name="legenda_secundaria_1",
        ),
        migrations.RemoveField(
            model_name="carrossel",
            name="legenda_secundaria_2",
        ),
    ]
