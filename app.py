from flask import Flask,render_template,redirect,flash,url_for
from flask_mail import Mail,Message
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Email

app=Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
app.config['DEBUG']=True
app.config['TESTING']=False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME']='yousufsyed900@gmail.com'
app.config['MAIL_PASSWORD']='Kiop000'
app.config['MAIL_MAX_EMAILS']=None
app.config['MAIL_DEFAULT_SENDER']='yousufsyed900@gmail.com'
app.config['MAIL_ASCII_ATTACHMENTS']=False
mail = Mail(app)


class MyForm(FlaskForm):
    body = StringField('Message',validators=[InputRequired(message="Message Is Required")])
    name = StringField('Name',validators=[InputRequired(message="Name Is Required")])
    email=StringField('Email',validators=[InputRequired(),Email(message='Email Format is Required')])



@app.route('/',methods=['GET','POST'])
def home():
    form=MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        msg =Message(sender="yousufsyed900@gmail.com",reply_to=form.email.data,subject=form.email.data,recipients=['yousufsyed900@gmail.com'],body=form.body.data)
        mail.send(msg)
        reply=Message(sender="yousufsyed900@gmail.com",subject="Asalam U ALikum",body="How are you "+str(form.name.data)+", It is a message from syed yousuf here is my freelance work https://www.fiverr.com/users/syedyousuf90/manage_orders?source=header_navigation&search_type=completed",recipients=[form.email.data])
        mail.send(reply)

        flash("Check Your Email "+str(form.name.data))
        return redirect(url_for('home'))
    return render_template('index.html',form=form)




if __name__ == '__main__':
    app.run(debug=True)
