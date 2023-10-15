from flask import Blueprint, render_template, request, flash, redirect,url_for, Response
from flask_login import login_required, current_user
from . import db
import json
import face_recognition
import pickle
from . models import Gchild , Unknown, User
from flask_login import login_user, login_required, logout_user, current_user
import sys
import base64
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)



@views.route('/guardianForm',methods=['GET','POST'])
@login_required
def guardianForm():
    if request.method=='POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        lastloc = request.form.get('lastLoc')
        file = request.files['image']
        mimetype = file.mimetype
        i = file.read()
        im = face_recognition.load_image_file(file)
        encode = face_recognition.face_encodings(im)
        enc = pickle.dumps(encode) 
        
        child = Gchild(name=name,age=age,gender=gender,lastLoc=lastloc,img=i,encoding=enc,mimetype=mimetype,user_id=current_user.id,status=False)
        db.session.add(child)
        db.session.commit()
        return redirect(url_for('views.home',user=current_user))
    
    return render_template('guardianForm.html',user=current_user)


@views.route('/unknownForm',methods=['GET','POST'])
def unknownForm():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        locatn = request.form.get('locatn')
        img = request.files['image']
        mimetype = img.mimetype 
        i = img.read()
        im = face_recognition.load_image_file(img)
        unencode = face_recognition.face_encodings(im)[0]
        known_encodings= []
        known_id = []
        guardiandb = db.session.query(Gchild).all()
        for child in guardiandb:
            ch = child.encoding
            known_encodings.append(pickle.loads(ch)[0])
            known_id.append(child.id)
            #print(type(pickle.loads(ch)[0]),file=sys.stderr)
        matches = face_recognition.compare_faces(unencode,known_encodings)
        index = 0
        print(matches,file=sys.stderr)
        if True in matches:
            index = matches.index(True)+1
            print(index)
            found = Gchild.query.filter_by(id=index).first()
            unknown = Unknown(name=name,phone=phone,loc=locatn,img=i,mimetype=mimetype,guid=found.user_id)
            Gu = db.session.query(User).filter_by(id=found.user_id).first()
            found.status = True
            Gu.status = True
            db.session.add(unknown)
            db.session.commit()
            print(found.name,file=sys.stderr)
            return render_template('unknownForm.html',user=current_user,child=found.name,contact=Gu.phone)
        else:
            return redirect(url_for('views.unknownForm'))
    return render_template('unknownForm.html',user=current_user)

@views.route('/check_status',methods=['GET','POST'])
def check_status():
    user = db.session.query(User).filter_by(id=current_user.id).first()
    if user.status:
        unf= db.session.query(Unknown).filter_by(guid=current_user.id).first() 
        return render_template('check_status.html',user=current_user,name=unf.name,phone=unf.phone,location=unf.loc,status=user.status)
    else:
        return render_template('check_status.html',user=current_user)
    
@views.route('/get_image',methods=['GET','POST'])
def get_image():
    unf = db.session.query(Unknown).filter_by(guid=current_user.id).first()
    return Response(unf.img,mimetype=unf.mimetype)

# @views.route('/delete_entry',methods=['GET','POST'])
# def delete_entry():
#     child = db.session.query(Gchild).filter_by(id=current_user.id)
#     child.delete()
#     db.session.commit()
#     return render_template('home.html',user=current_user)

@views.route('/get_info',methods=['GET','POST'])
def get_info():
    if db.session.query(Gchild).filter_by(user_id=current_user.id).first():
        child = db.session.query(Gchild).filter_by(user_id=current_user.id).first()
        return render_template('get_info.html',user=current_user,name=child.name,age=child.age,gender=child.gender,last=child.lastLoc)
    else:
        flash('There is no entry linked to your profile',category='error')
        return redirect(url_for('views.home'))
    
@views.route('/getimage',methods=['GET','POST'])
def getimage():
    unf = db.session.query(Gchild).filter_by(user_id=current_user.id).first()
    return Response(unf.img,mimetype=unf.mimetype)