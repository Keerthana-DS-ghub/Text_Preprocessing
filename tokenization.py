#tokenization

tokenized_docs = []
for doc in corpus:
  tokens = word_tokenize(doc)
  tokenized_docs.append(tokens)
#printing the all the tokens for all documents and the token lengths for each document    
print("\nTokenized Documents:")
for i, doc in enumerate(tokenized_docs):
  print(f"Document {i+1} Tokens:", doc[:], "... (Total:", len(doc), ")")
  print()  # Add an empty print statement for a new line.
