from flask import *
from main import *

app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')
@app.route("/")
def indexx():
    return render_template("index.html")

@app.route('/SignUp')
def signup():
    return render_template('signup.html')

@app.route('/SignIn')
def signin():
    return render_template('signin.html')

@app.route('/BlogPost')
def blogpost():
    return render_template('blog_post.html')

@app.route('/MarketBlog')
def Market():
    return render_template('Marblog.html')

@app.route('/SalesBlog')
def Sales():
    return render_template('Salesblog.html')

@app.route('/ServiceBlog')
def Service():
    return render_template('Serviceblog.html')

@app.route('/ViewPost')
def viewpost():
    a=selectAllPost()
    return render_template('view_post.html',elist=a)

# @app.route('/adddata',method=["post"])
# def adding():
#     name=request.form('name')
#     age=request.form('age')
#     email=request.form('email')
#     password=request.form('password')
#     t=(name,age,email,password)
#     signUp(t)
#     return redirect('/SignIn')

@app.route("/adddataauthor", methods=["post"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    password = request.form["password"]
    t = (name,age,email, password)
    addAuthor(t)
    return redirect("/SignIn")

# @app.route('/SignIn',method=['post'])
# def signin():
#     email=request.form('email')
#     password=request.form('password')
#     t=(email,password)
#     t1=checksignin(t)
#     if t in t1:
#         return redirect('/BlogPost')
#     else:
#         return redirect('/SignIn')

@app.route("/loga", methods=["post"])
def lga():
    email = request.form["email"]
    password = request.form["password"]
    t = (email, password)
    t1 = checklgauthor(t)
    if t in t1:
        return redirect("/BlogPost")
    else:
        return redirect("/SignIn")

# @app.route('/BlogPost',method=['post'])
# def addblog():
#     name=request.form['name']
#     title=request.form['title']
#     blog=request.form['blog']
#     t=(name,title,blog)
#     blogcheck(t)
#     return redirect('/ViewPost')

@app.route("/addpostauthor", methods=["post"])
def addpo():
    name = request.form["name"]
    title = request.form["title"]
    post = request.form["post"]
    t = (name, title, post)
    addPost(t)
    return redirect("/ViewPost")

if __name__=="__main__":
    app.run(debug=True)