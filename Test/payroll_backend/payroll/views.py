from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeReportSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
import calendar

class EmployeeReportView(APIView):
    @csrf_exempt
    def get(self,request):
        report_id = request.query_params.get('report_id')
        print(report_id,report_id)
        reports = EmployeeReport.objects.filter(report_id=report_id).first()
        if reports != None:
            reports = reports.employee_reports.all()
        else:
            return Response({"payrollReport":"","message":"No data found !!"},status=status.HTTP_200_OK)
        serializer = EmployeeReportSerializer(reports,many=True)
        return Response({"payrollReport":serializer.data,"message":""},status=status.HTTP_200_OK)


class EmployeeCreateView(APIView):
    @csrf_exempt
    def post(self,request):
        try:
            payrolldata = request.data
            report_name = payrolldata.get('file_name')
            csv_data = payrolldata.get('data')
            report_id = None
            try:
                if not report_name == None:
                    report_id = report_name.split("-")[2].split(".")[0]
            except:
                return Response({"payrollReport":"","message":"CSV file is unsupported !!"},status=status.HTTP_200_OK)
        
            #creating employee report database
            employeereport = EmployeeReport.objects.filter(report_id=report_id).first()
            if employeereport:
                return Response({"payrollReport":"","message":"Dumplicate report found !!"},status=status.HTTP_200_OK)
            employeereport = EmployeeReport.objects.create(report_id=report_id)

            #{'date': '4/11/2023', 'hours worked': 11, 'employee id': 2, 'job group': 'B'}
        
            report_data = []
            default_date = datetime(9999, 12, 31)
            #sorting csv data with employee id then date
            csv_data.sort(key=lambda x:(x.get('employee id', float('inf')),int(x.get('date').split("/")[0]) if x.get('date') else 35))
        
            month_type = "second"
            day = ""
            amount = 0;
            hours_worked = 0
            employee_id = ""
            monthtype = ""
            start_date=""
            #calculating report data for each two week
            for record in csv_data:
                report_data_obj = {}
            
                if record.get('employee id'):
                    employ_id = record.get('employee id')
                    date_obj = datetime.strptime(record.get('date'),"%d/%m/%Y")
                    day = date_obj.day
                    month = date_obj.month
                    year = date_obj.year
                    _,last_day = calendar.monthrange(year,month)
                    if (int(day) < 15 and monthtype == "last") or employ_id != employee_id:
                        if employee_id != "":
                            report_data_obj['employee_id'] = employee_id
                            report_data_obj['start_date'] = start_date
                            if monthtype == "last" :
                                report_data_obj['end_date'] = str(year) + "-" + str(month) +"-" + str(last_day) 
                            else:
                                report_data_obj['end_date'] = str(year) + "-" + str(month) + "-15" 
                            report_data_obj['amount'] = amount
                            report_data_obj['hoursworked'] = hours_worked
                            hours_worked = 0
                            amount = 0
                            report_data_obj['report'] = employeereport
                            report_data.append(report_data_obj)
                        monthtype = "first"
                        report_data_obj = {}
                        start_date = str(year) + "-" + str(month) + "-01"
                        hours_worked = record.get('hours worked')
                        if record.get('job group') == 'A':
                            amount = 20
                        elif record.get('job group') == 'B':
                            amount = 30
                    elif (int(day) > 15 and monthtype == "first") or employ_id != employee_id:
                    
                        if employee_id != "":
                            report_data_obj['employee_id'] = employee_id
                            report_data_obj['start_date'] = start_date
                            if monthtype == "first" :
                                report_data_obj['end_date'] = str(year) + "-" + str(month) + "-15" 
                            else:
                                report_data_obj['end_date'] = str(year) + "-" + str(month) +"-" + str(last_day) 
                            report_data_obj['amount'] = amount
                            report_data_obj['hoursworked'] = hours_worked
                            report_data_obj['report'] = employeereport
                            hours_worked = 0
                            amount = 0
                            report_data.append(report_data_obj)
                        monthtype = "last"
                        report_data_obj = {}
                        start_date = str(year) + "-" + str(month) + "-16"
                        hours_worked = record.get('hours worked')
                        if record.get('job group') == 'A':
                            amount = 20
                        elif record.get('job group') == 'B':
                            amount = 30
                    elif employ_id == employee_id:
                        if record.get('job group') == 'A':
                            amount += 20
                        elif record.get('job group') == 'B':
                            amount += 30
                        hours_worked += record.get('hours worked')
                    employee_id = record.get('employee id')
            report_data_obj = {} 
            _,last_day = calendar.monthrange(year,month)
            if day < 15:
                report_data_obj['employee_id'] = employee_id
                report_data_obj['start_date'] = str(year) + "-" + str(month) + "-01"
                report_data_obj['end_date'] = str(year) + "-" + str(month) + "-15"
                report_data_obj['amount'] = amount
                report_data_obj['hoursworked'] = hours_worked
                report_data_obj['employee_id'] = employee_id
                report_data_obj['report'] = employeereport
                report_data.append(report_data_obj)
            else:
                report_data_obj['employee_id'] = employee_id
                report_data_obj['end_date'] = str(year) + "-" + str(month) + "-" + str(last_day)
                report_data_obj['start_date'] = str(year) + "-" + str(month) + "-16"
                report_data_obj['amount'] = amount
                report_data_obj['hoursworked'] = hours_worked
                report_data_obj['employee_id'] = employee_id
                report_data_obj['report'] = employeereport
                report_data.append(report_data_obj)

            print(report_data)

            instances = [Employee(**key) for key in report_data]
            Employee.objects.bulk_create(instances)
            serializer = EmployeeReportSerializer(employeereport.employee_reports.all(),many=True)
            return Response({"payrollReport":serializer.data,"message":"successfully uploaded"},status=status.HTTP_200_OK)
        except:
            return Response({"payrollReport":"","message":"Something went wrong!!"},status=status.HTTP_200_OK)




# Create your views here.
