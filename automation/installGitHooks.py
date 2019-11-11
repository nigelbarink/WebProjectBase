import os
import shutil

CurrentPath = os.getcwd()

shutil.copyfile("automation/git_hooks/pre-commit" , ".git/hooks/pre-commit")


print ("DONE!")

