from django.urls import path
from .views import employee_create_view, tool_create_view, success_page, job_create_view, employee_delete_view, \
    tool_delete_view, job_delete_view, employee_update_view, tool_update_view, job_update_view,efficiency_view

urlpatterns = [
    path('employee_create/', employee_create_view, name='employee_create_view'),
    path('tool_create/', tool_create_view, name='tool_create_view'),
    path('job_create/', job_create_view, name='job_create_view'),
    path('success_page/', success_page, name='success_page'),

    path('employee/<int:emp_ssn>/delete/', employee_delete_view, name='employee_delete_view'),
    path('tool/<str:tool_code>/delete/', tool_delete_view, name='tool_delete_view'),
    path('job/<int:job_id>/delete/', job_delete_view, name='job_delete_view'),

    path('employee/<int:emp_ssn>/update/', employee_update_view, name='employee_update_view'),
    path('tool/<str:tool_code>/update/', tool_update_view, name='tool_update_view'),
    path('job/<int:job_id>/update/', job_update_view, name='job_update_view'),

    
    path('calculate-efficiency/', efficiency_view, name='calculate_efficiency'),
    
]
