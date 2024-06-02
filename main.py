"""
title           : main.py (client)
description     : This is the client API file which will deploy docker container with given image and ports.
date            : 2024/05/31
version         : 0.1
python_version  : 3.8

@author: Suchitra Kadolkar
"""

from fastapi import FastAPI
import uvicorn
import docker


client_app = FastAPI()

@client_app.post('/api/endpoint')
async def docker_deploy(data: dict):
    client = docker.from_env()
    image = client.images.pull(data['image_url'])
    container = client.containers.run(image, ports={f"{data['iport']}/tcp": f"{data['hport']}"}, detach=True, command = 'sleep 10')
    return {"message": f"Docker container is running successfully {container}"}


if __name__ == "__main__":
    uvicorn.run(client_app, host="0.0.0.0", port=8001) 