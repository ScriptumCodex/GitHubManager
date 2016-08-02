# Anna Paula Pawlicka Maule
import os
from github import Github
from os.path import expanduser

src = None
# getting users HOME path : User/username/
home = expanduser("~")
str(home)
# pat where all the Github repositories will be fetch
# TODO remove hard coded path...
base_path = home + "/projects"


def check_base_path():
    # check if the path already exists
    if os.path.exists(base_path):
        # fetch -all organizations and repositories here
        print "$HOME/projects already exists"
        return True

    # create directory/folder where the porjects will be
    # backed up in case the folder does not exists already
    else:
        os.makedirs(base_path)
        print "project folder created"
        return False


def login(tk):
    if tk:
        token_file = open(tk, 'r')
        token = token_file.readline()
        token = token.rstrip('\n')
        return Github(token)
    token = False
    if token:
        return Github(token)
    log = raw_input(" login: ")
    str(log)
    password = raw_input("password: ")
    str(password)
    return Github(log, password)


def fetch(orgs, repos):
    os.chdir(base_path + "/" + orgs.login + "/" + repos.name)
    os.system("git fetch --all ")
    print (orgs.login + repos.name + " fetched ")


def clone(orgs, repos):
    check_base_path()
    if not os.path.exists(base_path + "/" + orgs.login):
        makedir = base_path + "/" + orgs.login
        os.mkdir(makedir)
    os.chdir(base_path + "/" + orgs.login)
    os.system("git clone https://github.com/" + orgs.login + "/" + repos.name)
    # os.system("git clone https://github.com/" + org.login + "/" + repo.name)
    print orgs.login + repos.name + "  cloned"


def backup(orgs):
    for repo in orgs.get_repos():
            str(repo)
            if os.path.exists(base_path + "/" + orgs.login + "/" + repo.name):
                fetch(orgs, repo)
            else:
                clone(orgs, repo)


def print_org_info(orgs):
    print "\nOrganization Name:  " + orgs.name
    print "# Private repos : " + str(orgs.owned_private_repos)
    print "# Public repos : " + str(orgs.public_repos) + "\n"
    print "Org Login: " + orgs.login


def report_user(user, g):
    report = raw_input("Do you want full report?[y/n]")
    str(report)
    # getting the user's organizations :
    for org in g.get_user(user).get_orgs():
        print_org_info(org)
        if report == "y":
            # listing the organization's repositories
            for repo in org.get_repos():
                print repo.name
    # Fetching and Cloning repositories
    for org in g.get_user(user).get_orgs():
        str(org)
        backup(org)


def file_organizations(orgFile, g):
    tx = open(orgFile, 'r')
    for line in tx:
        str(line)
        line = line.rstrip('\n')
        org = g.get_organization(line)
        # print_org_info(org)
        backup(org)
        # checking out branches that belong to that repositories
        for repo in org.get_repos():
            print repo.name
            for b in repo.get_branches():
                os.chdir(base_path + "/" + org.login + "/" + repo.name)
                print str(b.name + "  checking out branches ...")
                os.system("git checkout -b " + b.name + " origin/" + b.name)


if __name__ == "__main__":
    user = raw_input("username: ")
    str(user)
    report_user(user)
