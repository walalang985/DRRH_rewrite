from flask import Flask,redirect,url_for,render_template,request,session
import scripts

app = Flask(__name__,static_folder='resources',template_folder='templates')
app.secret_key = 'qweqowieqweiodhjfskjkwelhrqjehlr1234231g1283490bbotgioybybiboyibioyboyboyboyboyboyboy'
@app.route('/')
@app.route('/<string:content>',methods=['GET', 'POST'])
def main(content='home'):
    return render_template('index.html',content=content)

@app.route('/action/<string:action>')
def action(action):
    if action == 'register':
        email = request.form.get('email')
        passw = request.form.get('password')
        fullname = request.form.get('fullname')
        hotel = request.form.get('hotel')
        hash = cipher(cipher.HASH).exec(msg=email+passw+hotel+fullname)
        pub,priv = KeyGen(KeyGen.RSAKEY).generate()
        fer = KeyGen(KeyGen.FERKEY).generate()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True,port=8080)