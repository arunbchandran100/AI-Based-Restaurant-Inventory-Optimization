import requests
from bs4 import BeautifulSoup
import concurrent.futures

city = "bangalore"
locality = "whitefield"
place = locality + " " + city
preference = "S"
rescom = "R"
format_type = "APP"
search_type = "COWORKING"
page_name = "homePage"
platform = "DESKTOP"

url = f"https://s.99acres.com/api/autocomplete/suggest?term={place}&PREFERENCE={preference}&RESCOM={rescom}&FORMAT={format_type}&SEARCH_TYPE={search_type}&CITY=&landmarkRequired=true&pageName={page_name}&platform={platform}"

response = requests.get(url)
data = response.json()

# Extract data from the first suggestion
first_suggestion = data['suggest'][0]
name = first_suggestion['NAME']
property_count = first_suggestion['PROPERTY_COUNT']
marker = first_suggestion['MARKER']
city1 = first_suggestion['CITY']
preference = first_suggestion['PREFERENCE']
rescom = first_suggestion['RESCOM']
e_type = first_suggestion['E_TYPE']

# Replace spaces with hyphens in the place name
name = name.replace(" ", "-")

# Constructing the URL
base_url = "https://www.99acres.com/search/property/buy/"

if e_type == "City":
    url_99acres = f"{base_url}{name.lower()}?city={city1}&preference={preference}&area_unit=1&res_com={rescom}"
else:
    locality_id = marker.split("_LOCALITY_")[-1]
    url_99acres = f"{base_url}{name.lower()}?city={city1}&locality={locality_id}&preference={preference}&area_unit=1&res_com={rescom}"

print("Constructed URL for 99acres:", url_99acres)


def scrape_listing(listing):
    project_name_element = listing.find("a", class_="projectTuple__projectName")
    project_name = project_name_element.get_text(strip=True)

    price_element = listing.find("span", class_="configurationCards__srpPriceHeading")
    price = price_element.get_text(strip=True)

    location_element = listing.find("h2", class_="projectTuple__subHeadingWrap body_med ellipsis")
    location = location_element.get_text(strip=True)

    link_element = listing.find("a", class_="projectTuple__projectName")
    link = link_element["href"]

    details_response = requests.get(link)
    details_soup = BeautifulSoup(details_response.content, "lxml")

    usp_description_element = details_soup.find('span', class_='caption_subdued_medium configurationCards__cardAreaSubHeadingOne')
    if usp_description_element:
        sq_foot_range = usp_description_element.get_text(strip=True)
    else:
        sq_foot_range = "N/A"

    image_elements = details_soup.find_all('div', class_='PhotonCard__photonDisp')
    image_urls = [img.find('img')['src'] for img in image_elements]

    return {
        "Title": project_name,
        "Price": price,
        "Location": location,
        "More details Link": link,
        "Square Footage": sq_foot_range,
        "Image Links": image_urls
    }


response = requests.get(url_99acres)
soup = BeautifulSoup(response.content, "lxml")
listings = soup.find_all("div", class_="projectTuple__descCont")

scraped_data = []

# Create a ThreadPoolExecutor with a specified number of workers
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    # Submit scraping tasks to the executor in parallel
    futures = [executor.submit(scrape_listing, listing) for listing in listings]

    # Process the scraped results as they complete
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        scraped_data.append(result)
        # Print or process the scraped result as needed
        #print(result)
        #print()

# Print the final scraped data
print("Scraped Data:", scraped_data)