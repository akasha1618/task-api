import faiss
import numpy as np
from embeddings_generator import embeddings

# Convert embeddings to a NumPy array
embeddings_np = np.array(embeddings)

# Create a Faiss index
index = faiss.IndexFlatL2(embeddings_np.shape[1])

# Add your embeddings to the index
index.add(embeddings_np)
faiss.write_index(index, 'faiss_index2.index')