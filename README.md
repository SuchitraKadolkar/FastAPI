For the given Python task I have created two python files as:
    1. server.py:
        This is the server API file in which I have created Sqlite db to store image_url, internal port and host port.
        After that I have created HTML Form to read these 3 values from user and also added submit button.
        Then localhost:8000 will call my get("/") API and it will display the form.
        When user clicks on "Submit", post("/") API is called which will save the details into the database and also call client API to deploy the container.
        When client API deploys container successfully it will display the success message.
        At last it will display form data successfully message also.

    2. main.py
        This is the client API file in which I have created the post("/api/endpoint") to deploy the docker container.
        It will simply pull the docker image and then deploy the container allowing mentioned ports.
        
requirements.txt - In this file I have listed the python packages that are required to be installed for this task.

Output images - I have added some screenshots after successful execution of the whole application using ngrok.
