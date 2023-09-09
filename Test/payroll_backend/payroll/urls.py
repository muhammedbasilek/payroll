from django.urls import path
from .views import *

urlpatterns = [
        path('employee-report/', EmployeeReportView.as_view(), name="employee-report"),
        path('create-employee-report/', EmployeeCreateView.as_view(), name="create-employee-report")
    ]