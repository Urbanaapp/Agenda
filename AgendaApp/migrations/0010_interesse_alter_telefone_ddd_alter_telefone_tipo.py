# Generated by Django 4.2.6 on 2023-11-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgendaApp', '0009_alter_telefone_ddd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interesse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='telefone',
            name='ddd',
            field=models.IntegerField(verbose_name='DDD'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='tipo',
            field=models.CharField(choices=[('CEL', 'Celular'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('REC', 'Recado')], max_length=3),
        ),
    ]
