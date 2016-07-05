#-*- coding: utf-8 -*-

#Anna Paula Pawlicka Maule 


import socket
import ssl
import httplib
from github import Github

def load_orgs():
	 """ read in orgs.txt (one org per line) in to a list
    main calls report_orgs() """



def report_orgs(): 
	""" or each org in orgs_list print "total number or repos is X" followed by a list of names (hint)"""

user = raw_input("user name: ")
str(user)
password=raw_input("password: ")
str(password)
# First create a Github instance:
g = Github(user,password)



# getting the user's organizations :
for org in g.get_user("mattben").get_orgs():
    print "\nOrganization Name:\n "
    print org.name 

# listing the organization's repositories 
    for repo in org.get_repos():
    	print repo.name 
    




   