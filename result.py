df_predictions = pd.DataFrame(predictions, columns=['SectionName', 'Description', 'DevelopmentPercentage','Similarity'])
recommendations = merged_df[['JobId', 'JobName', 'URL', 'Location', 'Date', 'Company','Description']].merge(df_predictions, on='Description')
recommendations = recommendations.sort_values('Similarity', ascending=False)[['JobName','Description','URL', 'Location','Date', 'Company', 'Similarity']]
recommendations = recommendations.drop_duplicates(subset=['JobName'])
recommendations = recommendations.loc[recommendations['Similarity'] != 0.0]
