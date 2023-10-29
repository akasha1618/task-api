from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


# Load  dataset
data = pd.read_csv('preprocessed_data.csv')

# Initialize the Sentence Transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(data['Description'].tolist())
print(embeddings.shape)

# Compute cosine similarity between all embeddings
#similarity_matrix = cosine_similarity(embeddings)
# similarity between the task in the doc
#print(similarity_matrix)