# Anecdotes-API Tutorial

## How to use Anecdotes-API?

The URL to the API's server is: https://anecdotes-task.herokuapp.com/

## About the project components:

This project contains several components:
1. **app.py** - This is the main component, it runs the API's endpoints.
2. **configuration.py** - This component contains the configurations data class ("Instructions") - for the parser, per each evidence.
3. **db_connection.py** - This is a context-manager, implemented as a class, responsible for creating the connection to the DB.
4. **storage.py** - This component contains the Storage class - responsible for adding and getting information from the DB.
* *The DB I use here is "Firestore" by Google Firebase*
* *The App runs as an image on Heroku free tier server, and using a gunicorn proxy*


The API's requests should:
---

1. For adding a new evidence, the request that should be sent is in POST method, to the endpoint https://anecdotes-task.herokuapp.com/add.
2. Parameters to evidence adding requests, should be delivered in JSON format only.
3. Headers should contain: "Content-Type: application/json"
4. For getting all the evidences, the request that should be sent is in GET method, to the endpoint https://anecdotes-task.herokuapp.com/get.
5. A mandatory parameter is "collection" - which specify the collection which we are about to retreive data from.
6. An optional parameter is "table" - which specify whether we'd like to receive the data in a HTML Table format.

## API's Methods:


1. **Insert an Evidence / Multiple Evidences:**

URL: https://anecdotes-task.herokuapp.com/add

The request should contain all the parameters that where described in the task in JSON format.


**Example**: *curl -X POST "https://anecdotes-task.herokuapp.com/add" -H "Content-Type: application/json" -d "{
   \"evidence_id\":1,
   \"evidence_data\":[
      {
         \"login_name\":\"anecdotes-exercise\",
         \"role\":\"owner\",
         \"user_details\":{
            \"updated_at\":\"2021-07-26T09:41:56Z\",
            \"id\":120000,
            \"email\":\"exercise@anecdotes.ai\",
            \"first_name\":\"anec\",
            \"last_name\":\"dotes\"
         },
         \"security\":{
            \"mfa_enabled\":true,
            \"mfa_enforced\":true
         }
      }
   ]}"*

A Valid Response: 
*{
    "count": 1,
    "message": "All evidences were successfully saved"
}*

**NOTE**: This type of evidence is described in the systen as "evidence_type_1", and may be seen and configured under the file configuration.py.
Any other type is also acceptable, but the configuration.py should be updated before that, as long as the function "_identify_and_parse" in parser.py.
  
2. **Get Evidences Data:**

  URL: https://anecdotes-task.herokuapp.com/get
  
  The request should contain a mandatory parameter, and may also contain an optional parameter.
  Parameters:
  1. "collection" (Mandatory) - This is the name of the collection in the DB, and related to the evidence type.
  You can find it in the file configuration.py, in the "collection" field which you may find under the relevent type.
  
  2. "table" (Optional) - This is an optional field that may parse the data into an HTML Table, instead a list of dicts.
  In case you want to trigger it, keep this field with a value.
  
   **TIP**: I strongly recommend to run this request from your browser, in order to see the HTML table.
  
  **Example**: *https://anecdotes-task.herokuapp.com/get?collection=evidence_type_1&table=1*
  
  A Valid Response: A HTML Table / List of dicts.
  
  
  

