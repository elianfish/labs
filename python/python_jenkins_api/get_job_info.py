
import jenkins

import configparser

import requests

from requests.auth import HTTPBasicAuth

import xml.etree.ElementTree as ET
import string

def jenkins_update_job():

    j1server_cfg_file = "/Users/elian/Documents/gitWork/jenkins-jobs-cfg/jenkins_jobs.ini"
    j1server = get_jenkins_server(j1server_cfg_file)

    #job_name = "entgiftflw"
    job_infos = []
    with open('project.txt') as fp:
        build_jobs = fp.readlines()

    for line in build_jobs:
        job_name = line.strip('\r\n')

        is_job_name = j1server.get_job_name(job_name)
        if is_job_name == None:
            print('{} is not job '.format(job_name))
            job_infos.append('{},{},{}\n'.format(job_name, 'None', 'None'))
        else:
            j1_cfg_info = j1server.get_job_config(job_name)
            root = ET.fromstring(j1_cfg_info.encode('utf-8'))
            scm_url = get_scm_info(job_name, root)
            description = get_description_info(job_name, root)
            job_infos.append('{},{},{}\n'.format(job_name, scm_url, description))

    with open('job_info_output.txt', 'w') as f:
        f.writelines(job_infos)

def get_scm_info(job_name, root):
    scm_url = None
    e = root.find(
        './properties/hudson.model.ParametersDefinitionProperty'
        '/parameterDefinitions'
        '/hudson.scm.listtagsparameter.ListSubversionTagsParameterDefinition'
    )
    if e is not None:
        if e.find('./name').text in ('DEV_LINE', 'TAG_NAME'):
            scm_url = e.find('./tagsDir').text

    if scm_url is None:
        e = root.find(
            './scm/locations'
            '/hudson.scm.SubversionSCM_-ModuleLocation'
        )
        if e is not None:
            scm_url = e.find('./remote').text

    return scm_url

def get_description_info(job_name, root):
    e = root.find(
        './description'
    )
    if e is not None:
        description = e.text
        if description == None:
            return None

        if 'Do not edit this job through the web' in description:
            return None
        else:
            return description

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
