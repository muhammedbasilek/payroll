from django.urls import path
from .views import *

urlpatterns = [
        path('get-report/', EmployeeReportView.as_view(), name="get-report"),
        path('create-employee-report/', EmployeeCreateView.as_view(), name="create-employee-report")
    ]