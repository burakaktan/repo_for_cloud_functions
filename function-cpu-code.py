from collections import Counter
import re
from math import sqrt
from google.cloud import storage

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    import time
    start = time.time()
    #request_json = request.get_json()
    #text1 = request_json['text1']
    #text2 = request_json['text2']
    text1 = ""
    text2 = ""
    user_uuid = ""
    try:
        text1 = str(request.args.get('text1'))
        text2 = str(request.args.get('text2'))
        user_uuid = str(request.args.get('uuid'))
    except Exception as e:
        return e.message + + "text1= " + str(text1)
    
    similarity = compute_similarity(text1, text2)
    end = time.time()
    time_result = end-start
    
    # Create a client for interacting with Google Cloud Storage
    storage_client = storage.Client()
    
    # Get the bucket where the files will be stored
    bucket = storage_client.bucket("storage_time_and_result")
    
    # Write string1 to a file called "file1.txt"
    file1 = bucket.blob("function_time_"+ user_uuid +".txt")
    file1.upload_from_string(str(time_result))
    
    # Write string2 to a file called "file2.txt"
    file2 = bucket.blob("function_result_" + user_uuid + ".txt")
    file2.upload_from_string(str(similarity))

    return "function result:" + str(similarity) +  " with time: " + str(end-start)

def preprocess_text(text):
    # Remove punctuation and make all characters lowercase
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

def compute_similarity(text1, text2):
    # Preprocess the texts
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Tokenize the texts
    tokens1 = text1.split()
    tokens2 = text2.split()

    # Compute the frequency of each word in each text
    frequency1 = Counter(tokens1)
    frequency2 = Counter(tokens2)

    # Compute the dot product of the frequency vectors
    dot_product = sum(frequency1[token] * frequency2[token] for token in frequency1)

    # Compute the Euclidean norms of the frequency vectors
    norm1 = sqrt(sum(frequency1[token] ** 2 for token in frequency1))
    norm2 = sqrt(sum(frequency2[token] ** 2 for token in frequency2))

    # Return the cosine similarity
    return dot_product / (norm1 * norm2)
    