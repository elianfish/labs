# Generated by Django 2.0.13 on 2020-09-07 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenkins_job_name', models.CharField(max_length=45, null=True)),
                ('jenkins_job_url', models.CharField(max_length=255, null=True)),
                ('jenkins_user_name', models.CharField(max_length=30, null=True)),
                ('jenkins_user_passwd', models.CharField(max_length=20, null=True)),
                ('uploaded_pgk_name', models.CharField(max_length=100, null=True)),
                ('uploaded_pgk_path', models.CharField(max_length=100, null=True)),
                ('start_shell_file', models.CharField(max_length=100, null=True)),
                ('analysis_mode', models.IntegerField(null=True)),
                ('analysis_result_file', models.CharField(max_length=100, null=True)),
                ('analysis_log_file', models.CharField(max_length=100, null=True)),
                ('analysis_reslut_type', models.IntegerField(null=True)),
                ('first_build_nu', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.IntegerField(null=True)),
                ('result_url', models.CharField(max_length=100, null=True)),
                ('log_url', models.CharField(max_length=100, null=True)),
                ('console_url', models.CharField(max_length=100, null=True)),
                ('build_nu', models.IntegerField(null=True)),
                ('program_exit_nu', models.IntegerField(null=True)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='analysis.Business')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('passwd', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='analysis.User'),
        ),
    ]