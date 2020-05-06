# SabudhHiringTask

# Project_Euler Problem 45
Firstly I tried list for saving all the pentagonal, hexagonal and triangle numbers. 
But the lists were not efficient enough. They were taking more than 7-8 minutes for saving the same.
Then I tried set and I was surprised that it took only a few seconds to save all the pentagonal, hexagonal  and triangle numbers to the set.

# Flask App

# Endpoints
There are 4 endpoints and the request methods for all the endpoints should be post method:
1. #####/create: 
Json should have the following keys. If you would provide less or more number of keys then it will print an error saying that "Only 4 values allowed" .The example is as shown:
{"id":2,"name":"Nitpreet Taneja","address":"Ludhiana","phone_number":1234567890}. This will create a new entry in both mysql and mongodb.


2. #### /update:
The only important field of json for this endpoint is id because we are updating the enteries on the basis of ids. Another field can be any field like address or name or phone_number or combination of some/all.
The example is as shown:
{"id":3, "address":"Chandigarh"}
It will update the record with id 3 in mongo and  mysql simultaneously.


3. ##### /delete:
The user has to provide only the id of the record. The example is :
{"id":3}
It will delete the record with id 3 from mongo and  mysql simultaneously.

4. ####/detect_prime:
The user will have to provide the number greater than 1 million.If the number provided is less than 1 million then it will return a statement saying enter the prime number greater than 1 million.
The example of the json file to be provided is as :
{"number": 15485863}
It will return a json saying whether the number is prime or not
