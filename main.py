from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cal1') # 入力ページ
def cal1():

    return render_template('request.html')

@app.route("/calres1", methods=['GET', 'POST'])
def calres1():
    
    var1 = 0.0
    var2 = 0.0
    
    if request.method=="GET":
        var1 = request.args.get('val1', '0')
        var2 = request.args.get('val2', '0')
        
    else:
        var1 = request.form.get('val1', '0')
        var2 = request.form.get('val2', '0')
        
        
    v1 = float(var1)
    v2 = float(var2)
    a = str(v1+v2)
    
    return render_template('response.html', var1=var1, var2=var2,
a=a)
    


@app.route("/cal2", methods=['GET', 'POST']) # 結果表示
def cal2():
    
    var1 = 0
    var2 = 0
    ans = "0"
    
    if request.method=="GET":
        var1 = None
    else:
        var1 = request.form.get('val1', "0")
        var2 = request.form.get('val2', "0")
        ans = str( float(var1) + float(var2) )
    
    return render_template('request.html', var1=var1, var2=var2, ans=ans)

@app.route("/cal3", methods=['GET', 'POST']) # 結果表示
def cal3():
    
    if request.method=="POST":
        
        if request.method=="GET":
            var1 = None
        else:
            var1 = request.form.get('val1', "0")
            var2 = request.form.get('val2', "0")
            name = request.form.get('name', "+")
        
        var1 = int(var1)
        var2 = int(var2)
        ans = "0"
    
        if name == '+':
            ans = var1 + var2
    
        elif name == '-':
            ans = var1 - var2
        
        elif name == '*':
            ans = var1 * var2
        
        elif name == '/':
            ans = var1 / var2
        
        return render_template('request.html', var1=var1, var2=var2, name=name, ans=ans)
    
    return render_template('request.html', var1='0', var2='0', name='+', ans="0")
    

if __name__ == '__main__':    
    app.debug = True
    app.run(host='localhost', port=8000)
