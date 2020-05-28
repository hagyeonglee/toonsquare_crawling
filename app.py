from flask import *
import pandas as pd
import csv

app = Flask(__name__)
listofemoji = []


@app.route('/<int:num>',methods=['GET','POST'])
def inputTest(num=None):
    dataf = pd.read_csv('naver_webtoon_comments.csv')
    num_row = len(dataf)
    s = pd.Series([index for index in range(1, num_row + 1)])
    dataf.set_index([s], inplace=True)
    dataf.index.name = None
    dataf = dataf.drop(['Unnamed: 0'], axis=1)
    dataf = dataf[(num-1)*15:num * 15]
    print(dataf.shape)
    render_template('test.html', num=num, num_row=num_row, tables=[dataf.to_html()])
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
        else:
            render_template('test.html', num=num,num_row=num_row, tables=[dataf.to_html()])
    elif request.method == "GET":
        print("GET")
    return render_template('test.html', num=num,num_row=num_row, tables=[dataf.to_html()])


@app.route('/calculate',methods=['GET','POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputTest', num=temp))


@app.route('/tohome', methods=['GET', 'POST'])
def showhome():
    if request.method=='POST':
        request.form["HOME"] == 'HOME'
    return redirect(url_for('make_read_csv'))


@app.route('/', methods=['GET', 'POST'])
def make_read_csv():
    data = pd.read_csv('naver_webtoon_comments.csv')
    num_row = len(data)
    s = pd.Series([index for index in range(1, num_row + 1)])
    data.set_index([s], inplace=True)
    data.index.name = None
    data = data.drop(['Unnamed: 0'], axis=1)
    print(data.shape)
    print(request.method)
    return render_template('view.html', row_num=num_row, tables=[data.to_html()])


@app.route('/result', methods=['GET', 'POST'])
def show():
    if request.method=='POST':
        request.form["toRESULT"] == 'toRESULT'
    return redirect(url_for('showResult'))


@app.route('/finalresult', methods=['GET', 'POST'])
def showResult():
    data = pd.read_csv('naver_webtoon_comments.csv')
    num_row = len(data)
    s = pd.Series([index for index in range(0, num_row)])
    data.set_index([s], inplace=True)
    data.index.name = None
    data = data.drop(['Unnamed: 0'], axis=1)

    data_emotion = pd.Series(listofemoji)
    num_row = len(data_emotion)
    data_emotion.index = [index for index in range(0, num_row)]
    data_emotion.index.name = None
    data_emotion = pd.DataFrame(columns=['supervised'], data=data_emotion)
    print(data_emotion)
    data['supervised'] = data_emotion['supervised']
    if request.method == "POST":
        if request.form['toCSV'] == 'submit':
            print('submit')
            data.reindex([index for index in range(0, num_row)])
            data.index.name = None
            data.to_csv('/home/ellie/Desktop/supervised.csv', sep=',', na_rep='NaN', quoting=csv.QUOTE_ALL)
            print('check csv file')
    return render_template('supervise.html', tables=[data_emotion.to_html()], datatables=[data.to_html()])

# 개별 데이터를 바꾸고 싶으면 사용자가 index 입력하고 supervise 데이터 입력해야함 -> 따로 페이지를 만들어야할 듯


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
