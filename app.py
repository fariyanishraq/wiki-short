from bs4 import BeautifulSoup
import streamlit as st
import requests


if __name__ == "__main__":
    bs = BeautifulSoup
    st.header('Wiki Short')
    input = st.text_input(label='Search Topic',
                          placeholder='what do you like to know?')
    # Show warning message if input is empty
    if not input:
        st.info('write only name of the topic. Ignore question such as what is etc.')
        st.markdown("""
          ### Limitations of the Wikipedia Short app:

         - Search term accuracy: The app searches for the exact search term entered by the user on Wikipedia. If the search term is not accurate or misspelled, the app may not be able to find the correct Wikipedia page.

         - Language support: The app only supports English Wikipedia pages. It may not work for pages in other languages.

         - Parsing limitations: The app uses Beautiful Soup to parse the HTML content of the Wikipedia page. Some pages may have complex HTML structures that may not be parsed accurately by Beautiful Soup, leading to missing or incorrect information.

         - Content limitations: The app only displays the first two paragraphs of the Wikipedia page. If the information required by the user is not contained in these paragraphs, they may need to visit the full Wikipedia page.

         - Connection errors: The app requires an internet connection to fetch data from Wikipedia. If there are connectivity issues, the app may not work as intended.
        """)

    else:
        # wikipedia url
        url = f'https://en.wikipedia.org/wiki/{input}'
        response = requests.get(url)
        html_content = response.content
        # parser
        parser = bs(html_content, 'html.parser')
        # extract parser
        paragraph = [p.text for p in parser.find_all('p')[:2]]
        text = ''
        for p in paragraph:
            text += p + '\n\n' if p else ''
        st.markdown(f'{text}')
