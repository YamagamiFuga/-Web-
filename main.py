from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cal1') # 入力ページ
def cal1():

    return render_template('request.html')

@app.route("/calres1")
def calres1():
    var1 = request.args.get('val1', '0')
    var2 = request.args.get('val2', '0')
    v1 = int(var1)
    v2 = int(var2)
    a = str(v1+v2)
    
    return render_template('response.html', var1=var1, var2=var2,
a=a)