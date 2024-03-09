from django import forms
from .models import Employee, Tool, Job


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_ssn', 'emp_name', 'mobile', 'address']


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_code', 'tool_name', 'max_length', 'cost', 'length_cut']


class JobForm(forms.ModelForm):
    # tool_code = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Job
        fields = ['job_id', 'job_name', 'length', 'no_of_holes', 'tool_code']



class EmployeessnForm(forms.Form):
    emp_ssn = forms.CharField(label='Employee SSN', max_length=20)



