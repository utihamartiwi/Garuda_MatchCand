from market import app
from flask import render_template, redirect, url_for
from market.models import Company, Item, User
from market.forms import RegisterForm
from market.forms import RegisterForm2
from market import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/candidate')
def market_page():
    users = User.query.all()
    return render_template('market.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              education=form.Education.data,
                              skill=form.Skill.data,
                              exp=form.Work_Experience.data,
                              domicile=form.Domicile.data,
                              resume=form.Link_to_resume.data,
                              repo=form.Link_to_repository.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')

    return render_template('register.html', form=form)

@app.route('/registerComany', methods=['GET', 'POST'])
def register2_page():
    form = RegisterForm2()
    if form.validate_on_submit():
        company_to_create = Company(company_name=form.comname.data,
                              position=form.Positon2.data,
                              education=form.Education2.data,
                              skill=form.Skill2.data,
                              exp=form.Work_Experience2.data,
                              domicile=form.Domicile2.data,
                              number_of_need=form.Numberofneed.data,
                              benefit=form.benefit.data)
        db.session.add(company_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            print(f'There was an error with creating a user: {err_msg}')

    return render_template('register2.html', form=form)