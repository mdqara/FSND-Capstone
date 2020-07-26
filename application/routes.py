from application import app
from flask import render_template, request, abort, jsonify

courseData = [{"courseID":"1111","title":"FSND","description":"Full Stack Nano Degree","credits":"3","term":"Fall, Spring"}, 
              {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, 
              {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, 
              {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, 
              {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]



@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', index=True)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term=2020):
    return render_template("courses.html", courseData=courseData, courses = True )


@app.route("/register")
def register():
    return render_template('register.html', register=True)


@app.route("/login")
def login():
    return render_template('login.html', login=True)



@app.route("/enrollment", methods=["GET","POST"])
def enrollment():

    #body = request.get_json()
    #data = body 
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')
    return render_template("enrollment.html", enrollment=False, data={"id":id,"title":title,"term":term}) 


@app.route('/api/') 
@app.route('/api/<index>') 
def api(index=None):
    if(index==None):
        json_data = courseData
    else:
        json_data = courseData[int(index)]

    return jsonify(json_data)