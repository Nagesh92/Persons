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

os.chdir("D://work")

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
                                self.age,
                                )

p1 = Persons(person_id =1,firstname ="Vamsi Nagesh", lastname = "P",Gender = "Male",age =30)
p1.firstname

# p2 = Persons(person_id =2,firstname = 'De Villiers',lastname = 'Abraham Benjamin',Gender ='Male',age =37),
# p3 = Persons(person_id =3,firstname = 'Magnussen',lastname = 'Kevin',Gender ='Male',age =32),
# p4 = Persons(person_id =4,firstname = 'Charles',lastname = 'Leclerc',Gender ='Male',age =30),
# p5 = Persons(person_id =5,firstname = 'Marcus',lastname = 'Stoinnis',Gender ='Male', age =29),
# p6 = Persons(person_id =6,firstname = 'Sylvester',lastname = 'Stallone',Gender ='Male',age =70),
# p7 = Persons(person_id =7,firstname = 'Judi',lastname = 'Dench',Gender ='Female',age =68),

# db.session.add(p2)
# db.session.add(p3)
# db.session.add(p4)
# db.session.add(p5)
# db.session.add(p6)
# db.session.add(p7)

# db.session.comm





# 
# db.session.add_all(
#       [
    
#      Persons(person_id =1,firstname = 'Vamsi Nagesh',lastname = 'Pemmaraju',Gender ='Male',age =30),
#      Persons(person_id =2,firstname = 'De Villiers',lastname = 'Abraham Benjamin',Gender ='Male',age =37),
#      Persons(person_id =3,firstname = 'Magnussen',lastname = 'Kevin',Gender ='Male',age =32),
#      Persons(person_id =4,firstname = 'Charles',lastname = 'Leclerc',Gender ='Male',age =30),
#      Persons(person_id =5,firstname = 'Marcus',lastname = 'Stoinnis',Gender ='Male', age =29),
#      Persons(person_id =6,firstname = 'Sylvester',lastname = 'Stallone',Gender ='Male',age =70),
#      Persons(person_id =7,firstname = 'Judi',lastname = 'Dench',Gender ='Female',age =68),
    
#      ]
    
#      )


@app.route("/")
def home_world():
    return render_template('home.html')


@app.route('/home', methods = ['GET','POST'])
def home():
    msg = ['Records successfully added','Records already exists']
    if request.method == 'POST':
        print(request.form['person_id'],request.form['firstname'],request.form['lastname'],request.form['Gender'],request.form['age'])
        
        instances = db.session.query(Persons).filter_by(person_id = request.form['person_id'],
                                                        firstname =request.form['firstname'],
                                                        lastname = request.form['lastname'],
                                                        Gender = request.form['Gender'],
                                                        age = request.form['age'])

        if len(instances.all())==0:
            p2 = Persons(person_id = request.form['person_id'],firstname = request.form['firstname'],lastname = request.form['lastname'],Gender = request.form['Gender'],age = request.form['age'])
            db.session.add(p2)
            db.session.commit()            

            msg = 'Records Successfully Added'

        else:            
            msg = 'Records Already exists'
             # return redirect(url_for('home'))   
    

    return render_template('home.html',msg = msg)




if __name__ == "__main__":
    app.debug = True
    app.run()



