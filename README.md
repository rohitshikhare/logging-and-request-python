# logging-and-request-python

# Logging:

Levels of Log Message-

1) Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
2) Info : These are used to Confirm that things are working as expected.
3) Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future.
4) Error : This tells that due to a more serious problem, the software has not been able to perform some function.
5) Critical : This tells serious error, indicating that the program itself may be unable to continue running.

If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation.
Each built-in level has been assigned its numeric value.

  
    Level         Numeric value

    CRITICAL      50
    ERROR         40
    WARNING       30
    INFO          20
    DEBUG         10
    NOTSET         0
        

# HTTP Methods:
  REST APIs listen for HTTP methods like GET, POST, and DELETE to know which operations to perform
on the web service’s resources. A resource is any data available in the web service that can be
accessed and manipulated with HTTP requests to the REST API. The HTTP method tells the API which
action to perform on the resource.

      the five methods listed below are the most commonly used with REST APIs:
  
HTTP method     |    Description
----------------|-----------------------------------------
GET         	|  Retrieve an existing resource.
POST	        |  Create a new resource.
PUT	        |  Update an existing resource.
PATCH           |  Partially update an existing resource.
DELETE          |  Delete a resource.
----------------------------------------------------------
              


      Below is a list of the most common status codes returned by REST APIs:

   Code	  |   Meaning    	        |           Description
 ---------|-----------------------------|-----------------------------------------------------------------------------------
200	  |     OK	                |  	The requested action was successful.
201       |	   Created   	        |  	A new resource was created.
202	  |    Accepted	         	|  The request was received, but no modification has been made yet.
204       |	   No Content	       	|  The request was successful, but the response has no content.
400	  |    Bad Request	     	|  The request was malformed.
401	  |    Unauthorized	     	|  The client is not authorized to perform the requested action.
404	  |    Not Found	       	|  The requested resource was not found.
415	  |    Unsupported Media Type	|  The request data format is not supported by the server.	           
422	  |     Unprocessable Entity   	|  The request data was properly formatted but contained invalid or missing data.
500	  |   Internal Server Error   	|	The server threw an error when processing the request.
---------------------------------------------------------------------------------------------------------------------

      follwing are logging examples:
      logging_test.py
      example.log

      follwing are http methods examples:
      delete_method.py
      get_method.py
      post_method.py
      put_method.py
           
