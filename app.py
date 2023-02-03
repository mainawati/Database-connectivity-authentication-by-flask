import pymysql


from flask import Flask,request,render_template,url_for

db_connection=None
db_cursor=None

app = Flask(__name__)

host="localhost"
name="root"
passwd=""
db_name="blog"
table_name = "details"

Connection = pymysql.Connection(
    host =host,
    user = name,
    password = passwd,
    db =db_name,
)

cur = Connection.cursor()
query ="select * from details"


print(query)

cur.execute(query)
output = cur.fetchall()

print('query output : ',output[0][1])

   
#API
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/demo_page',methods =['POST','GET'])
def demo():
    if request.method == 'POST':
        #return "mera bharat mahan"
        email = request.form['nm']
        password = request.form['mn']
        query = f"SELECT  * FROM details WHERE email='$email' AND password='$password'"
        cur.execute(query)
        print(cur.fetchone())

        if output[0][0] == email and output[0][1] == password:
            return "welcome to fetch data"+email+ " "+password
        else:
            return "*** email and password does not match***"
            cur.close() 
            return render_template("index.html")   
        # print(email)
        # print(password)

        # if email=="girija@gmail.com" and password=="giri12":
        #     print(True)
        #     return "welcome      "        +email + password
            
        # else:
        #     print(False)


            


        

            
    return render_template("demo_page.html")   

if __name__ == "__main__":
    app.run(debug=True)    
