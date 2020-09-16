from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30, null=True)
    passwd = models.CharField(max_length=20, null=True)


class Business(models.Model):
    jenkins_job_name = models.CharField(max_length=45, null=True)
    jenkins_job_url = models.CharField(max_length=255, null=True)
    jenkins_user_name = models.CharField(max_length=30, null=True)
    jenkins_user_passwd = models.CharField(max_length=20, null=True)
    uploaded_pgk_name = models.CharField(max_length=100, null=True)
    uploaded_pgk_path = models.CharField(max_length=100, null=True)
    start_shell_file = models.CharField(max_length=100, null=True)
    analysis_mode = models.IntegerField(null=True) #0 error analysis, 1all check
    analysis_result_file = models.CharField(max_length=100, null=True)
    analysis_log_file = models.CharField(max_length=100, null=True)
    analysis_reslut_type = models.IntegerField(null=True) #0 html, 1 txt
    first_build_nu = models.IntegerField(null=True)
    status = models.IntegerField(null=True) #0 closed, 1 running,2error

    user = models.ForeignKey('User',null=True, on_delete=models.DO_NOTHING)


class BusinessHistory(models.Model):
    result=models.IntegerField(null=True) #0 success, 1 program exit unzero, 2timeout
    result_url = models.CharField(max_length=100, null=True)
    log_url = models.CharField(max_length=100, null=True)
    console_url = models.CharField(max_length=100, null=True)
    build_nu = models.IntegerField(null=True)
    program_exit_nu = models.IntegerField(null=True)

    business = models.ForeignKey('Business',null=True, on_delete=models.DO_NOTHING)
