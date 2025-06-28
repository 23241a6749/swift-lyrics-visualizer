# 🎤 Taylor Swift Lyrics Visualizer

An interactive Streamlit app that fetches lyrics for Taylor Swift songs and displays a word cloud of the most used words.

## 🚀 Live App

👉 [Click to view the deployed app]https://swift-lyrics-visualizer-sctpb24yqtgdztr9chex5v.streamlit.app/


## 📸 Screenshot

![image](https://github.com/user-attachments/assets/63551d99-e3df-48b1-aae8-4e8387e78c8c)


## ✨ Features

- Search any Taylor Swift song
- Fetch lyrics from Genius.com using the Genius API
- Display full lyrics in a readable format
- Generate a dynamic word cloud
- Works on both local and deployed environments

## 🛠 Tech Stack

- Python
- Streamlit
- Genius API
- BeautifulSoup (for web scraping)
- WordCloud + Matplotlib
- dotenv (for secure token access)

## 🧪 How to Run Locally

```bash
git clone https://github.com/23241a6749/swift-lyrics-visualizer.git
cd swift-lyrics-visualizer
pip install -r requirements.txt
```

Create a `.env` file with:

```env
GENIUS_API_TOKEN=your_genius_token_here
```

Then run:

```bash
streamlit run app.py
```

## 🔐 Deployment Notes

If you're using [Streamlit Cloud](https://streamlit.io/cloud):

- Add `GENIUS_API_TOKEN` under **Secrets**.
- No need to upload `.env`.

## 📄 License

MIT License
