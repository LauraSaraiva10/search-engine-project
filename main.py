import streamlit as st
import numpy as np
import pandas as pd
import txtai

def load_data_and_embeddings_amazon():
    np.random.seed(1)
    df = pd.read_csv('data/amazon-data.csv')

    titles = df.dropna().sample(5905, replace=False).TITLE.values

    embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/all-MiniLM-L6-v2'
    })

    embeddings.load('embeddings/embeddings_amazon.tar.gz')

    return titles, embeddings

def show_ui_and_use_amazon_engine():

    titles, embeddings = st.cache_data(load_data_and_embeddings_amazon)()

    st.title('Amazon Item Search Engine')

    query = st.text_input('Enter a search query:', '')

    if st.button('Search'):
        if query:
            result = embeddings.search(query, 10)

            actual_results = [titles[x[0]] for x in result]

            for res in actual_results:
                st.write(res)
        else:
            st.write('Please enter a query')


def load_data_and_embeddings_seth():
    df = pd.read_csv('data/seth-data.csv').dropna()

    titles = df.title.values
    urls = df.url.values

    embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/paraphrase-mpnet-base-v2'
    })

    embeddings.load('embeddings/embeddings_seth.tar.gz')

    return titles, urls, embeddings

def show_ui_and_use_seth_engine():

    titles, urls, embeddings = st.cache_data(load_data_and_embeddings_seth)()

    st.title('Seth Blog Post Search Engine')

    query = st.text_input('Enter a search query:', '')

    if st.button('Search'):
        if query:
            result = embeddings.search(query, 10)

            actual_results = [f'Title: {titles[x[0]]}, URL: {urls[x[0]]}' for x in result]

            for res in actual_results:
                st.write(res)
        else:
            st.write('Please enter a query')

# Usage
show_ui_and_use_amazon_engine()
#show_ui_and_use_seth_engine()
