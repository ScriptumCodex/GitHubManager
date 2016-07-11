#-*- coding: utf-8 -*-

#Anna Paula Pawlicka Maule 

import sys
import socket
import ssl
import httplib
from github import Github

def load_orgs():
	 """ read in orgs.txt (one org per line) in to a list
    main calls report_orgs() """



def report_orgs(): 
	""" or each org in orgs_list print "total number or repos is X" followed by a list of names (hint)"""

#user = raw_input("user name: ")
#str(user)
#password=raw_input("password: ")
#str(password)
# First create a Github instance:
user = raw_input("user name: ")
str(user)
g = Github()



	# getting the user's organizations :
for org in g.get_user(user).get_orgs():
	print "\nOrganization Name:  " + org.name 
	print "# Private repos : " + str(org.owned_private_repos)
	print "# Public repos : " + str(org.public_repos) + "\n"


	# listing the organization's repositories 
	for repo in org.get_repos():
	    print repo.name 
    


   