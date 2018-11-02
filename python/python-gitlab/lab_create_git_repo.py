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

    repo_url = 'https://git.test.com/gittooltest/g-ci/third-project.git'
    parent_group_name = repo_url.split('/')[3]
    sub_group_name  = repo_url.split('/')[4]
    project_name = repo_url.split('/')[5].replace('.git','')
    descri = project_name
    print (parent_group_name,sub_group_name,project_name)

    ## login
    gl = gitlab.Gitlab.from_config('somewhere', ['/Users/elian/.python-gitlab.cfg'])

    group_all = gl.groups.list(search=parent_group_name) # list会列出重名的组
    print (group_all)
    namespaces = gl.namespaces.list(search=parent_group_name) # 搜索指定组名获取namespaces
    print (namespaces)

    group = gl.groups.get(parent_group_name)  # 获取parent组对象
    print (group)
    subgroup_id_list = group.subgroups.list() # 获取所有子组group id
    print (subgroup_id_list)
    subgroup_id = group.subgroups.list(search=sub_group_name) # 指定要获取子组的group id
    print (subgroup_id)
    if subgroup_id:
        print ("%s subgroup found" % sub_group_name)
        subgroup_id_value = subgroup_id[0].id
        print (subgroup_id_value)
        subgroup = gl.groups.get(subgroup_id_value) # 根据id获取子组对象
        projects = subgroup.projects.list()  # 获取子组下的项目
        print (projects)
        project = subgroup.projects.list(search=project_name)
        print (project)
        if project:
            print ("%s project found" % project_name)
        else:
            print ("%s project not exist,新创建一个" % project_name)
            new_project = gl.projects.create({'name': project_name, 'namespace_id': subgroup_id_value, 'description': descri}) # 创建项目
    else:
        print ("%s subgroup not exist" % sub_group_name)


if __name__ == '__main__':
    main()
