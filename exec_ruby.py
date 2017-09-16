from subprocess import Popen, PIPE, STDOUT

def ruby(filename='code.rb'):
    print 'Running Ruby code:'
    p = Popen(['ruby', filename], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output, errors = p.communicate() 
    print(output)
    return (output, errors)
