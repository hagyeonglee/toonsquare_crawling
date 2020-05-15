from flask import *
import pandas as pd
import numpy as np
import sys
from IPython.display import display, HTML
import ipywidgets as widgets

app = Flask(__name__)

click_list = []

button = widgets.Button(description='click')

@app.route('/')
def make_read_csv():
    data = pd.read_csv('naver_webtoon_comments.csv')
    data.set_index(["Unnamed: 0"],inplace=True)
    data.index.name = None
    num_row = len(data)
    #
    checkbox = widgets.Checkbox(description="emotion")
    # #supervise 열 추가
    # new_data = data.assign(supervise="none")
    display(checkbox)
    supervise = pd.DataFrame({'supervise': [checkbox for checkbox in range (1,num_row+1)]})
    # print(new_data.to_html())
    return render_template('view.html',tables=[data.to_html()],stables=[supervise.to_html()])


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
