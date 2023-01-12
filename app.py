from flask import Flask, render_template,request,flash,redirect,url_for
import sqlite3
import sqlite3 as sql
import datetime

app = Flask(__name__)
app.secret_key="123"

#con=sqlite3.connect("database.db")
#con.execute("CREATE TABLE IF NOT EXISTS data(pid INTEGER PRIMARY KEY ,name TEXT,address TEXT,contact INTEGER,mail TEXT)")
#con.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_record')
def add_record():
    return render_template('add_record.html')

@app.route("/TRC_Amir",methods=["GET","POST"])
def TRC_Amir():
    if request.method=='POST':
            body = request.json
            payload = body['data']['payload']
            number = payload['from']['phone_number']
            text = payload['text']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("database.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("database.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("TRC_Amir.html",data=data)

@app.route("/TRC_LA",methods=["GET","POST"])
def TRC_LA():
    if request.method=='POST':
            body = request.json
            payload = body['data']['payload']
            number = payload['from']['phone_number']
            text = payload['text']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseLA.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("databaseLA.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("TRC_LA.html",data=data)

@app.route("/TRC_Liran",methods=["GET","POST"])
def TRC_Liran():
    if request.method=='POST':
            body = request.json
            payload = body['data']['payload']
            number = payload['from']['phone_number']
            text = payload['text']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseLiran.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("databaseLiran.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("TRC_Liran.html",data=data)

@app.route("/TRC_Seattle",methods=["GET","POST"])
def TRC_Seattle():
    if request.method=='POST':
            body = request.json
            payload = body['data']['payload']
            number = payload['from']['phone_number']
            text = payload['text']
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            if number:
                with sql.connect("databaseSeattle.db") as con:
                    cur = con.cursor()
                    cur.execute("INSERT INTO data (date,number,text) VALUES (?,?,?)",(date,number,text))
                return "Number:{} Text:{}".format(number, text)
            if not number:
                return "No Data"
    else:
                  con=sqlite3.connect("databaseSeattle.db")
                  con.row_factory=sqlite3.Row
                  cur=con.cursor()
                  cur.execute("SELECT * from data")
                  data=cur.fetchall()
                  con.close()
                  return render_template("TRC_Seattle.html",data=data)

@app.route('/delete_record/<string:id>')
def delete_record(id):
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("home"))
        con.close()

@app.route('/delete_record1/<string:id>')
def delete_record1(id):
    try:
        con = sqlite3.connect("databaseLA.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("home"))
        con.close()

@app.route('/delete_record2/<string:id>')
def delete_record2(id):
    try:
        con = sqlite3.connect("databaseLiran.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("home"))
        con.close()

@app.route('/delete_record3/<string:id>')
def delete_record3(id):
    try:
        con = sqlite3.connect("databaseSeattle.db")
        cur = con.cursor()
        cur.execute("DELETE FROM data where pid=?",(id))
        con.commit()
        flash("Record Deleted Successfully","success")
    except:
        flash("Record Delete Failed","danger")
    finally:
        return redirect(url_for("home"))
        con.close()

if __name__ == "__main__":
    app.run(debug=True) 