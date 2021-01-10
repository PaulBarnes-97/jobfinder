from linkedin_api import Linkedin
import time




#Logs into linkedin and performs a job search.
#100 jobs are found and whittled down to a smaller list
def job_search():
    start = time.time()
    api = Linkedin('paulwesleybarnes@gmail.com', 'Paul1997')

    #now = time.time()
    #print(now-start,"\n")

    #search for software engineer, entry leve, fulltime, Colorado, limit results to 100
    jobs = api.search_jobs(keywords='software engineer', experience='2', job_type='F', location_name='Colorado, United States', limit=150,)
    joblist = []

    #now = time.time()
    #print(now-start,"\n")

    #go thru jobs to pull info
    for index in range((len(jobs))):

     #   now = time.time()
     #  print(now-start,"\n")

        job = []
        j = jobs[index]
        a = j.get('companyDetails')
        a = str(a.get('company'))
        a = list(a.split(":"))
        comp = api.get_company(a[-1])
        c= comp.get('universalName')
        d = comp.get('url')
        a = str(j.get('title'))
        job.append(str(a))
        job.append((str(c)))
        job.append(str(d))
        a = j.get('formattedLocation')
        a = list(a.split(", "))
        job.append(a[0])
        if len(a) > 1:
            job.append(a[1])
        a = (j.get('briefBenefitsDescription'))
        if len(a) < 1:
            a=" "
        job.append(str(a))
        a = (j.get('applyMethod'))
        b = a.get('companyApplyUrl')
        job.append(str(b))
        if job[-1] != 'None':
            joblist.append(job)
            print(job)
    joblist.sort(key=lambda x: x[4])
    return joblist
    #    now = time.time()
    #   print(now - start, "\n")