from django.contrib import admin
from .models import Employee, Tool, Job, Machine, Performs, Breakdown

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_ssn', 'emp_name', 'mobile', 'address', 'emp_efficiency']


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['tool_code', 'tool_name', 'max_length', 'cost', 'length_cut', 'no_of_brk_points', 'tool_efficiency']


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_id', 'job_name', 'length', 'no_of_holes', 'tool_code']


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['machine_id', 'machine_name', 'job_id', 'tool_name']


@admin.register(Performs)
class PerformsAdmin(admin.ModelAdmin):
    list_display = ['date', 'shift_number', 'shift_duration', 'achieved', 'partial_shift', 'target', 'emp_ssn', 'job_name', 'machine_name']


@admin.register(Breakdown)
class BreakdownAdmin(admin.ModelAdmin):
    list_display = ['date', 'tool_code', 'machine_id', 'length_used', 'expected_length_remaining', 'replaced_by', 'reason', 'change_time', 'no_of_min_shift']
