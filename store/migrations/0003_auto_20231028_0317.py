# Generated by Django 3.0.5 on 2023-10-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20231028_0240'),
    ]

    operations = [
        migrations.DeleteModel(
            name='shProduct',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=40),
        ),
    ]