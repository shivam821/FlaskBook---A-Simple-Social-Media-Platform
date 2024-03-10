from flask import Flask,render_template,url_for,redirect,request,session,flash
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_login import login_user, logout_user,login_required,current_user,login_manager
from sqlalchemy.sql import func
from flask_login import LoginManager
from flask_login import UserMixin



app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the login route for Flask-Login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique = True,nullable = False)
    username = db.Column(db.String(150),nullable = False)
    password = db.Column(db.String(150),nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    posts = db.relationship('Post',backref = 'user',passive_deletes = True)
        # Existing class definition remains unchanged

    # Implement required methods for Flask-Login
    def is_active(self):
        return True  # Return True if the user account is active, or implement your logic

    def is_authenticated(self):
        return True  # Return True if the user is authenticated, or implement your logic

    def get_id(self):
        return str(self.id)  # Return a string that uniquely identifies the user, typically the user ID



    def __init__(self,email,username,password) : 
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')

    def check_password(self,password) : 
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Post(db.Model) : 
    id = db.Column(db.Integer,primary_key = True)
    text = db.Column(db.Text,nullable = False)
    date_created = db.Column(db.DateTime(timezone = True),default = func.now())
    author = db.Column(db.Integer,db.ForeignKey('user.id',ondelete = "CASCADE"),nullable = False)

with app.app_context():
    db.create_all()



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("emailaddress")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            login_user(user)  # Login the user using Flask-Login
            flash('Logged In', category='success')
            return redirect(url_for('posts'))  # Redirect to posts page after successful login
        else:
            flash('Invalid email or password', category='error')

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()  # Logout the user using Flask-Login
    flash('Logged out successfully', category='success')
    return redirect(url_for('home'))



@app.route('/signup',methods = ['GET','POST'])
def signup():
    if request.method == 'POST' : 

        email = request.form.get("emailaddress")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

         
        if email_exists : 
            flash('Email already exits',category = 'error')
        elif username_exists : 
            flash('Username already exits',category = 'error')
        elif password1 != password2 : 
            flash('Passwords dont match',category = 'error')
        # elif len(password1) < 5 :
        #     flash('Passowrd is too short',category = 'error')
        # elif len(username) < 2 :
        #     flash('Username is too short',category = 'error')
        else :
            new_user = User(email=email,username=username,password=password2)
            db.session.add(new_user)
            db.session.commit()
            flash('User Created')
            return redirect('/login')

    return render_template('signup.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()

        posts = Post.query.all()
    return render_template('posts.html',user=user,posts = posts)

@app.route('/posts_div')
def posts_div():
    
    return render_template('posts_div.html')


# @app.route('/create_post', methods=['GET', 'POST'])
# def create_post():
#     if 'email' in session:
#         user = User.query.filter_by(email=session['email']).first()

#         if request.method == "POST":
#             textarea = request.form.get('textarea')

#             if not textarea:
#                 flash('Cannot post empty', category='error')
#             else:
#                 post = Post(text=textarea, author=user.id)
#                 db.session.add(post)
#                 db.session.commit()
#                 flash('Post Created', category='success')
#                 return render_template('create_post.html', user=user)

#         return render_template('create_post.html', user=user)

#     flash('You need to be logged in to create a post.', category='error')
#     return redirect(url_for('login'))


@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()

        if request.method == "POST":
            textarea = request.form.get('textarea')

            if not textarea.strip():  # Check if textarea is empty or contains only whitespace
                flash('Cannot post empty', category='error')
            else:
                post = Post(text=textarea, author=user.id)
                db.session.add(post)
                db.session.commit()
                flash('Post Created', category='success')
                return redirect(url_for('create_post'))  # Redirect to the same page after successful post

        return render_template('create_post.html', user=user)

    flash('You need to be logged in to create a post.', category='error')
    return redirect(url_for('login'))



@app.route("/delete-post/<int:id>", methods=["POST"])
@login_required
def delete_post(id):
    post = Post.query.get(id)
    if not post:
        flash("Post does not exist.", category="error")
    elif current_user.id != post.author:
        flash("You don't have permission to delete the post.", category="error")
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully.', category='success')

    # Redirect back to the posts page regardless of the outcome
    return redirect(url_for('posts'))




if __name__ == '__main__':
    app.run(debug=True ,port=8080,use_reloader=False)