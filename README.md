# GitHubManager

#### backup(clone or fetch) organizations and its repositories:

`githubManager.py [-f] file.txt [-u] username [-t] OAuth_token.txt` 

example: 

1.  `githubManager.py -f list.txt` 

    #### That will backup/update the repositories of the organizations listed on "list.txt"
    
2. `githubManager.py -u pawpepe` 

    #### This command will backup/update repositories that belong to user "pawpepe" 
  
3.  `githubManager.py -f file.txt -u pawpepe` 
  
    #### It will run 1 and 2 

4.  `githubManager.py -f file.txt -t oAuthToken.txt`
  
    #### You can provide a path to the file that contains your token. This way you wont be prompt to enter your username/password
    alternative: Go to the `GitBackup.py` code and replace `False` attribute ( `token = False`)(line 41) with your OAuth token at `login(tk)` function( line 33). 

    * How to create an [OAtuh Token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

    * DO NOT upload this code with your token to a Public/Shared repository at Github for security purposes! ( your token are your credentials)

## Observations:
  1. #### Inside the file.txt each organization must be listed in one line 
     example:
  
     Organization1 
  
     Organization2 
  
     Organization3 
  
    ...

  2. #### Make sure to have Python 2.7 up and PyGitHub installed on your computer 
  
  3. #### Have a Github account 
  
  
  
