from flask_security import login_required
from server_part.app import app
from server_part.database.tables import Post, Comment, Tag, comment_votes, post_votes
from flask import request
from server_part.database import db 
from flask import jsonify, g
from server_part.utils.misc import auth
from datetime import datetime



@app.route('/new_post', methods=['POST'])
@auth.login_required(role='common')
def new_post():
    new_post = Post(request.form['title'], request.form['post_text'], g.user.id) 
    try:
        tags_list = request.form['tegs'].lower().lstrip().rstrip().split('#')
        tags_list = tags_list[1:]
        print(tags_list)
        for tag in tags_list:
            try:
                get_tag = Tag.query.filter_by(name = tag).first()  # get tag from database if exist
                tag_id = get_tag.id # get tag id if exist or add new tag to database
                t = get_tag
                new_post.tag.append(t)
                db.session.add(new_post)
                
            except AttributeError:
                t = Tag(tag)
                new_post.tag.append(t)
                db.session.add(new_post)           
    except:
        db.session.add(new_post)
    db.session.commit()
    time = datetime.now()
    return jsonify({ 'Action': '%s made a post with the title "%s"' %(g.user.username, request.form['title']),
                    'Time': f'{time.ctime()}'})


# requests.post('http://localhost:5000/new_post', auth=HTTPBasicAuth('username', 'pass'), data={'title': 'c1hipsy', 'post_text': 'Lays', 'tegs':'#Hisl2t #lwa1r113w# ss fd'}).json()
# requests.post('http://localhost:5000/new_post', auth=HTTPBasicAuth('username', 'pass'), data={'title': 'chipsy', 'post_text': 'Lays'}).json()
# requests.post('http://localhost:5000/new_post', auth=HTTPBasicAuth('username', 'pass'), data={'title': 'chipsy', 'post_text': 'Lays', 'tegs':'#Hist #war'}).json()


@app.route('/add_teg', methods=['POST'])
@auth.login_required(role='admin')
def add_teg():
    new_teg = Tag(request.form['name'])
    db.session.add(new_teg)
    db.session.commit()
    time = datetime.now()
    return jsonify({ 'Action': '%s made a teg with the title "%s"' %(g.user.username, request.form['name']),
                    'Time': f'{time.ctime()}'})


# requests.post('http://localhost:5000/add_teg', auth=HTTPBasicAuth('username', 'pass'), data={'name': 'modern history'}).json()
# requests.post('http://localhost:5000/add_teg', auth=HTTPBasicAuth('username', 'pass'), data={'name': 'physics'}).json()



@app.route('/add_comment', methods=['POST'])
@auth.login_required(role=['common', 'admin'])
def add_comment():
    new_comment = Comment(request.form['comment_text'], request.form['post_id'], g.user.id)
    try:
        new_comment.comment_id = request.form['comment_id']
    except:
        pass   
    db.session.add(new_comment)
    db.session.commit()
    time = datetime.now()
    return jsonify({ 'Action': '%s made a post with the title "%s"' %(g.user.username, request.form['comment_text']),
                    'Time': f'{time.ctime()}'})



# requests.post('http://localhost:5000/add_comment', auth=HTTPBasicAuth('username', 'pass'), data={'comment_text': 'physics', 'post_id':'44'}).json()
# requests.post('http://localhost:5000/add_comment', auth=HTTPBasicAuth('username', 'pass'), data={'comment_text': 'physics', 'post_id':'44', 'comment_id':'1'}).json()


@app.route('/voute_for_comment', methods=['POST'])
@auth.login_required(role='common')
def give_voute_for_comment():
    give_voute = comment_votes.insert().values(user_id=g.user.id, comment_id=request.form['comment_id'])
    db.session.execute(give_voute)
    db.session.commit()
    time = datetime.now()
    return jsonify({ 'Action': '%s like comment with id "%s"' %(g.user.username, request.form['comment_id']),
                    'Time': f'{time.ctime()}'})



# requests.post('http://localhost:5000/voute_for_comment', auth=HTTPBasicAuth('username', 'pass'), data={'comment_id': '1'}).json()


@app.route('/voute_for_post', methods=['POST'])
@auth.login_required(role='common')
def give_voute_for_post():
    give_voute = post_votes.insert().values(user_id=g.user.id, post_id=request.form['post_id'])
    db.session.execute(give_voute)
    db.session.commit()
    time = datetime.now()
    return jsonify({ 'Action': '%s like post with id "%s"' %(g.user.username, request.form['post_id']),
                    'Time': f'{time.ctime()}'})

# requests.post('http://localhost:5000/voute_for_post', auth=HTTPBasicAuth('username', 'pass'), data={'post_id': '1'}).json()




