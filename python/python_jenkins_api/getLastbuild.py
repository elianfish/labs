# -*- coding: utf-8 -*-

import jenkins
import datetime


jenkins_server_url = 'https://xxx.yy.com/jenkins'
user_id = 'elian'
api_token = '64647'

server = jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)

outputs = []

with open('jenkinsjobs.list') as f:
    for job_name in f:
        # job_name = "fenda-ios_appstore"
        number = server.get_job_info(job_name)['lastBuild']['number']
        buildTimestamp = server.get_build_info(job_name, number)['id']
        print job_name, buildTimestamp
        outputs.append(job_name + ',' + buildTimestamp + '/n')


with open('jobbuildtime.list', 'w') as f:
     f.writelines(outputs)
