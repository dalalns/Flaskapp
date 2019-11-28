from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

#url routing and binding the funtion to run app.route(rule, options)  rule: It represents the URL binding with the function.
#options: It represents the list of parameters to be associated with the rule object
@app.route('/')
def root():
	return render_template('a.html')

@app.route('/admin')
def admin():
	return "My name is admin"

@app.route('/student')
def student():
	return "My name is student"

@app.route('/user/<name>')
def helloworld(name):
	if name=='admin':
		return redirect(url_for('admin'))
	if name=='student':
		return redirect(url_for('student'))
	#print("this is ,name ", name)
	#return(f"this is name {age}")
	
#Another way to route url	
def about():  
    return "This is about page";  
  
app.add_url_rule("/about/","about",about)

app.run(debug=True) #app.run(host, port, debug, options)  The default hostname is 127.0.0.1, i.e. localhost.,The default port number is 5000
#debug The default is false.options	It contains the information to be forwarded to the server.

#Http Methods
#1	GET	It is the most common method which can be used to send data in the unencrypted form to the server.
#2	HEAD	It is similar to the GET but used without the response body.
#3	POST	It is used to send the form data to the server. The server does not cache the data transmitted using the post method.
#4	PUT	or editIt is used to replace all the current representation of the target resource with the uploaded content.
#5	DELETE	It is used to delete all the current representation of the target resource specified in the URL.