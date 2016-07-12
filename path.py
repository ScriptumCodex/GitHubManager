import os
from github import Github
from os.path import expanduser

src = None 
	#getting users HOME path : User/username/
home = expanduser("~") 
str(home)

#pat where all the Github repositories will be fetch 
base_path = home + "/projects"

print base_path