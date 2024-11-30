from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# database connection and configuration
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db= SQLAlchemy(app)


# creating database model
class todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"        

#  implementing create/read operations
@app.route('/',methods=['POST','GET'])
def index_page():  
    if request.method=='POST':
        title=(request.form['title'])
        desc=(request.form['desc'])
        data = todo(title=title,desc=desc)
        db.session.add(data)
        db.session.commit()
    all_data = todo.query.all()
    return render_template('index.html',all_data=all_data)

# implementing update operation
@app.route('/update/<int:sno>',methods=['POST','GET'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        all_data = todo.query.filter_by(sno=sno).first()
        all_data.title = title
        all_data.desc = desc
        db.session.commit()
        return redirect('/')
    all_data = todo.query.filter_by(sno=sno).first()
    return render_template('update.html', all_data=all_data)

# implementing delete operation
@app.route('/Delete/<int:sno>')
def delete(sno):
    all_data = todo.query.filter_by(sno=sno).first()
    db.session.delete(all_data)
    db.session.commit()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
