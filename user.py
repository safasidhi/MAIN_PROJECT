from flask import *
from database import *
from train import predict_spam

user=Blueprint('user',__name__)

@user.route('/ushome')
def user_home():
    return render_template('userhome.html')


@user.route("/usviewbl",methods=['get','post'])
def viewblog():
		data={}
		q="select * from blog1 inner join blogger using(blogger_id)"
		data['view']=select(q) 
		return render_template("viewblog.html",data=data)


@user.route("/detect_blog", methods=['POST'])
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


@user.route("/sendcmm", methods=['get', 'post'])
def sendcmm():
    if not session.get("lid") is None:
         data = {}
         if 'send' in request.form:
            comt = request.form['com']
            bid = request.args['id']
            q = "INSERT INTO `comment`(`comment_id`,`blog_id`,`comment`,`user_id`) VALUES(NULL,'%s','%s','%s')" % (bid, comt, session['uid'])
            insert(q)
    return render_template('sendcmnt.html',data=data)


@user.route("/usersendcomp", methods=['get', 'post'])
def secomp():
        data = {}
        q="select * from complaint where sender_id='%s'"%(session['uid'])
        data['vie']=select(q) 
        if 'Add' in request.form:
            complaint = request.form['comp']
            q = "INSERT INTO `complaint`(`complaint_id`,`sender_id`,`complaint`,`reply`,`date`) VALUES(NULL,'%s','%s','%s',now())" % (session['uid'], complaint, 'Pending')
            insert(q)
            return redirect(url_for('user.secomp'))  
        return render_template('user_send_comp.html',data=data)


@user.route("/user_viewrep", methods=['get', 'post'])
def user_view_reply():
    if not session.get("lid") is None:
        data = {}
        coid=request.args['compl_id']
        qr = "SELECT * FROM complaint WHERE complaint_id='%s'"%(coid)
        data['view'] = select(qr)

    return render_template("userviewreplies.html", data=data)   