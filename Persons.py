# -*- coding: utf-8 -*-#
"""
Created on Sat May  6 18:49:31 2023

@author: vaish
"""


import os
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Sequence, ForeignKey

os.getcwd()

os.chdir("C://Users//vaish\Documents//vamsi//Project2")

app = Flask(__name__) #

basedir = os.path.abspath(os.path.dirname(__file__))
#basedir = os.path.abspath(os.getcwd())


app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir,'test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#db.create_all()

#db.init_app(app)



# a = {'111111' : 'N@gesh92', '111112' : 'Justin@2022', '111113' : 'Kevin1991@',
#             '111114' : 'Charles@23', '111115': 'Marcus@1448', '111116' : 'Sylvester@70',
#             '111117' : 'Judi@201992'}


class Persons(db.Model):
    person_id = db.Column(db.Integer,Sequence("per_id_seq"),nullable = False,primary_key = True)
    firstname = db.Column(db.String(100),nullable = False)
    lastname = db.Column(db.String(100),nullable = False)
    Gender = db.Column(db.String(50),nullable = False)
    age = db.Column(db.Integer,nullable = False)
    
    def __repr__(self):
        return "<Persons(person_id ='%s', firstname = '%s', lastname = '%s', Gender = '%s',age = '%s')>" % (
                                self.person_id,
                                self.firstname,
                                self.lastname,
                                self.Gender,
                                self.age
                                )

p1 = Persons(person_id =1,firstname = "Vamsi Nagesh",lastname = "P",Gender = "Male",age =30)
p1.firstname


#   db.session.add_all
#     (
#      [
    
#     Persons(firstname = 'Vamsi Nagesh',lastname = 'Pemmaraju',Gender ='Male',Age =30,username = 111111),
#     Persons(firstname = 'De Villiers',lastname = 'Abraham Benjamin',Gender ='Male',Age =37,username = 111112),
#     Persons(firstname = 'Magnussen',lastname = 'Kevin',Gender ='Male',Age =32,username = 111113),
#     Persons(firstname = 'Charles',lastname = 'Leclerc',Gender ='Male',Age =30,username = 111114),
#     Persons(firstname = 'Marcus',lastname = 'Stoinnis',Gender ='Male', Age =29, username = 111115),
#     Persons(firstname = 'Sylvester',lastname = 'Stallone',Gender ='Male',Age =70,username = 111116),
#     Persons(firstname = 'Judi',lastname = 'Dench',Gender ='Female',Age =68,username = 111117),
    
#     ]
    
#     )


@app.route("/")
def home_world():
    return render_template('home.html')


@app.route('/home', methods =['GET','POST'])
def home():
    global msg
    if request.method == 'POST':
        print(request.form['person_id'],request.form['firstname'],request.form['lastname'],request.form['Gender'],request.form['age'])
        
        #db.session.query().fiter(usernaem ==request.form['username'])


        instances = db.session.query(Persons).filter_by(person_id = request.form['person_id'])

        
        if len(instances.all())==0:
            p2 = Persons(person_id = request.form['person_id'],firstname = request.form['firstname'],lastname = request.form['lastname'],Gender = request.form['Gender'],age = request.form['age'])
            db.session.add(p2)
            db.session.commit()    
            
            msg = "Records successfully added"
        else:
            msg = "Records already exiists!"
            # return redirect(url_for('home'))

        
    return render_template('home.html',msg = msg)




if __name__ == "__main__":
    app.debug = True
    app.run()



