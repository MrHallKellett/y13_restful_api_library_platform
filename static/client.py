                                            # import necessary libraries
import asyncio                              # for asynchronous programming
from pyscript import document, when         # for using JS type functions and mapping Python to JS
from pyodide.http import pyfetch            # for making requests to the server
from json import loads, dumps               # for handling json

###############################################################

# create a list of all sections
sections = [document.getElementById(f"{section}_section") for section in '''get_all_books
search_books
loan_book
add_new_book
delete_book'''.splitlines()]

################################################################

def hide_sections_except(this_section):
    for section in sections:
        print(section.id, "vs", this_section)
        if section.id != this_section:
            section.classList.add("hide_section")
        else:
            section.classList.remove("hide_section")

################################################################

def display_response(response: str):
    '''Given a response from the server, display it on the 
    response container on the HTML page'''
    new_response = document.createElement("li")         # create a new element
    new_response.innerHTML = response                   # set the content INSIDE the element
    responses = document.getElementById("responses")    # get an existing element
    responses.appendChild(new_response)                 # add the new element to the DOM (which is a tree!) 

################################################################

def display_all_books(books):
    '''Populates the table when the get all books button has been pressed'''
    table = document.getElementById("all_book_table")
    table.innerHTML = "" # reset the table
    body = document.getElementsByTagName("body")[0]
    body.appendChild(table)

    row = document.createElement("tr")
    table.appendChild(row)
    for key in books[0].keys():
        element = document.createElement("th")
        row.appendChild(element)
        element.innerHTML = key.title()
    
    
    for book in books:
        row = document.createElement("tr")
        table.appendChild(row)
        for field in book.values():
            element = document.createElement("td")
            row.appendChild(element)
            element.innerHTML = field
        

###############################################################

async def write_to_server(some_data: str):
    '''Example of POST request PyScript'''

    print(f"Using pyfetch to send {some_data} to server")
    result = await pyfetch(
        url="/example_server_url_route",
        method="POST",                                  # correct HTTP method goes here
        headers={"Content-Type": "application/json"},
        body = dumps(some_data)                         # convert to json
    )
    
    response = await result.json()                      # await a response - convert to Python dict

    print(f"Received a response: {response}")
    display_response(response["message"])

###############################################################

async def search_books(query):
    '''Search the database for a particular term'''


###############################################################

async def get_all_books():
    '''Retrieves all books from the database'''
    print(f"Fetching books")
    all_books_result = await pyfetch(
        url="api/books",
        method="GET"
    )
    all_books_response = await all_books_result.json()
    display_all_books(all_books_response)

###############################################################

@when("click", "button")                                                   # run the event handler for ALL buttons
def handle(event):
    btn_id = event.target.id
    section_to_show = btn_id.replace("_menu_btn", "_section")
    hide_sections_except(section_to_show)
    if section_to_show == "get_all_books_section":
        asyncio.ensure_future(get_all_books())                            # run your async function from the event handler
    
    if btn_id == "perform_search_btn":
        search_query = document.getElementById("search_book_input").value
        asyncio.ensure_future(search_books(search_query))                # run your async function from the event handler


###############################################################


