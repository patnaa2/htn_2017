from subprocess import Popen, PIPE, STDOUT

CHALLENGE_FILE_PRE = 'coding_challenge_pre.txt'
CHALLENGE_FILE_POST = 'coding_challenge_post.txt'

def ruby(filename='code.rb'):
    print 'Running Ruby code:'
    p = Popen(['ruby', filename], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output, errors = p.communicate()
    #print(output)
    if p.returncode != 0:
        errors = output
        output = None
    return (output, errors)

def make_challenge_file(text, ruby_file):
    with open(ruby_file, "w") as f:
        with open(CHALLENGE_FILE_PRE) as r:
            f.write(r.read())

        f.write(text)

        with open(CHALLENGE_FILE_POST) as r:
            f.write(r.read())

