# GitHubManager

backup(clone or fetch) organizations and its repositories:

`run.py [-f] file.txt [-u] username` 

example: 
  1.  
    `run.py -f list.txt` 

    that will backup the repositories of the organizations listed on "list.txt"
  2. 
    `run.py -u pawpepe` 

    this command will backup organizations and repositories that belong to "pawpepe" 

  3.
    `run.py -f file.txt -u pawpepe` 
    it will run 1 and 2 
    
## Observation:
  inside the file.txt each organization must be listed in one line 
  example:
  
  Organization1 
  Organization2 
  Organization3 
  ...
  
  
