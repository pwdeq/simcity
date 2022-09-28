# Generated by Django 4.0.3 on 2022-09-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=40)),
                ('chip_count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transfered_chip_count', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_date', models.DateTimeField()),
                ('action', models.CharField(max_length=40)),
            ],
        ),
    ]