# naive-rag
Creating a basic rag system to test and evolve features

This RAG uses only pdf files as data

usable functions
documents = load_documents()
chunks = chunk_documents(documents)
embeddings = embed(chunks)
scores = cosine_similarity(query_embedding, embeddings)
top_chunks = retrieve_top_k(scores)
answer = generate(question, top_chunks)
