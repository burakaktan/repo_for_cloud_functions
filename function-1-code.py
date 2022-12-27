from google.cloud import storage
import uuid
import json 

def hello_world(request):
    user_uuid = str(uuid.uuid4())
    # Get the request parameters
    string1 = request.args.get('text1')
    string2 = request.args.get('text2')
    d = {
        "uuid": user_uuid,
        "text1": string1,
        "text2": string2
    }
    json_string = json.dumps(d)
    # Create a client for interacting with Google Cloud Storage
    storage_client = storage.Client()
    
    # Get the bucket where the files will be stored
    bucket = storage_client.bucket("storage_for_text2")
    
    # Write string1 to a file called "file1.txt"
    file1 = bucket.blob(user_uuid + ".txt")
    file1.upload_from_string(json_string)
    
    # Return a response indicating that the strings were written to GCS
    return "Your uuid is: " + user_uuid
