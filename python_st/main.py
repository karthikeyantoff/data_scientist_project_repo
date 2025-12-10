# from flask import Flask, render_template, request
# import mysql.connector 

# main= Flask(__name__)
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'root', 
#     'database': 'machi'
# }
# @main.route('/')
# def home():
#     return render_template('login.html')
# @main.route('/login', methods=['POST'])
# def login():
#     # 1. Get data from HTML
#     username_input = request.form['username']
#     password_input = request.form['password']

#     try:
#         # 2. CONNECT
#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#         cursor.execute(query, (username_input, password_input))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return f"<center><h1 style='color:blue'>Success! {username_input} has been saved to the Database.</h1></center>"
#     except mysql.connector.Error as err:
#         return f"Database Error: {err}"
# if __name__ == '__main__':
#     main.run(debug=True)


from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)
key={
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'machi'
}
@app.route('/')
def  home():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username_input=request.form['username']
    password_input=request.form['password']

    try:
        con=mysql.connector.connect(**key)
        cursor=con.cursor()
        query="insert into  users(username,password) values (%s,%s)"
        cursor.execute(query,(username_input,password_input))
        con.commit()
        cursor.close()
        con.close()
        return '<h1>logon success fullt</h1>'
    except mysql.connector.Error as err:
        return f"database error:{err}"
if __name__=='__main__':
    app.run(debug=True)



