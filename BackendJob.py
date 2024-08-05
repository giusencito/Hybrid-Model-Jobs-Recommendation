 def getBackendJobs(self):
     url = backendURL
     self.GetJob(url)
     self.start=0
     df = pd.DataFrame(self.data, columns=['Jobname', 'URL', 'Location', 'Date', 'Company', 'Description'])
     df.to_csv('csv/Backendjobs.csv', sep='\t',index=False)