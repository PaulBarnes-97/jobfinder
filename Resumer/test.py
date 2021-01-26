from linkedin_api import Linkedin
from datetime import date
import os
import json




#Logs into linkedin and performs a job search.
#100 jobs are found and whittled down to a smaller list
def job_search():
    #start = time.time()
    api = Linkedin('paulwesleybarnes@gmail.com', 'Paul1997')

    #now = time.time()
    #print(now-start,"\n")

    #search for software engineer, entry leve, fulltime, Colorado, limit results to 100
    jobs = api.search_jobs(keywords='software engineer', experience='2', job_type='F', location_name='Colorado, United States', limit=150,)
    joblist = []

    #now = time.time()
    #print(now-start,"\n")

    #go thru jobs to pull info
    job_TEST_list = []
    for index in range((len(jobs))):

     #   now = time.time()
     #  print(now-start,"\n")

        j = jobs[index]
        a = j.get('companyDetails')
        a = str(a.get('company'))
        a = list(a.split(":"))
        comp = api.get_company(a[-1])
        comp_Name= comp.get('universalName')
        comp_Addr = comp.get('url')
        job_title = str(j.get('title'))

        a = j.get('formattedLocation')
        a = list(a.split(", "))
        job_city = str(a[0])
        if len(a)>1:
            job_state = str(a[1])
        else:
            continue
        a = (j.get('briefBenefitsDescription'))
        if len(a) < 1:
            a=" "
        job_benefits = str(a)

        a = (j.get('applyMethod'))
        job_url = str(a.get('companyApplyUrl'))

        job_json = {"job":[{
            "Job_Title": job_title,
            "Company": str(comp_Name),
            "LinkedIn": str(comp_Addr),
            "City": job_city,
            "State": job_state,
            "Benefits": job_benefits,
            "Link": job_url
            }]}
        job_TEST_list.append(job_json)
    path = str(os.getcwd())
    today = str(date.today())
    file = ('/json dump/'+today+'.json')
    fp = path+file
    with open(fp,'w') as json_file:
        json.dump(job_TEST_list, json_file, indent=4,)
    #    now = time.time()
    #   print(now - start, "\n")
job_search()