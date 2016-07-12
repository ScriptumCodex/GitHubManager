

#Anna Paula Pawlicka Maule
import os
import sys
import socket
import ssl
import argparse
import httplib
import subprocess
from github import Github
from os.path import expanduser

login = raw_input(" login: ")
str(login)
password = raw_input("password: ")
str(password)
g = Github(login,password)

org= g.get_organization("ESGF")

    
print "\nOrganization Name:  " + org.name
print "# Private repos : " + str(org.owned_private_repos)
print "# Public repos : " + str(org.public_repos) + "\n"
print "Org Login: " + org.login
            
	# listing the organization's repositories
for repo in org.get_repos():
    print repo.name