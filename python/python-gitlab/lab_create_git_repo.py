#/usr/bin/env python
# -*- coding: utf-8 -*


"auto create git repo"

import os,sys
import gitlab

WORKDIR = os.path.split(os.path.realpath(__file__))[0]
PROJECTFILE = os.path.join(WORKDIR, 'project.list')

def main():
    create_project_repo(PROJECTFILE)

def create_project_repo(ini_file):
    fp = open(ini_file, 'r')
    repo_names = fp.readlines()
    fp.close()


    ## login
    gl = gitlab.Gitlab.from_config('somewhere', ['/Users/elian/.python-gitlab.cfg'])

    group = gl.groups.get('gittooltest')  # 获取parent组对象
    print (group)
    subgroup_id_list = group.subgroups.list() # 获取所有子组group id
    print (subgroup_id_list)
    subgroup_id = group.subgroups.list(search="g-ci")[0].id # 指定要获取子组的group id
    print (subgroup_id)
    subgroup = gl.groups.get(subgroup_id) # 根据id获取子组对象
    projects = subgroup.projects.list()  # 获取子组下的项目
    print (projects)
    project = subgroup.projects.list(search="third-project")
    print (project)
    if project:
        print ("project found")
    else:
        print ("project not found")

    namespaces = gl.namespaces.list(search='gittooltest')
    print (namespaces)

if __name__ == '__main__':
    main()
