#-*- coding: utf-8 -*-

#Anna Paula Pawlicka Maule 
import os
import sys
import socket
import ssl
import httplib
from github import Github
from os.path import expanduser


def load_orgs():
	 """ read in orgs.txt (one org per line) in to a list
    main calls report_orgs() """



def report_orgs(): 
	""" or each org in orgs_list print "total number or repos is X" followed by a list of names (hint)"""

user = raw_input("user name: ")
str(user)
g = Github()



if sys.argv[1] == "all" :

	# getting the user's organizations :
	for org in g.get_user(user).get_orgs():
	    print "\nOrganization Name:  " + org.name 
	    print "# Private repos : " + str(org.owned_private_repos)
	    print "# Public repos : " + str(org.public_repos) + "\n"


	# listing the organization's repositories 
	    for repo in org.get_repos():
	    	print repo.name 
    
elif sys.argv[1] == "none" : 
	# getting the user's organizations :
	for org in g.get_user(user).get_orgs():
	    print "\nOrganization Name:  " + org.name 
	    print "# Private repos : " + str(org.owned_private_repos)
	    print "# Public repos : " + str(org.public_repos) + "\n"


#getting users HOME path : User/username/
home = expanduser("~") 
str(home)

#pat where all the Github repositories will be fetch 
base_path = home + "/projects"

#check if the path already exists 
if os.path.exists(base_path) :
	# feth -all organizations and repositories here
	print "$HOME/projects already exists" 

#create directory/folder where the porjects will be backed up in case the folder does not exists already
else: 
	os.makedirs(base_path)
	print "project folder created"

#Fetching and Cloning repositories 
for org in g.get_user(user).get_orgs():
	str(org)
	for repo in org.get_repos():
		str(repo)
		if os.path.exists(base_path + "/" + org + "/" + repo)
			#git fetch all at "base_path + "/" + org + "/" + repo"
		else:
			os.makedirs(base_path)
			#git clone https://github.com/org/repo (in base_path/org)








   