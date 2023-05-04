from flask import *
from newspaper import Article

import spacy
from spacy import displacy
nlp=spacy.load('en_core_web_sm')
from flaskext.markdown import Markdown

# model = load_model(r'D:\VIT\Sem 6\NLP Lab\Web Text Extractor\Web Text Extractor\nerlstm.h5')
# model.summary()
app = Flask(__name__)
Markdown(app)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem;">{}</div>"""

@app.route('/', methods=['GET', 'POST'])
def get_text():
    text = ''
    title=''
    result=''
    if request.method == 'POST':
        url = request.form['url']
        article = Article(url,language="en")
        article.download()
        article.parse()
        article.nlp()
        title = article.title
        text=article.text
        docx = nlp(text)
        html = displacy.render(docx,style='ent')
        html=html.replace("\n\n","\n")
        result = HTML_WRAPPER.format(html)
        

        # return render_template('text.html', text=text)
    return render_template('./index.html',title=title,text=text,result=result)

if __name__ == '__main__':
    app.run(debug=True,port=80)
