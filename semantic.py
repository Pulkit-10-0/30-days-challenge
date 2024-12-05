from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initialize Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use other SBERT models depending on your requirements

# Function to encode text into embeddings
def encode_text(text):
    # Ensure the tensor is on CPU
    embedding = model.encode(text, convert_to_tensor=True)
    return embedding.cpu().detach().numpy()  # Move to CPU and convert to numpy array

# Function to compute cosine similarity between two text embeddings
def compute_similarity(embedding1, embedding2):
    # Compute cosine similarity
    similarity = cosine_similarity(embedding1.reshape(1, -1), embedding2.reshape(1, -1))
    return similarity[0][0]

# Example texts: Student's answer and model answer
student_answer = """
quadratic equations  is hwo i dont know x while the are 2a or my 4ac then solution derived on or not the completing the incomplete solution of the square or yoooooooo whgile are the is the an 
"""

model_answer = """
Quadratic equations can be solved using the quadratic formula, which is derived by completing the square. 
The formula is given by x = (-b ± √(b² - 4ac)) / 2a.
"""

# Encode the answers into vector embeddings
student_embedding = encode_text(student_answer)
model_embedding = encode_text(model_answer)

# Compute the similarity score using cosine similarity
similarity_score = compute_similarity(student_embedding, model_embedding)

# Print the similarity score
print(f"Cosine Similarity Score: {similarity_score:.4f}")

# Threshold for determining a mismatch
threshold = 0.9

if similarity_score >= threshold:
    print("The student's answer is semantically similar to the model answer.")
else:
    print("The student's answer is not semantically similar to the model answer.")
