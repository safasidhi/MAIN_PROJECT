from flask import *
from database import *
from train import predict_spam

admin=Blueprint('admin',__name__)


@admin.route('/admhome')
def admin_home():
    return render_template('admhome.html')


@admin.route("/admviewuser",methods=['get','post'])
def viewuser():
		data={}
		q="select * from user"
		data['view']=select(q)
		return render_template("viewuser.html",data=data)


@admin.route("/admviewcmt",methods=['get','post'])
def viewcmt():
		data={}
		q="select * from blog1 inner join comment using(blog_id) inner join user using(user_id)"
		data['view']=select(q)
		return render_template("viewcmnt.html",data=data)

@admin.route("/admviewcomp",methods=['get','post'])
def viewcomp():
		data={}
		q="(SELECT complaint_id,sender_id,complaint,reply,date,fname,lname FROM complaint inner join user on complaint.sender_id=user.user_id) union (SELECT complaint_id,sender_id,complaint,reply,date,fname,lname FROM complaint inner join blogger on complaint.sender_id=blogger.blogger_id)"
		data['comp']=select(q)
		return render_template("viewcomp.html",data=data)
	
@admin.route("/admin_sendreply", methods=['get', 'post'])
def adm_serep():
        data = {}   
        compid=request.args['id']
        usid=request.args['userid']
        if 'send' in request.form:
            reply = request.form['rep']
            q = "UPDATE `complaint` SET `reply`='%s' WHERE `complaint_id`='%s'"%(reply,compid)
            insert(q)
            q="SELECT * FROM `complaint` WHERE `sender_id`='%s'"%(usid)	
            data['view']=select(q)
            return redirect(url_for('admin.viewcomp'))
        return render_template('sendrep.html',data=data)

@admin.route("/viewbl",methods=['get','post'])
def viewblog():
		data={}
		q="select * from blog1 inner join blogger using(blogger_id)"
		data['view']=select(q) 
		return render_template("adviewblog.html",data=data)

@admin.route("/detect_blog", methods=['POST'])  
def detect_blog():

    blog_id = request.args.get('id')

    blog_text = get_blog_text(blog_id)
    
    prediction_result = predict_spam(blog_text)
    print(prediction_result)
  
    return prediction_result

       
def get_blog_text(blog_id):
    query = "SELECT * FROM blog1 WHERE blog_id = '%s'" % (blog_id)
    res = select(query) 
    if res:
        if 'blog' in res[0]:
            blog_text = res[0]['blog']
            print(blog_text)
            return blog_text
    return None

