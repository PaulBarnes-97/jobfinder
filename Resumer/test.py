from linkedin_api import Linkedin
from datetime import date, time
import os
import json




#Logs into linkedin and performs a job search.
#100 jobs are found and whittled down to a smaller list
def job_search(today):

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
#################################
#City and State assigned to variables, acts as state filter
#################################
        a = j.get('formattedLocation')
        a = list(a.split(", "))
        job_city = str(a[0])
        if len(a)>1:
            if str(a[1]) == "CO":
                job_state = str(a[1])
            else:
                continue
        else:
            continue
#################################
# company info
#################################
        a = j.get('companyDetails')
        a = str(a.get('company'))
        a = list(a.split(":"))
        comp = api.get_company(a[-1])
        comp_Name = comp.get('universalName')
        comp_Addr = comp.get('url')
        job_title = str(j.get('title'))

        a = (j.get('briefBenefitsDescription'))
        if len(a) < 1:
            a = " "
        job_benefits = str(a)

        a = (j.get('applyMethod'))
        job_url = str(a.get('companyApplyUrl'))

        job_json = {
            "Job_Title": job_title,
            "Company": str(comp_Name),
            "LinkedIn": str(comp_Addr),
            "City": job_city,
            "State": job_state,
            "Benefits": job_benefits,
            "Link": job_url
            }
        job_TEST_list.append(job_json)
        if len(job_TEST_list) == 10:
            job_dict = {"job": job_TEST_list}
            break

    path = str(os.getcwd())
    file = ('/json dump/'+str(today)+'.json')
    fp = path+file
    with open(fp,'w') as json_file:
        json.dump(job_dict, json_file, indent=4,)

#job_search()