from flask import *
from database import *

blogger=Blueprint('blogger',__name__)

@blogger.route('/bloghome')
def blohome():
    return render_template('bloghome.html')


@blogger.route('/manageblog',methods=['get','post'])
def userblog():
    	
	data={}


	if 'submit' in request.form:
		bl=request.form['blog']
		pa=request.form['path']

		q="INSERT INTO `blog1` VALUES(NULL,'%s','%s','%s',curdate(),'Pending')"%(session['bid'],bl,pa)
		insert(q)

	if 'action' in request.args:
		action=request.args['action']
		blog_id=request.args['id']
	
	else:
		action=None

	if action=='delete':
		q="delete from blog1 where blog_id='%s'"%(blog_id)
		delete(q)
		return redirect(url_for('blogger.userblog'))

	if action=='update':
		q="SELECT * from blog1 WHERE blog_id='%s'"%(blog_id)
		res=select(q)
		data['up']=res

	if 'update' in request.form:
		bl=request.form['blog']
		pa=request.form['path']
		q="UPDATE `blog1` SET `blog` ='%s',`path`='%s' WHERE `blog_id`='%s'"%(bl,pa,blog_id)
		update(q)
		return redirect(url_for('blogger.userblog'))

	q="SELECT * from blog1 WHERE blogger_id='%s'"%(session['bid'])
	data['view']=select(q)
    
	return render_template('blogermngblogs.html',data=data)



@blogger.route("/viewcmt",methods=['get','post'])
def viewcmt():
		data={}
		q="select * from blog1 inner join comment using(blog_id) inner join user using(user_id)"
		data['view']=select(q)
		return render_template("blogviewcmnt.html",data=data)


@blogger.route("/sendcomp", methods=['get', 'post'])
def secomp():
		data = {}
		q="select * from complaint where sender_id='%s'"%(session['bid'])
		print(select(q))
		data['viw']=select(q)
		if 'Add' in request.form:
				complaint = request.form['comp']
				q = "INSERT INTO `complaint`(`complaint_id`,`sender_id`,`complaint`,`reply`,`date`) VALUES(NULL,'%s','%s','%s',now())" % (session['bid'], complaint, 'Pending')
				insert(q)
				return redirect(url_for('blogger.secomp'))
		return render_template('sendcomp.html',data=data)



@blogger.route("/viewrep", methods=['get', 'post'])
def user_view_reply():
    if not session.get("lid") is None:
        data = {}
        coid=request.args['compl_id']
        qr = "SELECT * FROM complaint WHERE complaint_id='%s'"%(coid)
        data['view'] = select(qr)

    return render_template("viewreply.html", data=data)
		

@blogger.route("/viewprof", methods=['get', 'post'])
def viewpro():
		
		data = {}
		qr = "SELECT * FROM blogger WHERE blogger_id='%s'"%(session['bid'])
		data['vie'] = select(qr)
		return render_template('blogviewpro.html',data=data)
