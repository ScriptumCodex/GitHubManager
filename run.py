

#Anna Paula Pawlicka Maule
import os
import sys
import socket
import ssl
import argparse
import httplib
import subprocess
import GitBackup
from github import Github
from os.path import expanduser

parser =argparse.ArgumentParser()
parser.add_argument("-f","--file",help="file path to GitHub organization's list")
parser.add_argument("-u","--user",help="Github user id to backup all hers/his organizations or repositories")
parser.add_argument("-t","--token", help="Path to the file that contains the OAuth token")

arg =parser.parse_args()

orgFile = arg.file
username = arg.user 
token = arg.token


g = GitBackup.login(token)


if __name__ == "__main__":

	if  orgFile:
		GitBackup.file_organizations(orgFile, g)

	if  username:
		
		GitBackup.report_user(username, g)


		