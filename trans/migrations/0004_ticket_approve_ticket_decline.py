# Generated by Django 4.0.3 on 2022-09-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0003_ticket_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='approve',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='decline',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
