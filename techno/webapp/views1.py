from django.http import JsonResponse
from .models import Tool


def get_tool_names(request):
    job_id = request.GET.get('job_id', None)
    if job_id:
        try:
            # Retrieve tool names for the given job_id
            tools = Tool.objects.filter(job_id=job_id)
            tool_names = [tool.tool_name for tool in tools]
            return JsonResponse({'tool_names': tool_names})
        except Tool.DoesNotExist:
            return JsonResponse({'error': 'Tools not found for the given job ID'})
    else:
        return JsonResponse({'error': 'Job ID not provided'})



# Employee Efficiency:

# def calculate_efficiency(emp_ssn):
#     performs_aggregated = Performs.objects.filter(emp_ssn=emp_ssn).aggregate(
#         shift_duration_sum=Sum('shift_duration'),
#         partial_shift_sum=Sum('partial_shift'),
#         target_sum=Sum('target'),
#         achieved_sum=Sum('achieved')
#     )

#     shift_duration_sum = performs_aggregated['shift_duration_sum']
#     partial_shift_sum = performs_aggregated['partial_shift_sum']
#     target_sum = performs_aggregated['target_sum']
#     achieved_sum = performs_aggregated['achieved_sum']

#     if shift_duration_sum and partial_shift_sum and target_sum and achieved_sum:
#         x = target_sum * (partial_shift_sum / shift_duration_sum)
#         efficiency = achieved_sum / x
#         return efficiency
#     else:
#         return None



# Shift Efficiency:

# def calculate_shift_efficiency(shift_no):
#     shift_efficiency_aggregated = Performs.objects.filter(shift_no=shift_no).aggregate(
#         shift_duration_sum=Sum('shift_duration'),
#         partial_shift_sum=Sum('partial_shift'),
#         target_sum=Sum('target'),
#         achieved_sum=Sum('achieved')
#     )

#     return shift_efficiency_aggregated



# Employee Efficiency Monthly/Weekly:


# def calculate_employee_efficiency(emp_ssn, start_date, end_date):
#     employee_efficiency_aggregated = Performs.objects.filter(emp_ssn=emp_ssn, date__range=[start_date, end_date]).aggregate(
#         shift_duration_sum=Sum('shift_duration'),
#         partial_shift_sum=Sum('partial_shift'),
#         target_sum=Sum('target'),
#         achieved_sum=Sum('achieved')
#     )

#     return employee_efficiency_aggregated



# Shift Efficiency Monthly/weekly:

# def calculate_shift_efficiency(emp_ssn, shift_no, start_date, end_date):
#     shift_efficiency_aggregated = Performs.objects.filter(emp_ssn=emp_ssn, shift_no=shift_no, date__range=[start_date, end_date]).aggregate(
#         shift_duration_sum=Sum('shift_duration'),
#         partial_shift_sum=Sum('partial_shift'),
#         target_sum=Sum('target'),
#         achieved_sum=Sum('achieved')
#     )

#     return shift_efficiency_aggregated



# Breakdown Tools Details:

# def get_breakdown_table():
#     breakdown_table_entries = BreakdownTable.objects.all()
#     return breakdown_table_entries









