from bs4 import BeautifulSoup
import requests
import pdb

# Ask user to input any term which we will search on bing
search = input("Search for:")

# params will be appended into our url like ?q=<search_term>
params = {"q": search}

# Get response from this url
r = requests.get("https://www.bing.com/search", params=params)

# status_code should be 200 if the requests.get worked
print("requests returned status_code", r.status_code)
print("r.url = ", r.url)
# print("r.text =", r.text)

# Before being able to use the response, we need to parse it, the thing we get after parsing it, we call soup.
soup = BeautifulSoup(r.text, "html.parser")
print("soup mil gaya")
# Find an ordered list in our soup with the id b_results, the ordered list contains any attributes you're looking for
results = soup.find("ol", {"id": "b_results"})
print("results mil gaye")
# Find all the lists in results with the class b_algo and store it in a list called links
links = results.findAll("li", {"class": "b_algo"})
print("links mil gayein:", links)
# Loop over links
for item in links:

    print("mein loop mein hun")
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    print("Looping over links")

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print("Parent:", item.find("a").parent)

        children = item.find("h2")
        print("Next Sibling of the h2:", children.next_sibling)
