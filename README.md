# repo_for_cloud_functions

The most important one is "function-cpu", similarity calculation is done there

*function-cpu* is the Cloud Function where plagiarism check is done. We are comparing metrics of the function with Cloud Run.

*function-cpu-2* is the function triggering both function-cpu and cloud run

*function-1* is where user first interacts with the system and receives a UUID (universally unique identifier).

*function-returning-result2* is where user gives the uuid and returns similarity score and run time of cloud run and cloud functions
