                                            # import necessary libraries
import asyncio                              # for asynchronous programming
from pyscript import document, when         # for using JS type functions and mapping Python to JS
from pyodide.http import pyfetch            # for making requests to the server
from json import loads, dumps               # for handling json

###############################################################

def display_response(response):
    '''Given a response from the server, display it on the 
    response container on the HTML page'''
    new_response = document.createElement("li")         # create a new element
    new_response.innerHTML = response                   # set the content INSIDE the element
    responses = document.getElementById("responses")    # get an existing element
    responses.appendChild(new_response)                 # add the new element to the DOM (which is a tree!) 

###############################################################
    
def create_table(data):
    # use your Python loop knowledge
    # remember: .keys(),   .items(),   .values()

    table = document.createElement("table")
    body = document.getElementsByTagName("body")[0]
    body.appendChild(table)
    row = document.createElement("tr")
    table.appendChild(row)
    this_data = document.createElement("td")
    row.appendChild(this_data)
    this_data.innerHTML = "some data"










###############################################################

async def search(some_data):
    '''An asynchronous function to send data to the server
    whenever needed'''

    result = await pyfetch(
        url="/api/books",
        method="GET",                                  # correct HTTP method goes here
        headers={"Content-Type": "application/json"},
        body = dumps(some_data)                         # convert to json
    )
    
    response = await result.json()                      # await a response - convert to Python dict

    print(f"Received a response: {response}")
    display_response(response["message"])

###############################################################

@when("click", "#search_btn")                                        # map a Python function to a HTML5 event.
def handle(event):
    data = document.getElementById("book_search").value     # extract some data from the DOM..
    print(data)
    asyncio.ensure_future(search(data))                # run your async function from the event handler

###############################################################