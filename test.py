#-*- coding: utf-8 -*-

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

src = None
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
        return True

    #create directory/folder where the porjects will be backed up in case the folder does not exists already
    else:
        os.makedirs(base_path)
        print "project folder created"
        return False



def report_orgs(option):

    login = raw_input(" login: ")
    str(login)
    password = raw_input("password: ")
    str(password)
    g = Github(login,password)



    if (option == "all") or ( option == None):
        user = raw_input("user name: ")
        str(user)
    # reading organizations from a file
    if (option=="-f") or ( option=="all" and src!= None) :
        str(src)
        #checking if it is a valid path
        if os.path.exists(src) == False:
            print "[error] invalid path!"
        #read dictionary and fetch the organization
        else :
            check_base_path()

    if (option== None) or (option == "all"):

        report = raw_input("Do you want full report?[y/n]")
        str(report)
                # getting the user's organizations :
        for org in g.get_user(user).get_orgs():
            print "\nOrganization Name:  " + org.name
            print "# Private repos : " + str(org.owned_private_repos)
            print "# Public repos : " + str(org.public_repos) + "\n"
            print "Org Login: " + org.login
            if report == "y":
            # listing the organization's repositories
                for repo in org.get_repos():
                    print repo.name



#Fetching and Cloning repositories
    for org in g.get_user(user).get_orgs() :
        str(org)
        for repo in org.get_repos() :
            str(repo)
            if os.path.exists(base_path + "/" + org.login + "/" + repo.name) :
                os.chdir(base_path + "/" + org.login + "/" + repo.name)
                os.system("git fetch --all ")
                print (org.login + repo.name + " fetched ")

            else:
                check_base_path()
                if os.path.exists(base_path+"/"+org.login) == False :

                    makedir = base_path + "/" + org.login
                    os.mkdir(makedir)


                os.chdir(base_path + "/" + org.login)
                os.system("git clone https://github.com/"+org.login+"/"+repo.name)
                #os.system("git clone https://github.com/"+org.login+"/"+repo.name)
                print org.login + repo.name + "  cloned"





if __name__ == "__main__":


    op = raw_input("option: all or none ? ")
    str(op)

result = report_orgs(op)

print result












