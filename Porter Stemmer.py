stemmer = PorterStemmer()

# Apply stemming to the documents
stemmed_docs = []
for tokens in no_stopwords_including_also_docs:
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    stemmed_docs.append(stemmed_tokens)

# Print the stemmed documents, along with their token counts
print("\nDocuments with Tokens Lowercased, Punctuation Removed, Stopwords Including 'also' Removed, and Stemmed:")
for i, doc in enumerate(stemmed_docs):
    print(f"Document {i+1} Tokens:", doc, "... (Total:", len(doc), ")\n")
