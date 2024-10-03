# News Summarizer and Sentiment Analyzer using RAG

This project is a **News Summarizer and Sentiment Analyzer** that retrieves the latest news articles from the web, generates concise summaries using a pre-trained language model (LLM), and performs sentiment analysis to determine the tone of the articles.

## Features

- **News Retrieval**: Fetches the latest news articles based on a specific query (e.g., "AI", "Technology").
- **Text Summarization**: Generates concise summaries of the news articles using a pre-trained transformer model.
- **Sentiment Analysis**: Analyzes the sentiment of the summarized articles (Positive, Neutral, Negative).
- **Interactive Web Interface**: A simple and easy-to-use interface built with Streamlit for real-time interaction.
- **Article Retrieval**: Uses FAISS to implement a basic retrieval mechanism for querying relevant articles.

## Technology Stack

- **Python**: Programming language used to develop the backend logic.
- **Hugging Face Transformers**: Pre-trained models for text summarization.
- **Sentence-Transformers**: For document similarity and retrieval.
- **FAISS**: For fast similarity search and retrieval.
- **VADER (NLTK)**: For sentiment analysis of text.
- **NewsAPI or BeautifulSoup**: For retrieving news articles.
- **Streamlit**: For building the frontend UI.

## Project Structure

```
.
├── app.py                # Main application script
├── README.md             # Project documentation
├── requirements.txt      # Dependencies for the project
└── ...
```

## Installation

1. **Clone the repository:**

```
git clone https://github.com/your-username/news-summarizer.git
cd news-summarizer
```

2. **Create and active a virtual environment:**

```
python -m venv news-summarizer-env
source news-summarizer-env/bin/activate  # Linux/Mac
news-summarizer-env\Scripts\activate     # Windows
```

3. **Install the dependencies:**

```
pip install -r requirements.txt
```

4. **Obtain a NewsAPI key:**

Sign up at https://newsapi.org/ to get a free API key. You will need this to fetch the latest news articles.

## Usage

1. **Run the application:**

```
streamlit run app.py
```

2. **Using the application:**

- Enter your NewsAPI Key in the input box.
- Enter a search term (e.g., "AI", "Technology").
- Click "Summarize and Analyze" to retrieve news articles, generate summaries, and analyze sentiments.

The summarized articles along with their sentiment labels (Positive, Neutral, Negative) will be displayed, along with links to the full articles.

## Dependencies

- Python 3.7+
- Transformers by Hugging Face
- FAISS for similarity search
- VADER (NLTK) for sentiment analysis
- Sentence-Transformers for document embedding
- Streamlit for building the UI
- NewsAPI for fetching the news articles

## Requirements

You can install the required libraries using:

```
pip install -r requirements.txt
```

## Future Improvements

- **Advanced Filtering:** Add more options for filtering news articles (by date, source, etc.).
- **Multi-Language Support:** Extend the summarizer and sentiment analyzer to handle multiple languages.
- **Customization:** Allow users to choose between different summarization models or sentiment analysis techniques.

## License

This is an `open-source` project.