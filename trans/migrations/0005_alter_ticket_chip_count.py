# Generated by Django 4.0.3 on 2022-09-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0004_ticket_approve_ticket_decline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='chip_count',
            field=models.CharField(max_length=40),
        ),
    ]
