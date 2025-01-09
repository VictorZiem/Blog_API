from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Relacionamento: um post pode ter vários comentários
    comments = db.relationship('Comment', backref='post', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)

    # Foreign Key que referencia o Post
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "text": self.text,
            "post_id": self.post_id
        }
