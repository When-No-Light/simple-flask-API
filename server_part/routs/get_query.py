from server_part.app import app
from markupsafe import escape
from server_part.database.tables import User, Post
from flask import abort, jsonify, g
from server_part.utils.misc import auth


# admin could get information about some users using this function

@app.route('/user/<int:user_id>', methods=['GET'])
@auth.login_required(role=['admin'])
def show_user_profile(user_id):
    user_obj = User.query.filter_by(id=user_id).first()
    return jsonify({'username': user_obj.username, 
                    'is active': user_obj.active,
                    'confirmed at': user_obj.confirmed_at,
                    'last activity': user_obj.last_activity,
                    'user roles': [role.name for role in user_obj.roles]})


# requests.get('http://localhost:5000/user/9', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()


@app.route('/post/<int:post_id>', methods=['GET'])
@auth.login_required(role=['admin', 'common'])
def show_post(post_id):
    post_obj = Post.query.filter_by(id=post_id).first()
    user_obj = User.query.filter_by(id=post_obj.user_id).first()
    return jsonify({'title': post_obj.title, 
                    'post text': post_obj.post_text,
                    'confirmed at': post_obj.confirmed_at,
                    'outdated': post_obj.outdated,
                    'created by ': user_obj.username,
                    'with tags': [tag.name for tag in post_obj.tag]})

    

# requests.get('http://localhost:5000/post/55', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()