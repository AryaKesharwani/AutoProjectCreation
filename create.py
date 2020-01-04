import os
import sys
from github import Github

#Remember to create this variables, learn how to in the README
username = os.environ.get("GIT_USER")
password = os.environ.get("GIT_PASS")

#Enter where you want to save your projects, use "/" instead of "\"
PATH = "G:/Proyectos"

def new_folder_repo():
    fol_name = str(sys.argv[1])
    pubpriv  = str(sys.argv[2])
    os.makedirs(PATH + "/" + fol_name)

    user = Github(username, password).get_user()

    if (pubpriv == "private"):
        user.create_repo(fol_name, private = True)
    if (pubpriv == "public"):
        user.create_repo(fol_name, private = False)

    print("")
    print("Created repository and directory with name" + fol_name)

if __name__ == "__main__":
    new_folder_repo()