from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)

# @app.route("/")  #when press / then call hello_world function
# def hello_world():
#     return "<p>Hello, Ayan!</p>"


# @app.route('/<username>/<int:post_id>')  #when press / then call hello_world function
# def hello_world(username=None, post_id=None): #passing the name
#     #print(url_for('static', filename='bolt.ico')) # it will print the bolt.ico path
#     return render_template('index.html', name=username, post_id=post_id)

#code for added files
@app.route('/')  #when press / then call hello_world function
def my_home(): #passing the name
    return render_template('index.html')


#code for added files
@app.route('/<string:page_name>')
def html_page(page_name): #passing the name
    return render_template(page_name)
#this above will take care of below code in end commented code


#code to fetch the submitted data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data) # it will call the write to file function
            write_to_csv(data) # it will call the write to csv function
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])





#
# #instead of creating multiple entries, we can set dynamic entries
#
#
# @app.route("/about.html")  #when press / then call hello_world function
# def about():
#     return render_template('about.html')
#
#
# @app.route("/works.html")  #when press / then call hello_world function
# def work():
#     return render_template('works.html')
#
#
# @app.route("/contact.html")  #when press / then call hello_world function
# def contact():
#     return render_template('contact.html')
#
#
#
# @app.route("/blog")  #when press /blog/ then call blog function
# def blog():
#     return "<p>this is blog page- parwinder singh dhaliwal</p>"
#
#
#
# # @app.route("/favicon.ico")  #when press /blog/ then call blog function
# # def blog1():
# #     return "<p>Icon for web, Parwinder</p>"
#
# @app.route("/blog/2023/dogs")  #when press /blog/2023/dogs then call blog2 function
# def blog2():
#     return "<p>this is dog page</p>"
#
