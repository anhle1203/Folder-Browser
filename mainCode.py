import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity_search(keyword_input):
    # Convert folder keywords dictionary to a DataFrame
    df = pd.read_csv("keywordsList.csv")

    # Initialize documents list
    documents = []
    
    # Process the keywords from the DataFrame
    for keywords in df["Keyword"]:
        keywords = keywords.lower().split(", ")
        documents.append(' '.join(keywords))
    
    # Normalize all input tokens to lower case to ensure uniformity
    keyword_input_processed = ' '.join(keyword_input.lower().split(', '))
    documents.append(keyword_input_processed)

    #Vectorize the documents using TF-IDF
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    #Compute Cosine Similarity between the input and all keywords
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    #Add similarity scores to the DataFrame
    df["Similarity"] = cosine_sim.flatten()

    # Sort the DataFrame by similarity scores and get the top 7 folders
    top_folders = df.sort_values(by = "Similarity", ascending = False).head(7)

    return top_folders[["Folder Name", "Similarity"]]


# -----------------------------------------------------------------------------------------------------------------
# GUI
from tkinter import ttk
import tkinter as tk

# Function to handle the search button click
def on_search():
    result_text.delete("1.0", tk.END) #delete previous query
    # Get the keyword input
    input = keyword_entry.get()
    # For now, just set the result text area to show the keyword input
    result = cosine_similarity_search(input)
    result_text.insert(tk.END, f"Results for: {input}\n{result}")

# Create the main application window
root = tk.Tk()
root.title("Keyword Search")
root.geometry("500x300")

# Create a label for the keyword input
keyword_label = ttk.Label(root, text="Enter Keywords:")
keyword_label.pack(pady=10)

# Create a text entry for keyword input
keyword_entry = ttk.Entry(root, width=50)
keyword_entry.pack(pady=10)

# Create a search button
search_button = ttk.Button(root, text="Search", command=on_search)
search_button.pack(pady=10)

# Create a text area for displaying results
result_text = tk.Text(root, height=10, width=60)
result_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()