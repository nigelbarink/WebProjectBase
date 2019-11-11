import subprocess
cmds = {
    'gitHooks':'python automation/installGitHooks.py',
    'setupNpm':'python automation/setupNpm.py'
}

p = subprocess.Popen(cmds['gitHooks'], stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
print (out)

p = subprocess.Popen(cmds['setupNpm'], stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
print (out)




