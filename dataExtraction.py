jobs_df = pd.read_csv('jobs.csv',sep='\t')
ratings_df = pd.read_csv('ratings_section.csv')
sections_df = pd.read_csv('section.csv')
all_combinations = pd.MultiIndex.from_product([sections_df['SectionId'], jobs_df['JobId']], names=['SectionId', 'JobId'])
all_combinations_df = pd.DataFrame(index=all_combinations).reset_index()
merged_df = all_combinations_df.merge(ratings_df, on='SectionId', how='left')
merged_df = merged_df.merge(sections_df, left_on='SectionId',right_on='SectionId', how='left')
merged_df = merged_df.merge(jobs_df, left_on='JobId', right_on='JobId', how='left')
merged_df['DevelopmentPercentage'].fillna(0, inplace=True)