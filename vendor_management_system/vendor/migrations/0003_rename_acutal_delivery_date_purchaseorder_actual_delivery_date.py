# Generated by Django 5.0.4 on 2024-05-03 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_rename_vendor_performance_history_vendorperformancehistory_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='acutal_delivery_date',
            new_name='actual_delivery_date',
        ),
    ]
