def calculate_similarity(test_section,test_description,rating):
    if test_section is None or pd.isnull(test_description):
       return 0
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([test_section,test_description])
    similarity = (tfidf_matrix * tfidf_matrix.T).A[0, 1] * rating
    return similarity