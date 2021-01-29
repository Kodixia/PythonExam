import requests

# Exercise 1

def getMovieTitles(title):
    # Setting the parameters for the requests as a dictionary
    title_params = {'Title': str(title)}
    # Establish the url api as a variable
    url = 'https://jsonmock.hackerrank.com/api/movies/search/'
    # Calling the sendRequest function and saving the value on a variable
    json_file = sendRequest(url,title_params)
    # Establish the number of pages and the current page to start
    current_page = json_file["page"]
    total_pages = json_file["total_pages"]
    # Create an empty array to return when the function finishes
    titles = []
    # Main loop that gets the data and the array of titles and then append the titles to the array 
    while ( current_page != (total_pages + 1)):
        title_params["page"]=str(current_page)
        json_response = sendRequest(url,title_params)
        json_data = json_response['data']
        for title_array in json_data:
            titles.append(title_array['Title'])
        current_page = current_page + 1 
    # Sort the array
    titles.sort()
    # Print the titles
    for title in titles:
        print(title)
    # return the title array list 
    return titles



def sendRequest(url,parameters):
    r = requests.get(url,params=parameters)
    return r.json()
