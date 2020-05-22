from flask import *
import pandas as pd

import numpy as np
import sys
from IPython.display import display, HTML
import ipywidgets as widgets

app = Flask(__name__)
listofemoji = []
@app.route('/',methods=['GET','POST'])
def make_read_csv():
    data = pd.read_csv('naver_webtoon_comments.csv')
    num_row = len(data)
    s = pd.Series([index for index in range(1, num_row + 1)])
    data.set_index([s], inplace=True)
    data.index.name = None
    data = data.drop(['Unnamed: 0'], axis=1)
    print(data.shape)
    print(request.method)
    render_template('view.html', row_num=num_row, tables=[data.to_html()])
    if request.method == "POST":
        if request.form['submit_button'] == "중립":
            # pass
            print("중립")
            listofemoji.append("중립")
            print(listofemoji)
        elif request.form['submit_button'] == "슬픔":
            # pass
            print("슬픔")
            listofemoji.append("슬픔")
            print(listofemoji)
        elif request.form['submit_button'] == "기쁨":
            # pass
            print("기쁨")
            listofemoji.append("기쁨")
            print(listofemoji)
        elif request.form['submit_button'] == "분노":
            # pass
            print("분노")
            listofemoji.append("분노")
            print(listofemoji)
        elif request.form['submit_button'] == "혐오":
            # pass
            print("혐오")
            listofemoji.append("혐오")
            print(listofemoji)
        elif request.form['submit_button'] == "공포":
            # pass
            print("공포")
            listofemoji.append("공포")
            print(listofemoji)
        elif request.form['submit_button'] == "놀람":
            # pass
            print("놀람")
            listofemoji.append("놀람")
            print(listofemoji)
        # else:
        #     return render_template('view.html', row_num=num_row, tables=[data.to_html()])
    elif request.method == "GET":
        print("get")
    return render_template('view.html', row_num=num_row, tables=[data.to_html()])



@app.route('/result',methods=['GET','POST'])
def result():
    # result = request.form
    return render_template('supervise.html',result=result)

@app.route('/test')
def test():
    # result = request.form
    return render_template('test.html')
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
