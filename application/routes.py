from flask import render_template, redirect, url_for, flash, request, make_response, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from application import app
from application.models import *
from application.forms import *
from application.utils import save_image

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            login_user(user)
            return redirect(url_for('profile', username=username))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html', title="Login", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# @app.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', title=f'{current_user.fullname} Profile')


@app.route('/<string:username>')
@login_required
def profile(username):
    posts = current_user.posts
    reverse_posts = posts[::-1]
    return render_template('profile.html', title=f'{current_user.fullname} Profile', posts=reverse_posts)

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = CreatePostForm()

    if form.validate_on_submit():
        post = Post(
            author_id = current_user.id,
            caption = form.caption.data
        )
        post.image = save_image(form.post_pic.data)
        db.session.add(post)
        db.session.commit()
        flash('Your image has been posted', 'success')

    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(author_id = current_user.id).order_by(Post.post_date.desc()).paginate(page=page, per_page=3)

    # posts = current_user.posts

    return render_template('index.html', title='Home', form=form, posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            password = form.password.data,
            fullname = form.fullname.data,
            email = form.email.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect('login.html')
        
    return render_template('signup.html', title='Signup', form=form)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if form.username.data != user.username:
            user.username = form.username.data
        user.fullname = form.fullname.data
        user.bio = form.bio.data


        if form.profile_pic.data:
            pass

        db.session.commit()
        flash("profile updated", 'success')
        return redirect(url_for('profile', username=current_user.username))
        
    form.username.data = current_user.username
    form.fullname.data = current_user.fullname
    form.bio.data = current_user.bio

    return render_template('edit.html', title="Edit {current_user.username} Profile", form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/respass', methods=['GET', 'POST'])
@login_required
def respass():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        if user.password != form.old_password.data:
            flash("ur old password is wrong", "error")
            return redirect(url_for("respass"))
        user.password = form.new_password.data
        user.password_Confirm = form.confirm_new_password.data

        if form.old_password.data == form.new_password.data:
            flash("ur password is the same as the old one", "error")
            return redirect(url_for("respass"))

        db.session.commit()
        flash("password has been reset", 'success')
        return redirect(url_for('profile', username=current_user.username))
    
    return render_template('resetpass.html', title='ResetPassword', form=form)


@app.route('/like', methods=['GET', 'POST'])
@login_required
def like():
    data = request.json
    post_id = int(data['postId'])
    like = Like.query.filter_by(user_id=current_user.id,post_id=post_id).first()
    if not like:
        like = Like(user_id=current_user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
        return make_response(jsonify({"status" : True}), 200)
    
    db.session.delete(like)
    db.session.commit()
    return make_response(jsonify({"status" : False}), 200)

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    form = EditPostForm()

    post = Post.query.get(post_id)
    if form.validate_on_submit():
        post.caption = form.caption.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('index', username=current_user.username))

    elif request.method == 'GET':
        form.caption.data = post.caption

    return render_template('edit_post.html', title='Edit Post', form=form, post=post)

@app.route('/forgotPass', methods=['GET', 'POST'])
def forgotPass():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        email = User.query.filter_by(email=email)
    return render_template('forgotpass.html', title='Forgot Password', form=form)