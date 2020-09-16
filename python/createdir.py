
import os


WORKDIR = os.path.split(os.path.realpath(__file__))[0]


path1=WORKDIR + '/a/b/c/d/a1'
path2=WORKDIR + '/a/b/c/d/a2'
path3=WORKDIR + '/a/b/c/d/a3'

os.makedirs(path1)
os.makedirs(path2)
os.makedirs(path3)


os.mkdir(path1)
os.mkdir(path2)
os.mkdir(path3)


