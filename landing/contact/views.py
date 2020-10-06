from flask import render_template, request, redirect
from landing import app 
from .forms import ContactForm, ViewContactForm
from .models import EmailSignup

@app.route("/contact/", methods =['GET', 'POST'])
def contact():
    
    form = ContactForm()
    if form.validate_on_submit():
        #print(form.first_name.data)
        #print(form.last_name.data)
        #print(form.email.data)
        #print(form.phone_number.data)
        data = { 
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": form.email.data,
            "phone_number": form.phone_number.data
        }
        obj = EmailSignup(**data)
        obj.save()
        return redirect("/success/")
    return render_template('contact.html', form=form)

@app.route("/contact_list/", methods=['GET', 'POST'])
def contact_list():
    form = ViewContactForm()
    if form.validate_on_submit():
        object_list = EmailSignup.query.all()
        return render_template('contact_list.html', form =None, object_list=object_list)
    return render_template('contact_list.html', form=form, object_list=[])

@app.route("/success/", methods=['GET'])
def success():
    return render_template('success.html')