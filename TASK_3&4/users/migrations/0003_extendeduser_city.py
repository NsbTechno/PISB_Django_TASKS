# Generated by Django 3.2.6 on 2021-09-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210912_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='city',
            field=models.CharField(default=' ', max_length=12, null=True),
        ),
    ]