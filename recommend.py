for test_section, test_description, test_rating in testset:
    knn_pred = knn_model.predict(test_section,test_description, test_rating).est
    content_pred = content_model.predict(test_section, test_description,test_rating).est
    similarity_pred_content = calculate_similarity(test_section,test_description,content_pred)
    similarity_pred_knn = calculate_similarity(test_section,test_description,knn_pred)
    similarity_hybrid_pred = min((similarity_pred_content + similarity_pred_knn) / 2, 1.0)
    similarity_hybrid_pred = round(similarity_hybrid_pred, 1)
    section_rating = merged_df.loc[merged_df['SectionName'] == test_section,'DevelopmentPercentage'].iloc[0]
    normalized_rating = (section_rating - min_rating) / (max_rating - min_rating)
    similarity_hybrid_pred *= normalized_rating
    predictions.append((test_section, test_description, test_rating, similarity_hybrid_pred))