from flask import Flask, render_template
from dags.database_func import fetch_news_data
app = Flask(__name__)

@app.route('/')
def index():
    news = fetch_news_data()
    if news.empty:
        return "No news articles were found."
    return render_template('news.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)