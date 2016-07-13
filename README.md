# GitHubManager

### backup(clone or fetch) organizations and its repositories:

`run.py [-f] file.txt [-u] username [-t] OAuth_token.txt` 

example: 
  1.  
    `run.py -f list.txt` 

    ### That will backup the repositories of the organizations listed on "list.txt"
  2. 
    `run.py -u pawpepe` 

    ### This command will backup organizations and repositories that belong to "pawpepe" 

  3.
    `run.py -f file.txt -u pawpepe` 
    it will run 1 and 2 
    
  4. `run.py -f file.txt -t oAuthToken.txt`
  
    ### You can provide a path to the file that contains your token. This way you wont be prompt to enter your username/password
    alternative: Go to the `GitBackup.py` code and replace `False` attribute ( `token = False`) with your OAuth token at `login(tk)`. 
    * DO NOT upload this code with your token to a Public/Shared repository at Github for security purposes! ( your token are your credentials)
    
    
    
## Observation:
  1. ### Inside the file.txt each organization must be listed in one line 
     example:
  
     Organization1 
  
     Organization2 
  
     Organization3 
  
    ...

  2. ### Make sure to have Python 2.7 up and PyGitHub installed on your computer 
  
  3. ### Have a Github account 
  
  
