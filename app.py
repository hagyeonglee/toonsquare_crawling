from flask import *
import pandas as pd

import numpy as np
import sys
from IPython.display import display, HTML
import ipywidgets as widgets

app = Flask(__name__)

@app.route('/')
def make_read_csv():
    data = pd.read_csv('naver_webtoon_comments.csv')
    num_row = len(data)
    s = pd.Series([index for index in range(1,num_row+1)])
    data.set_index([s], inplace=True)
    data.index.name = None
    data = data.drop(['Unnamed: 0'],axis=1)
    print(data.shape)
    try:
        import simplejson as json
    except (ImportError):
        import json
    # result = json.loads(json_string)
    return render_template('view.html',row_num=num_row, tables=[data.to_html()])

# @app.route('/')
# def load():
#     data = pd.read_csv('naver_webtoon_comments.csv')
#     num_row = len(data)
#     render = render_template('supervise.html',row_num=num_row)
#     print(type(render))
#     print(render)
#     tables= pd.read_html(render)
#     print(len(tables))
#     print(tables[0])
#     df = pd.DataFrame(tables[0])
#     print(df.shape)
#     return render_template('view.html',row_num=num_row,tables=[df.to_html()])



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
