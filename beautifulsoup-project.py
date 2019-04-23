""" scraping weather forecasts from the National Weather Service,
and then analyzing them using the Pandas library"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# download the page
page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat="
    "37.7772&lon=-122.4168#.XL7k5aKEa00")
# create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
# the div containing the forecast has id "seven-day-forecast"
seven_day = soup.find(id="seven-day-forecast")
# use css selectors to find all the periods, short descriptions, temperatures,
# and the description. Use list comprehension to return them
periods = [pt.get_text() for pt in
           seven_day.select(".tombstone-container .period-name")]
short_desc = [sd.get_text() for sd in
              seven_day.select(".tombstone-container .short-desc")]
temperature = [tp.get_text() for tp in
               seven_day.select(".tombstone-container .temp")]
descriptions = [d["title"] for d in
                seven_day.select(".tombstone-container img")]
# use DataFrame class to store the data in a table
weather = pd.DataFrame({
    "Periods": periods,
    "Short_desc": short_desc,
    "Temperature": temperature,
})
# find all the temperatures (integers) using the Series.str.extract method
temp_nums = weather["Temperature"].str.extract("(?P<temp_num>\d+)",
                                               expand=False)
weather["temp_num"] = temp_nums.astype('int')
# find the lows that happen at night
is_night = weather["Temperature"].str.contains("Low")
weather["is_night"] = is_night


