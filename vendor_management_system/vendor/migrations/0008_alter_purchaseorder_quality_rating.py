# Generated by Django 4.2.4 on 2024-05-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_alter_purchaseorder_response_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
