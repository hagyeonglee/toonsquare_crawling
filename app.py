from flask import *
import pandas as pd
import numpy as np
app = Flask(__name__)


@app.route('/')
def make_read_csv():
    data = pd.read_csv('naver_webtoon_comments.csv')
    data.set_index(["Unnamed: 0"],inplace=True)
    data.index.name=None
    Sentence = data.Sentence
    Emotion = data.Emotion
    return render_template('view.html',tables=[data.to_html()])


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
