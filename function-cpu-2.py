from collections import Counter
import re
from math import sqrt
from google.cloud import storage
import json

def hello_gcs(event, context):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    import time
    import requests
    start = time.time()
    [text1,text2, uuid] = get_texts(event)
    requests.get("https://service1-tjxfrnr6mq-uc.a.run.app?text1=" + text1 + "&text2=" + text2 + "&uuid=" + str(uuid))
    requests.get("https://us-central1-enduring-fold-367507.cloudfunctions.net/function-cpu?text1=" + text1 + "&text2=" + text2  + "&uuid=" + str(uuid))
    

def get_texts(event):
    file_name = event['name']

    storage_client = storage.Client()

    # Get the bucket and the blob
    bucket = storage_client.bucket("storage_for_text2")
    blob = bucket.blob(file_name)

    # Read the blob and print its contents
    blob_content = blob.download_as_string().decode()

    json_object = json.loads(blob_content)

    return [str(json_object['text1']),str(json_object['text2']), str(json_object['uuid'])]
    
