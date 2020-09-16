
import jenkins

import configparser

import requests

from requests.auth import HTTPBasicAuth

def jenkins_update_job():

    j1server_cfg_file = "/Users/elian/Documents/gitWork/git.yy.com/jenkins-jobs-cfg/jenkins_jobs.ini"
    j1server = get_jenkins_server(j1server_cfg_file)

    j2server_cfg_file = "/Users/elian/Documents/gitWork/git.yy.com/jenkins-jobs-cfg/jenkins2_jobs.ini"
    j2server = get_jenkins_server(j2server_cfg_file)

    #job_name = "entgiftflw"
    with open('project.txt') as fp:
        build_jobs = fp.readlines()

    for line in build_jobs:
        job_name = line.strip('\r\n')
        print ('update %s nextBuildNumber' % job_name)

        j1_next_bn = j1server.get_job_info(job_name)['nextBuildNumber']
        print("jenkins1: %s, %d" % (job_name, j1_next_bn))

        (
            url,
            username,
            passwd
        ) = get_jenkins_account(j2server_cfg_file)
        j2_auth = HTTPBasicAuth(username, passwd)
        j2_status = change_next_build_number(url, j2_auth, job_name, j1_next_bn)
        j2_next_bn = j2server.get_job_info(job_name)['nextBuildNumber']
        print("jenkins2: %s, %d" % (job_name, j2_next_bn))

        if j2_status:
            print('close jenkins1 job : %s' % job_name)
            close_job(j1server, job_name)

def get_jenkins_server(server_cfg_file):
    config = EnConfigParser.read_from_file_as_dict(server_cfg_file)
    server = jenkins.Jenkins(config['jenkins']['url'], username=config['jenkins']['user'], password=config['jenkins']['password'])

    return server

def get_jenkins_account(server_cfg_file):
    config = EnConfigParser.read_from_file_as_dict(server_cfg_file)

    return  (
        config['jenkins']['url'],
        config['jenkins']['user'],
        config['jenkins']['password']
    )

def update_next_build_number(job_name, next_bn):
    j2server_cfg_file = "/Users/elian/Documents/gitWork/git.yy.com/jenkins-jobs-cfg/jenkins2_jobs.ini"
    config = EnConfigParser.read_from_file_as_dict(j2server_cfg_file)
    server = jenkins.Jenkins(config['jenkins']['url'], username=config['jenkins']['user'], password=config['jenkins']['password'])

    server.set_next_build_number(job_name, int(next_bn))

def change_next_build_number(baseurl, auth, job_name, next_bn):
    data = 'nextBuildNumber={}'.format(next_bn)
    headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
    posturl = "{}/job/{}/nextbuildnumber/submit".format(baseurl, job_name)
    response = requests.post(posturl, auth=auth, headers=headers, data=data)
    response.raise_for_status()

    print (response.status_code)
    return response.status_code

def close_job(server, job_name):
    server.disable_job(job_name)

class EnConfigParser(configparser.ConfigParser):

    optionxform = str

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

    @classmethod
    def read_from_file_as_dict(cls, path):
        config = EnConfigParser()
        config.read(path)
        return config.as_dict()



def main():
    jenkins_update_job()


if __name__ == '__main__':
    main()
