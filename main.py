# import JobScraper
from bs4 import BeautifulSoup as bs
import requests
import math


if __name__ == '__main__':
    target_url = 'https://www.linkedin.com/jobs/search/?currentJobId=3763562394&geoId=90000348&keywords=data%20engineer&location=Greater%20Indianapolis&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'

    #get response from target_url by sending a request
    url_request = requests.get(target_url)
    url_text_response = url_request.text

    # create soup class of text response
    soup = bs(url_text_response,'html.parser')

    # find total jobs found
    total_jobs = int(soup.select('span.results-context-header__job-count')[0].text)

    # select all the jobs from the list
    job_cards = soup.select('div.base-card.relative.w-full.hover\\:no-underline.focus\\:no-underline.base-card--link.base-search-card.base-search-card--link.job-search-card')

    # extract job ids
    job_id_list = []
    for job in job_cards:

        job_id = job.get('data-entity-urn').split(":")[3]
        job_id_list.append(job_id)
    print(job_id_list)

    # job_cards.



    # pull total results from target_url