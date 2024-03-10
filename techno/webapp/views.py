from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, ToolForm, JobForm, EmployeessnForm
from .models import Employee, Tool, Job,Performs
from django.db.models import Sum



def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = EmployeeForm()

    return render(request, 'webapp/employee_form.html', {'form': form})


def tool_create_view(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = ToolForm()

    return render(request, 'webapp/tool_form.html', {'form': form})


from django.shortcuts import get_object_or_404

def job_create_view(request):
    if request.method == 'POST':
        # Process the form data
        job_id = request.POST.get('job_id')
        job_name = request.POST.get('job_name')

        selected_tools = request.POST.getlist('tools')
        for tool_code in selected_tools:
            length_field = f'length_{tool_code}'
            holes_field = f'no_of_holes_{tool_code}'
            length = request.POST.get(length_field)
            no_of_holes = request.POST.get(holes_field)

            # Retrieve the Tool instance based on the tool code
            tool = get_object_or_404(Tool, tool_code=tool_code)

            # Create the Job instance with the Tool reference and save it
            job = Job.objects.create(job_id=job_id, job_name=job_name, length=length, no_of_holes=no_of_holes, tool_code=tool)
            job.save()

        return redirect('success_page')  # Replace 'success_page' with the actual URL or view name
    else:
        # Retrieve tools for displaying in the form
        tools = Tool.objects.all()

    return render(request, 'webapp/job_form.html', {'tools': tools})

def employee_delete_view(request, emp_ssn):
    employee = get_object_or_404(Employee, emp_ssn=emp_ssn)

    if request.method == 'POST':
        employee.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/employee_delete.html', {'employee': employee})


def tool_delete_view(request, tool_code):
    tool = get_object_or_404(Tool, tool_code=tool_code)

    if request.method == 'POST':
        tool.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/tool_delete.html', {'tool': tool})


def job_delete_view(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('/webapp/success_page/')

    return render(request, 'webapp/job_delete.html', {'job': job})


def employee_update_view(request, emp_ssn):
    employee = get_object_or_404(Employee, emp_ssn=emp_ssn)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'webapp/employee_update.html', {'form': form})


def tool_update_view(request, tool_code):
    tool = get_object_or_404(Tool, tool_code=tool_code)

    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = ToolForm(instance=tool)

    return render(request, 'webapp/tool_update.html', {'form': form})


def job_update_view(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('/webapp/success_page/')
    else:
        form = JobForm(instance=job)

    return render(request, 'webapp/job_update.html', {'form': form})


def success_page(request):
    return render(request, 'webapp/success_page.html')


def calculate_efficiency(emp_ssn):
    performs_aggregated = Performs.objects.filter(emp_ssn=emp_ssn).aggregate(
        shift_duration_sum=Sum('shift_duration'),
        partial_shift_sum=Sum('partial_shift'),
        target_sum=Sum('target'),
        achieved_sum=Sum('achieved')
    )

    shift_duration_sum = performs_aggregated['shift_duration_sum']
    partial_shift_sum = performs_aggregated['partial_shift_sum']
    target_sum = performs_aggregated['target_sum']
    achieved_sum = performs_aggregated['achieved_sum']

    if shift_duration_sum and partial_shift_sum and target_sum and achieved_sum:
        x = target_sum * (partial_shift_sum / shift_duration_sum)
        efficiency = achieved_sum / x
        return efficiency
    else:
        return None

def efficiency_view(request):
    efficiency = None

    if request.method == 'POST':
        form = EmployeessnForm(request.POST)
        if form.is_valid():
            emp_ssn = form.cleaned_data['emp_ssn']
            efficiency = calculate_efficiency(emp_ssn)*100
    else:
        form = EmployeessnForm()

    return render(request, 'webapp/efficiency_template.html', {'form': form, 'efficiency': efficiency})


    


