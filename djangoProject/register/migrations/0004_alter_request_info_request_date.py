"""Altered request_info"""
# pylint: disable= C0103,E0401
from django.db import migrations, models


# pylint: disable = R0903
class Migration(migrations.Migration):
    """Migrations"""

    dependencies = [
        ('register', '0003_alter_request_info_request_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_info',
            name='request_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
