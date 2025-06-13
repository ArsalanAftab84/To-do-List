from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from datetime import datetime
import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Database configuration
database_url = os.getenv('DATABASE_URL', 'postgresql://todo_db_owner:npg_ZH6KJkcmG7qO@ep-square-hill-a8bcranw-pooler.eastus2.azure.neon.tech/todo_db?sslmode=require')
print(f"Using database URL: {database_url}")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Todo Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

# Health check route
@app.route('/health')
def health():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return {'status': 'healthy', 'database': 'connected'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500

# Routes
@app.route('/')
def index():
    try:
        todos = Todo.query.order_by(Todo.created_at.desc()).all()
        return render_template('index.html', todos=todos)
    except Exception as e:
        print(f"Error loading todos: {e}")
        return f"Database connection error: {e}", 500

@app.route('/add', methods=['POST'])
def add():
    try:
        title = request.form.get('title')
        if title:
            new_todo = Todo(title=title)
            db.session.add(new_todo)
            db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error adding todo: {e}")
        return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    try:
        todo = Todo.query.get_or_404(id)
        todo.completed = not todo.completed
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error updating todo: {e}")
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    try:
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error deleting todo: {e}")
        return redirect(url_for('index'))

def wait_for_db():
    """Wait for database to be ready"""
    max_retries = 30
    for i in range(max_retries):
        try:
            with app.app_context():
                db.session.execute(text('SELECT 1'))
                print("Database connection successful!")
                return True
        except Exception as e:
            print(f"Database connection attempt {i+1}/{max_retries} failed: {e}")
            time.sleep(2)
    print("Failed to connect to database after all retries")
    return False

if __name__ == '__main__':
    print("Starting Flask application...")
    
    # Wait for database to be ready
    if not wait_for_db():
        print("Exiting due to database connection failure")
        sys.exit(1)
    
    # Create tables
    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
        except Exception as e:
            print(f"Error creating database tables: {e}")
            sys.exit(1)
    
    print("Starting Flask server on 0.0.0.0:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)
