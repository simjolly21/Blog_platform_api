from flask import Flask, request, jsonify
from models import BlogPost
from database import db_session, init_db
from datetime import datetime

app = Flask(__name__)

# Initialize the database
@app.before_first_request
def setup():
    init_db()

@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('content'):
        return jsonify({'error': 'Title and content are required'}), 400
    
    new_post = BlogPost(
        title=data['title'],
        content=data['content'],
        category=data.get('category', ''),
        tags=data.get('tags', []),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db_session.add(new_post)
    db_session.commit()
    return jsonify(new_post.serialize()), 201

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    post.category = data.get('category', post.category)
    post.tags = data.get('tags', post.tags)
    post.updated_at = datetime.utcnow()

    db_session.commit()
    return jsonify(post.serialize()), 200

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    
    db_session.delete(post)
    db_session.commit()
    return '', 204

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post.serialize()), 200

@app.route('/posts', methods=['GET'])
def get_posts():
    term = request.args.get('term', '')
    query = BlogPost.query
    
    if term:
        query = query.filter(
            (BlogPost.title.contains(term)) | 
            (BlogPost.content.contains(term)) | 
            (BlogPost.category.contains(term))
        )
    
    posts = query.all()
    return jsonify([post.serialize() for post in posts]), 200

if __name__ == '__main__':
    app.run(debug=True)
