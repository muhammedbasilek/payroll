# Generated by Django 4.2.5 on 2023-09-09 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_remove_employeereport_employee_employee_report_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='group',
        ),
    ]
