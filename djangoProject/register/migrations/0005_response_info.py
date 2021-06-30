"""Response_info"""
# pylint: disable= C0103,E0401
from django.db import migrations, models
import django.db.models.deletion


# pylint: disable = R0903
class Migration(migrations.Migration):
    """migrations"""
    dependencies = [
        ('register', '0004_alter_request_info_request_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='response_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, \
                                           serialize=False, verbose_name='ID')),
                ('response_message', models.CharField(max_length=150)),
                ('request_id',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, \
                                   to='register.request_info')),
            ],
        ),
    ]
