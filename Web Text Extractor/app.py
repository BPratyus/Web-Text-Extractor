from flask import *
# import requests
# from bs4 import BeautifulSoup
from newspaper import Article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_text():
    text = ''
    title=''
    keywords=''
    if request.method == 'POST':
        url = request.form['url']
        article = Article(url,language="en")
        article.download()
        article.parse()
        article.nlp()
        title = article.title
        text=article.summary
        keywords=article.keywords

        # return render_template('text.html', text=text)
    return render_template('./index.html',title=title,text=text,keywords=keywords)

if __name__ == '__main__':
    app.run(debug=True)
