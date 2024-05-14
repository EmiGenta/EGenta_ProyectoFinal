# Generated by Django 5.0.6 on 2024-05-14 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancos', '0002_bancos_casa_central_bancos_mail_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancos',
            name='casa_central',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Casa Central'),
        ),
        migrations.AlterField(
            model_name='bancos',
            name='mail_contacto',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email de Contacto'),
        ),
        migrations.AlterField(
            model_name='bancos',
            name='pais_origen',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='País de Origen'),
        ),
    ]