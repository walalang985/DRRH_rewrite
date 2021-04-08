from flask import Flask,redirect,url_for,render_template,request,session

app = Flask(__name__,static_folder='resources',template_folder='templates')
app.secret_key = 'qweqowieqweiodhjfskjkwelhrqjehlr1234231g1283490bbotgioybybiboyibioyboyboyboyboyboyboy'
@app.route('/')
@app.route('/<string:content>',methods=['GET', 'POST'])
def main(content='home'):
    return render_template('index.html',content=content)

@app.route('/action/<string:action>')
def action(action):
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True,port=8080)