def JOB_NAME = 'TESTJOB'
def APP_NAME = 'YSLAPP'


def myFile = new File("${JOB_NAME}.properties")
println myFile.toPath()
myFile.write("APP_NAME=${APP_NAME}\n")
