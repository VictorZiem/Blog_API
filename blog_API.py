from flask import Flask, request, jsonify
from Meus_modelos import db, Post, Comment
import os

app = Flask(__name__)

# Configurações de banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'blog.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com o app
db.init_app(app)



# Rota inicial (opcional)
@app.route('/')
def home():
    return jsonify({"message": "Blog API - Flask"}), 200


# ========= ROTAS PARA POSTS =========

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200


@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data.get('title') or not data.get('content'):
        return jsonify({"error": "Title and content are required"}), 400

    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post.to_dict()), 200


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify(post.to_dict()), 200


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    db.session.delete(post)
    db.session.commit()
    return '', 204


# ========= ROTAS PARA COMMENTS (COMENTÁRIOS) =========

@app.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([comment.to_dict() for comment in comments]), 200


@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()
    if not data.get('text'):
        return jsonify({"error": "Comment text is required"}), 400

    new_comment = Comment(text=data['text'], post_id=post_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment.to_dict()), 201


@app.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['GET'])
def get_comment(post_id, comment_id):
    comment = Comment.query.filter_by(post_id=post_id, id=comment_id).first()
    if not comment:
        return jsonify({"error": "Comment not found"}), 404
    return jsonify(comment.to_dict()), 200


@app.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['PUT'])
def update_comment(post_id, comment_id):
    comment = Comment.query.filter_by(post_id=post_id, id=comment_id).first()
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    data = request.get_json()
    comment.text = data.get('text', comment.text)
    db.session.commit()
    return jsonify(comment.to_dict()), 200


@app.route('/posts/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(post_id, comment_id):
    comment = Comment.query.filter_by(post_id=post_id, id=comment_id).first()
    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
