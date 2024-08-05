def GetJob(self,url):
    while self.start < self.total_jobs:
          response = requests.get(url)
          soup = BeautifulSoup(response.text, 'html.parser')
          jobs = soup.find_all('li')
          for job in jobs:
              title = job.find('h3', class_=title).text.strip()
              url_element = job.find('a', class_=base_card)
              if url_element is not None:
                 job_url = url_element['href']
              else:
                 url_element = job.find('a', class_=base_card_relative)
                 if url_element is not None:
                    job_url = url_element['href']
                 else:
                    job_url = "URL not found"