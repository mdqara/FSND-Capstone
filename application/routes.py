from application import app, cors
from flask import render_template, request, abort, jsonify, url_for, redirect
from models import Course, Instructor
from models import db


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PATCH,POST,DELETE,OPTIONS')
    return response


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', login=False)


@app.route("/courses/")
@app.route("/courses/<term>")
def courses(term=2020):
    return render_template("courses.html", courseData=courseData, courses=True)


@app.route("/register")
def register():
    return render_template('register.html', register=True)


@app.route("/login")
def login():
    return render_template('login.html', login=True)


@app.route("/user")
def user():
    return render_template('user.html')


@app.route("/add-course")
def add_course():
    return render_template('add-course.html')


@app.route("/create-course", methods=['POST'])
def create_course():

    # try:
    course_name = request.form.get('course-name')
    description = request.form.get('course-description')
    duration = request.form.get('course-duration')
    imgURL = request.form.get('course-img-URL')

    course_to_add = Course(
        name=course_name,
        description=description,
        duration=duration,
        image_link=imgURL,
    )

    db.session.add(course_to_add)
    db.session.commit()

    return render_template("enrollment.html", course_name=course_name)


@app.route('/course/<int:index>')
def course(index):
    result = db.session.query(Course).filter(Course.id == index)
    result = result[0]

    json_data = {
        'id': result.id,
        'name': result.name,
        'desc': result.description,
        'duration': result.duration,
        'image_link': result.image_link
    }

    return render_template('course.html', course=json_data)


@app.route("/update-course/<int:index>", methods=['POST'])
def update_course(index):

    # try:

    result = db.session.query(Course).filter(Course.id == index)
    result = result[0]
    course = result

    course.name = request.form.get('course-name')
    course.description = request.form.get('course-description')
    course.duration = request.form.get('course-duration')
    course.image_link = request.form.get('course-img-URL')

    db.session.commit()

    return redirect(url_for('course', index=index))


# except Exception as e:
#    db.session.rollback()
#    print(e)

# finally:
#    db.session.close()


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():

    return render_template("enrollment.html")

    '''
    body = request.get_json()
    data = body
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')

    return render_template("enrollment.html", enrollment=False, data={"id": id, "title": title, "term": term})
    '''


@app.route('/view_catalog')
def view_catalog():

    courses = Course.query.all()
    data = []

    for course in courses:
        data.append({
            "id": course.id,
            "name": course.name,
            "desc": course.description,
            "duration": course.duration,
            "image_link": course.image_link
        })

    return render_template("catalog.html", courses=data)


@app.route('/view_courses')
def view_courses():
    return render_template("courses.html")


@app.route('/api/')
@app.route('/api/<index>')
def api(index=None):
    courses = Course.query.all()
    data = []

    for course in courses:
        data.append({
            "name": course.name,
            "desc": course.description,
            "duration": course.duration,
            "image_link": course.image_link
        })

    return jsonify(data)
