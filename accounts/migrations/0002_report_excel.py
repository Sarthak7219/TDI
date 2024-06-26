# Generated by Django 4.2.4 on 2024-05-07 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('file', models.FileField(upload_to='user_excel_reports/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='excel_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
