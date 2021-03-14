from flask import Flask,render_template,redirect,flash,url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app=Flask(__name__)



class MyForm(FlaskForm):
    body = StringField('Message',validators=[InputRequired(message="Message Is Required")])
    name = StringField('Name',validators=[InputRequired(message="Name Is Required")])
    email=StringField('Email',validators=[InputRequired(),Email(message='Email Format is Required')])

    
    

mail_content = '''Hello,This is a simple mail.' ' '


message = MIMEMultipart()






@app.route('/',methods=['GET','POST'])
def home():
    form=MyForm()
    if form.validate_on_submit():
        message['Subject'] = 'Asalam U Alikum' 
        sender_address = 'yousufsyed900@gmail.com'
        sender_pass = 'Kiop000!'
        receiver_address = form.email.data
        sender_address = 'yousufsyed900@gmail.com'
        sender_pass = 'Kiop000!'
        receiver_address = form.email.data
        message['From'] = sender_address
        message['To'] = receiver_address
        session = smtplib.SMTP('smtp.gmail.com', 587) 
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        flash("Check Your Email "+str(form.name.data))
        return redirect(url_for('home'))
    return render_template('index.html',form=form)




if __name__ == '__main__':
    app.run(debug=True)
