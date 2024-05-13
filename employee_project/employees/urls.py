from django.urls import path
from .views import EmployeeCreateAPIView

urlpatterns = [
    path('create-employee/', EmployeeCreateAPIView.as_view(), name='employee-create'),
]
