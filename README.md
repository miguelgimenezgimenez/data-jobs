# Programming Jobs in Glassdoor.
Program to scrape job listings in glassdor by providing a url to the CLI. 
Service added to send mails to the provided email with the info for the city requested.


### Usage : 
`python3 main.py -city Madrid`  =>  Get job listings for provided city. 


`python3 main.py -city Madrid --mailto`  =>  Get job listings for provided city and send email. Prompt will appear asking for credentials. 


`python3 main.py -cl`  =>  Get list of cities there is information for. 


`python3 main.py -stats`  =>  Get job listings all over the world. 


`python3 main.py -scr https://www.glassdoor.es/Empleo/madrid-empleos-SRCH_IL.0,6_IC2664239_IP1.htm?industryId=1059`  =>  Scrape given page


`python3 main.py -m -f Madrid`  =>  Merge data from a given file. 
