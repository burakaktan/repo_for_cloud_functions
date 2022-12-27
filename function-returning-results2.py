from collections import Counter
import re
from math import sqrt
from google.cloud import storage
import json

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
    user_uuid = request.args.get('uuid')
    [function_result,function_time,cloud_run_result,cloud_run_time] = get_texts(user_uuid)
    end = time.time()
    string_list = [
                "function result: "+ str(function_result),
                "function took time: " + str(function_time),
                "cloud run result: " + str(cloud_run_result),
                "cloud run took time: " + str(cloud_run_time),
                "current function took time: " + str(end-start)]
    json_string = json.dumps(string_list)
    return json_string
    

def get_texts(user_uuid):
    # Set the names of the buckets and the files you want to read
    bucket_name = "storage_time_and_result"
    file_name_1 = "function_result_" + user_uuid + ".txt"
    file_name_2 = "function_time_" + user_uuid +  ".txt"
    file_name_3 = "cloud_run_result_" + user_uuid + ".txt"
    file_name_4 = "cloud_run_time_" + user_uuid  + ".txt"

    # Connect to the Cloud Storage API
    client = storage.Client()

    # Read the contents of the first file
    bucket = client.bucket(bucket_name)
    blob_1 = bucket.blob(file_name_1)
    file_contents_1 = blob_1.download_as_string()
    blob_2 = bucket.blob(file_name_2)
    file_contents_2 = blob_2.download_as_string()
    blob_3 = bucket.blob(file_name_3)
    file_contents_3 = blob_3.download_as_string()
    blob_4 = bucket.blob(file_name_4)
    file_contents_4 = blob_4.download_as_string()


    return [file_contents_1.decode(),file_contents_2.decode(),file_contents_3.decode(),file_contents_4.decode()]
    

