# FastAPI

I have created basic application using FastAPI in which server sends data to client by calling client's API.
Basically, It take user input as docker image url, internal and host ports to expose.
This data is saved to sqlite database and also sent to client, then client will pull the docker image and deploy the container.
After that, i have integrated ngrok to expose the localhost service to the internet.
