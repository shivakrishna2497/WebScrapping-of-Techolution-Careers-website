import numpy as np
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os
def getHTMLContent(link):
    html = urlopen(link)
    soup = BeautifulSoup(html, 'html.parser')
    return soup
content = getHTMLContent('https://techolution.app.param.ai/jobs/')
print(content)
source_code = """<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Project Manager</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Talent Acquisition Specialist</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Sr.QA Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Senior Cloud Specialist</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Cloud Native Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Data Scientist Intern</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Embedded Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">System Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Associate QA Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Solution Architect</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Android Mobile Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">iOS Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Associate Cloud Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Sr Full Stack Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Sr SAP PI/PO Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Blockchain Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Junior Cloud Native Developer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Senior DevOps Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Lead DevOps Engineer </h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Site Reliability Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">OSS DevOps Engineer</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">DevOps Architect</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Engineering Lead</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">HR and Community Specialist</h3>
<h3 data-v-5b44ba93="" class="job_name text-ellipsis">Machine Learning Engineer</h3>"""
soup = BeautifulSoup(source_code,features="lxml")
for el in soup.find():
    job_title = el.get_text()
    print(job_title) 
outfile = open('jobtitle.txt','w')
for l in job_title:
    outfile.write(str(l.strip('')))
outfile.close()
source_code2="""<span data-v-5b44ba93="" class="date_posted">3 days ago</span>
<span data-v-5b44ba93="" class="date_posted">3 days ago</span>
<span data-v-5b44ba93="" class="date_posted">8 days ago</span>
<span data-v-5b44ba93="" class="date_posted">20 days ago</span>
<span data-v-5b44ba93="" class="date_posted">21 days ago</span>
<span data-v-5b44ba93="" class="date_posted">23 days ago</span>
<span data-v-5b44ba93="" class="date_posted">24 days ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">a month ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">3 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>
<span data-v-5b44ba93="" class="date_posted">2 months ago</span>"""
soup = BeautifulSoup(source_code2,features="lxml")
for i in soup.find():
    date_posted=i.get_text()
    print(date_posted)
outfile2 = open('date.txt','w')
for l in date_posted:
    outfile2.write(str(l.strip('')))
outfile2.close()
with open('jobtitle.txt') as fp:
	lines1 = fp.read().split('\n')
with open('date.txt') as fp:
	lines2 = fp.read().split('\n') 
lines3=[]
for k in range(len(lines1)):
	line = lines1[k].split(',')[:3]
	line.extend( lines2[k].split(',')[:3] )
	lines3.append(','.join(line))
fp = open('techolution.txt','w')
fp.write('\n'.join(lines3) )
fp.close()
data = pd.read_csv('techolution.txt', header = None, names=["Job Title","Date Posted"])
print(data)
data.to_csv('Techolution.csv',index=False)
