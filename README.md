# GitHubManager

### backup(clone or fetch) organizations and its repositories:

`run.py [-f] file.txt [-u] username` 

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
    
## Observation:
  1. ### Inside the file.txt each organization must be listed in one line 
     example:
  
     Organization1 
  
     Organization2 
  
     Organization3 
  
    ...

  2. ### Make sure to have Python 2.7 up and PyGitHub installed on your computer 
  3. ### Have a Github account 
  
  
