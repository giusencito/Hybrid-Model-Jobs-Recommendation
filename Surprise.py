reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(merged_df[['SectionName', 'Description', 'DevelopmentPercentage']], reader)
trainset, testset = train_test_split(data,test_size=0.2, random_state=42)
knn_model = KNNBasic(sim_options={'name': 'cosine','user_based': False})
knn_model.fit(trainset)
content_model = SVD()
content_model.fit(trainset)
predictions = []
max_rating = merged_df['DevelopmentPercentage'].max()
min_rating = merged_df['DevelopmentPercentage'].min()