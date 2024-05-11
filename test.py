import streamlit as st
import requests
from bs4 import BeautifulSoup
import string

def get_wikipedia_data(keyword):
    url = "https://en.wikipedia.org/wiki/" + keyword
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    infobox = soup.find('table', {'class': 'infobox'})
    if infobox:
        details = {}
        rows = infobox.find_all('tr')
        for row in rows:
            heading = row.find('th')
            detail = row.find('td')
            if heading and detail:
                details[heading.text.strip()] = detail.text.strip()
        return details
    else:
        return None

def main():
    st.title("Know more about your word")
    input_data = st.text_input("Enter your word:")
    if input_data:
        keyword = "_".join(input_data.split()).capitalize()
        wiki_data = get_wikipedia_data(keyword)
        if wiki_data:
            st.write("###  {}".format(keyword))
            for key, value in wiki_data.items():
                st.write("**{}:** {}".format(key, value))
        else:
            st.write("No Wikipedia infobox found for {}".format(keyword))

if __name__ == "__main__":
    main()
