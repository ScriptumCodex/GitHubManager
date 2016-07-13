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



g = Github("90433323be0a5f3b3f74b5e28b18291a47b50874")


# getting the user's organizations :
for repo in g.get_user().get_repos():
        
    for b in repo.get_branches():
    	print str(b.name)
