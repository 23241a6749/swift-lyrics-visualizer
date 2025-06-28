import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load .env token
load_dotenv()
GENIUS_API_TOKEN = os.getenv("GENIUS_API_TOKEN")

if not GENIUS_API_TOKEN:
    st.error("⚠️ Genius API token not found. Make sure .env is set up.")
    st.stop()

HEADERS = {"Authorization": f"Bearer {GENIUS_API_TOKEN}"}
BASE_URL = "https://api.genius.com"

# Function to search for song
def search_song(song_title):
    search_url = f"{BASE_URL}/search"
    params = {"q": song_title}
    response = requests.get(search_url, params=params, headers=HEADERS)
    if response.status_code != 200:
        return None
    data = response.json()
    hits = data["response"]["hits"]
    if not hits:
        return None
    return hits[0]["result"]["url"]

# Function to scrape lyrics
def scrape_lyrics_from_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    lyrics_divs = soup.find_all("div", attrs={"data-lyrics-container": "true"})
    lyrics = "\n".join([div.get_text(separator="\n") for div in lyrics_divs])
    return lyrics.strip()

# Function to generate word cloud
def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wc

# Streamlit UI
st.title("🎤 Taylor Swift Lyrics Visualizer")
st.write("Enter the title of a Taylor Swift song to fetch its lyrics and see a word cloud.")

song_title = st.text_input("🎵 Enter Song Title", placeholder="e.g. Love Story")

if song_title:
    with st.spinner("Fetching lyrics..."):
        url = search_song(song_title)
        if url:
            lyrics = scrape_lyrics_from_url(url)
            if lyrics:
                st.subheader("📜 Lyrics")
                st.text_area("Lyrics", lyrics, height=300)

                st.subheader("☁️ Word Cloud")
                wordcloud = generate_wordcloud(lyrics)
                fig, ax = plt.subplots()
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)
            else:
                st.error("⚠️ Could not extract lyrics.")
        else:
            st.error("❌ Song not found. Try a different title.")
