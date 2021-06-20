from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    Education = StringField(label='Education Background:', validators=[Length(min=2), DataRequired()])
    Skill = StringField(label='Skill:', validators=[Length(min=2), DataRequired()])
    Work_Experience = StringField(label='Work Experience:', validators=[Length(min=2), DataRequired()])
    Domicile = StringField(label="Domicile:", validators=[Length(min=2), DataRequired()])
    Positon = StringField(label='Positon:', validators=[Length(min=2), DataRequired()])
    Link_to_resume = StringField(label='Link to resume:', validators=[Length(min=6), DataRequired()])
    Link_to_repository = StringField(label='Link to repository:', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Submit Data')

class RegisterForm2(FlaskForm):
    comname = StringField(label='Company Name:', validators=[Length(min=2, max=30), DataRequired()])
    Education2 = StringField(label='Education Background:', validators=[Length(min=2), DataRequired()])
    Skill2 = StringField(label='Skill:', validators=[Length(min=2), DataRequired()])
    Work_Experience2 = StringField(label='Work Experience:', validators=[Length(min=2), DataRequired()])
    Domicile2 = StringField(label="Domicile:", validators=[Length(min=2), DataRequired()])
    Positon2 = StringField(label='Positon:', validators=[Length(min=2), DataRequired()])
    Numberofneed = StringField(label='Number of Need:', validators=[Length(min=0), DataRequired()])
    benefit = StringField(label='Benefit:', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Submit Data')