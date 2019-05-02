# WebScrapping-of-Techolution-Careers-website
Problem statement:   I need to scrap the data from techolution website and store the data in a dataframe according to the date posted   Step 1:  Created virtualenvironment for the task needed to be done and installed required dependencies   1.beautifulsoup4==4.7.1 2.lxml==4.3.3 3.numpy==1.16.3 4.pandas==0.24.2 5.urllib3==1.24.
 
 
 2  Step 2 :  Pulled the data from https://techolution.app.param.ai/jobs/ using BeautifulSoup  
 
 
 Step 3 :  I tried to pull the all the data regarding Job Titles and Date posted at once but I was getting empty list , So I pulled out each and every header tag which contained job title and stored it in “jobtitle.txt” file , Similarly stored all the data regarding date posted in “date.txt”  Step 4 :  Opened two text files and wrote down the entire details in third file “techolution.txt”  Step 5 :  Then I loaded the “techolution.txt” file into a dataframe according to the date posted with “Job Title” and “Date Posted” as Column names and stored the dataframe to a csv “Techolution.csv”
