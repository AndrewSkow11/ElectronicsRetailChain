# Generated by Django 5.0.6 on 2024-07-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chain", "0002_alter_linkofchain_supplier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="market_date",
            field=models.DateField(verbose_name="дата выхода на рынок"),
        ),
    ]
