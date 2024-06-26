# Generated by Django 5.0.4 on 2024-05-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vendor_performance_history',
            new_name='VendorPerformanceHistory',
        ),
        migrations.RenameField(
            model_name='purchaseorder',
            old_name='delivery_date',
            new_name='expected_delivery_date',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='acutal_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
