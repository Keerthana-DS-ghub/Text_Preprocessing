lemmatizer = WordNetLemmatizer()

# Apply lemmatization to the documents
lemmatized_docs = []
for tokens in no_stopwords_including_also_docs:
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    lemmatized_docs.append(lemmatized_tokens)

# Print the lemmatized documents, along with their token counts
print("\nDocuments with Tokens Lowercased, Punctuation Removed, Stopwords Including 'also' Removed, and Lemmatized:")
for i, doc in enumerate(lemmatized_docs):
    print(f"Document {i+1} Tokens:", doc, "... (Total:", len(doc), ")\n")
