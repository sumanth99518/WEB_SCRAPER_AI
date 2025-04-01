import streamlit as st
from scraper import scrape_website, extract_body_content, clean_body_content, split_dom_content
from llms import parse_with_ollama
import re
st.title("Web Scraper")

with st.sidebar:
    choice = st.radio("Select an option", ["Upload file", "Upload URL"])
    st.info("Upload a file or a URL to scrape data from")

if choice == "Upload file":
    file = st.file_uploader("Upload a file", type=["html"])
    if file:
        body_content = extract_body_content(file)
        cleaned_body_content = clean_body_content(body_content)
        with st.expander("content"):
            st.text_area("Body content", cleaned_body_content, height=400)
        st.session_state.body_content = cleaned_body_content
        st.text_input("Enter the description of the data you want to scrape", key="parse_description")
        if st.button("Scrape data"):
            st.write("Scraping data...")
            chunks = split_dom_content(cleaned_body_content)
            st.session_state.result=parse_with_ollama(chunks,st.session_state.parse_description)
            if st.session_state.result:
                file=re.findall(r'</think>\s*```csv\n(.*?)```',st.session_state.result , re.DOTALL)
                output="".join(file).strip()
                print(output)
                st.text(output)
                with st.expander("output"):
                    st.text_area("output file",output,height=500)
                st.download_button(
                label="Download CSV",
                data=output,
                file_name="movie_data.csv",
                mime="text/csv"
                )

elif choice == "Upload URL":
    url =st.text_input("Enter the description of the data you want to scrape")
    file =scrape_website(url)
    print(file)
    if file:
        body_content = extract_body_content(file)
        cleaned_body_content = clean_body_content(body_content)
        with st.expander("content"):
            st.text_area("Body content", cleaned_body_content, height=400)
        st.session_state.body_content = cleaned_body_content
        st.text_input("Enter the description of the data you want to scrape", key="parse_description")
        if st.button("Scrape data"):
            st.write("Scraping data...")
            chunks = split_dom_content(cleaned_body_content)
            st.session_state.result=parse_with_ollama(chunks,st.session_state.parse_description)
            if st.session_state.result:
                file=re.findall(r'</think>\s*```csv\n(.*?)```',st.session_state.result , re.DOTALL)
                output="".join(file).strip()
                print(output)
                st.text(output)
                with st.expander("output"):
                    st.text_area("output file",output,height=500)
                st.download_button(
                label="Download CSV",
                data=output,
                file_name="movie_data.csv",
                mime="text/csv"
                )



