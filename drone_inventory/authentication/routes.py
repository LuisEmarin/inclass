from flask import Blueprint, render_template, request,url_for, flash, redirect
from drone_inventory.forms import UserLoginForm
from drone_inventory.models import User, db, check_password_hash
from flask_login import login_user, login_required, logout_user


auth = Blueprint('auth',__name__,template_folder='auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)


#  create a new user class and add that user into the table 
        new_user = User(email, password)
        db.session.add(new_user)
        db.session.commit()
        # flash message for registration success
        flash(f'You have successfully registered an account under{email}', 'user-created')
        # redirecting to home page
        return redirect(url_for('site.home'))
        


    return render_template('signup.html', form = form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)

        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash('You were successfully logged in', 'auth-success')
            # redirecting upon successful sign in
            return redirect(url_for('site.home'))

        else:
            #  eventually putting popup for failed sign in
            flash('Your Email/Password id incorrent','auth-failed')
            return redirect(url_for('auth.signin'))


    return render_template('signin.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out.', 'auth-success')
    return redirect(url_for('site.home'))
