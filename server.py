"""
title           : server.py (server)
description     : This is the server API file which will take input from user in th form of HTML Form 
                  and then save data to database and after that call client API to deploy the docker container.
date            : 2024/05/31
version         : 0.1
python_version  : 3.8

@author: Suchitra Kadolkar
"""

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from databases import Database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from fastapi import FastAPI, HTTPException
import httpx

# Create a FastAPI app instance
app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./deploydocker.db"
database = Database(DATABASE_URL)
metadata = MetaData()

# Define a table for storing form data
forms = Table(
    "forms",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("image_url", String),
    Column("iport", Integer),
    Column("hport", Integer),
)
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

# HTML form
html_form = """
<form method="post">
    <label for="image_url">Docker Image URL:</label><br>
    <input type="text" id="image_url" name="image_url"><br>
    <label for="i_port">Internal Port:</label><br>
    <input type="number" id="i_port" name="iport"><br>
    <label for="h_port">Host Port:</label><br>
    <input type="number" id="h_port" name="hport"><br><br>
    <button type="submit">Submit</button>
</form>
"""

# Endpoint to serve the form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return html_form

# Endpoint to handle form submission
@app.post("/")
async def submit_form(image_url: str = Form(...), iport: int = Form(...), hport: int = Form(...)):
    query = forms.insert().values(image_url=image_url, iport=iport, hport=hport)
    await database.execute(query)
    result = await send_data_to_client_api(image_url, iport, hport)
    print(result)
    return {"message": "Form submitted successfully"}


@app.post("/send_data_to_client_api")
async def send_data_to_client_api(image_url, iport, hport):
    client_api_url = "http://localhost:8001/api/endpoint"
    
    async with httpx.AsyncClient() as client:
        try:
            # Make a POST request to the client API with the data
            response = await client.post(client_api_url, json={'image_url': image_url, 'iport': iport, 'hport': hport}, timeout=90)
            # Check if the request was successful

            if response.status_code == 200:
                return {"message": "Docker container is deployed successfully using client API"}
            else:
                raise HTTPException(status_code=response.status_code, detail="Failed to send data to client API")
            
        except Exception as e:
            print("Error occurred")
