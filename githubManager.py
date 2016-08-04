# Anna Paula Pawlicka Maule
import argparse
import GitBackup

_f = "file path to GitHub organization's list"
_u = "Github user id to backup all hers/his organizations or repositories"
_t = "Path to the file that contains the OAuth token"

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help=_f)
parser.add_argument("-u", "--user", help=_u)
parser.add_argument("-t", "--token", help=_t)

arg = parser.parse_args()
orgFile = arg.file
username = arg.user
token = arg.token
while True:
    try:
        g = GitBackup.login(token)
        break
    except ValueError:
        if token:
            print("path of token is wrong or the OAuth token is invalid.")
            token = raw_input("token file path: ")
        else:
            print("invalid user or password. try again!")

if __name__ == "__main__":
    if orgFile:
        # backups or updates the all the organizations listes on the provided file
        GitBackup.file_organizations(orgFile, g)
    if username:
        #backups or updates the all the user reposiotires
        GitBackup.user_backup(username, g)
