from django.db import models


# Employee Table
class Employee(models.Model):
    emp_ssn = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.TextField()
    emp_efficiency = models.FloatField(default=None, null=True)

    def __str__(self):
        return f"Details Of {self.emp_name}"


class Tool(models.Model):
    tool_code = models.CharField(primary_key=True, max_length=100)
    tool_name = models.CharField(max_length=100)
    max_length = models.FloatField()
    cost = models.FloatField()
    length_cut = models.FloatField()
    no_of_brk_points = models.IntegerField()
    tool_efficiency = models.FloatField(default=None, null=True)

    def __str__(self):
        return f"Tool: {self.tool_name} (Code: {self.tool_code})"


# Job Table
class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    job_name = models.CharField(max_length=100)
    length = models.FloatField()
    no_of_holes = models.IntegerField()
    tool_code = models.ForeignKey(Tool, on_delete=models.CASCADE, db_column='tool_code', to_field='tool_code')

    def __str__(self):
        return f"Job: {self.job_name} (ID: {self.job_id})"


# Machine Table
class Machine(models.Model):
    machine_id = models.IntegerField(primary_key=True)
    machine_name = models.CharField(max_length=100)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_id', default='default_job_id')
    tool_name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('machine_id', 'job_id')

    def __str__(self):
        return f"Machine: {self.machine_name} (ID: {self.machine_id})"


# Performs Table
class Performs(models.Model):
    date = models.DateField(primary_key=True)
    shift_number = models.IntegerField()
    shift_duration = models.FloatField()
    achieved = models.IntegerField()
    partial_shift = models.IntegerField()
    target = models.IntegerField()
    emp_ssn = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_ssn')
    job_name = models.ForeignKey(Job, on_delete=models.CASCADE, db_column='job_name')
    machine_name = models.ForeignKey(Machine, on_delete=models.CASCADE,db_column='machine_name')

    class Meta:
        unique_together = ['date', 'emp_ssn', 'job_name']

    def __str__(self):
        return f"Performs on {self.date} for {self.emp_ssn} (Job: {self.job_name}, Machine: {self.machine_name})"


class Breakdown(models.Model):
    date = models.DateField()
    tool_code = models.ForeignKey(Tool, on_delete=models.CASCADE, db_column='tool_code', to_field='tool_code')
    machine_id = models.ForeignKey(Machine,on_delete=models.CASCADE,db_column='machine_id',to_field='machine_id')
    length_used = models.FloatField()
    expected_length_remaining = models.FloatField()
    replaced_by = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    change_time = models.DurationField()
    no_of_min_shift = models.IntegerField()

    def __str__(self):
        return f"Breakdown on {self.date} for {self.tool_code} on {self.machine_id}"





