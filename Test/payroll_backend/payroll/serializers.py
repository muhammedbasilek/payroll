from rest_framework import serializers
from .models import *
class EmployeeReportSerializer(serializers.ModelSerializer):
    report_id = serializers.SerializerMethodField()
    payPeriod = serializers.SerializerMethodField()
    employeeId = serializers.SerializerMethodField()
    amountPaid = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ("employeeId","amountPaid","hoursworked","payPeriod","report_id")
    def get_report_id(self, obj):
        return obj.report.report_id
    def get_payPeriod(self, obj):
        dateObj = {}
        dateObj["startDate"] = obj.start_date
        dateObj["endDate"] = obj.end_date
        return dateObj
    def get_employeeId(self, obj):
        return obj.employee_id
    def get_amountPaid(self, obj):
        return "$" + str(obj.amount)