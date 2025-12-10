from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def method_name():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    # return f"<center><h1>wellcome,{username,password}!</h1></center>"h1>
    # return f"<center><h1>welcoem user</h1></


    if username=="admin"and password=="1234":
        return f"<h1>wellcome,{username}!</h1>"
    else:
        return "<h1>invalide</h1>"

if __name__=='__main__':
    app.run(debug=True)

# # from flask import Flask
# # app=Flask(__name__)
# # @app.route('/')
# # @app.route('/index')
# # def fun():
# #     return '<h1>karthikeyan home page</h1>'
# # @app.route('/about')
# # def about():
# #     return '<h1>karthikeyan about page<h1>'

# # if __name__=='__main__':
# #     app.run(debug=True)


