from django.db import models


class EmployeeReport(models.Model):
    report_id = models.PositiveIntegerField(default=0)
    create_on = models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
    employee_id = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    hoursworked = models.PositiveIntegerField(default=0)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    create_on = models.DateTimeField(auto_now_add=True)
    report = models.ForeignKey(EmployeeReport, on_delete=models.CASCADE, null=True, related_name="employee_reports")


# Create your models here.
