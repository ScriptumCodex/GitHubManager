#-*- coding: utf-8 -*-

#Anna Paula Pawlicka Maule 
import os
import sys
import socket
import ssl
import httplib
from github import Github
from os.path import expanduser


	#getting users HOME path : User/username/
home = expanduser("~") 
str(home)
#pat where all the Github repositories will be fetch 
base_path = home + "/projects"

def check_base_path():



	#check if the path already exists 
	if os.path.exists(base_path) :
		# feth -all organizations and repositories here
		print "$HOME/projects already exists" 

	#create directory/folder where the porjects will be backed up in case the folder does not exists already
	else: 
		os.makedirs(base_path)
		print "project folder created"


def report_orgs(option, src): 

	g = Github()

	if (option == "all") or ( option == None):
		user = raw_input("user name: ")
		str(user)
	# reading organizations from a file 	
	if (option=="-f") or ( option=="all" and src!= None) :
		str(src)
		#checking if it is a valid path 
		if os.path.exists(src) == false:
			print "[error] invalid path!"
		#read dictionary and fetch the organization	
		else : 
			
			check_base_path()

	if (option== None) or (option == "all"):
        
        	# getting the user's organizations :
		for org in g.get_user(user).get_orgs():
		    print "\nOrganization Name:  " + org.name 
		    print "# Private repos : " + str(org.owned_private_repos)
		    print "# Public repos : " + str(org.public_repos) + "\n"

	        if (report=="y") :
			    # listing the organization's repositories 
			    for repo in org.get_repos():
			    	print repo.name 
		        


			#Fetching and Cloning repositories 
		for org in g.get_user(user).get_orgs():
			str(org)
			for repo in org.get_repos():
				str(repo)
				if os.path.exists("cd " + base_path + "/" + org + "/" + repo):
						os.system("git fetch -all ")
						
				else:

					check_base_path

					os.system("cd " + base_path)
					os.system("mkdir " + org)
					os.system("cd " + org)
					os.system("git clone https://github.com/"+org+"/"+repo)
						







	









   