from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Summarization and sentiment analysis function
def summarize_articles(news_text):
    # Initialize the summarization and sentiment analysis pipelines
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    sentiment_analyzer = pipeline("sentiment-analysis")

    # Summarize the input text (news_text)
    summary = summarizer(news_text, max_length=130, min_length=30, do_sample=False)
    summarized_text = summary[0]['summary_text']

    # Analyze sentiment of the original text
    sentiment = sentiment_analyzer(news_text)
    sentiment_result = sentiment[0]['label']

    # Return the summary and sentiment result
    return summarized_text, sentiment_result

# Home route to render the index.html page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission for summarization and sentiment analysis
@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        news_text = request.form['news_text']  # Get the news text from the form

        # Call the summarize_articles function
        summary, sentiment = summarize_articles(news_text)

        # Return the rendered template with the results
        summaries = {
            'summary': summary,
            'sentiment': sentiment
        }

        return render_template('index.html', summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)