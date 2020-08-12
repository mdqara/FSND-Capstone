from application import app, cors
from flask import render_template, request, abort, jsonify, url_for, redirect
from models import Course, Instructor
from models import db

dummy_course = [{
    "id": "1",
    "desc": "Hone specialized skills in Data Product Management and learn how to model data, identify trends in data, and leverage those insights to develop data-backed product strategy.",
    "duration": "1",
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/4FCXQsUpzftEgEdFGqQmXE/8ba5c2e69a5b036d4dafe1ae5803fe60/syllabus__8_.jpg",
    "name": "Applying Data Science to Product Management"
},
    {
    "id": "2",
    "desc": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
    "duration": "2",
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/219UNjX4r925AbuYRhbFYa/cc41f3d6d2a53d23637335a7a81baa1b/syllabus__6_.jpg",
    "name": "Learn SQL+"
},
    {
    "id": "3",
    "desc": "Gain foundational data skills applicable to marketing. Collect and analyze data, model marketing scenarios, and communicate your findings with Excel, Tableau, Google Analytics, and Data Studio.",
    "duration": "3",
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/1rJDmku9XmR3FlxsyJ8JVc/a6442a0ef3d7200af03b9107e15f894c/MAND_Syllabus.jpg",
    "name": "Become a Marketing Analyst "
},
    {
    "id": "4",
    "desc": "Learn foundational machine learning techniques -- from data manipulation to unsupervised and supervised algorithms.",
    "duration": "3",
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/4BPXeRdaDDHpbKZOTJfG0a/4da8801f996950f2f2cb63b4561dbeaf/image-term1.jpg",
    "name": "Intro to Machine Learning with PyTorch"
}]


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


@app.route('/course/<int:index>', methods=['GET'])
def view_courses(index):
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


@app.route("/course/<int:index>", methods=['POST'])
def update_course(index):

    try:
        result = db.session.query(Course).filter(Course.id == index)
        result = result[0]
        course = result

        course.name = request.form.get('course-name')
        course.description = request.form.get('course-description')
        course.duration = request.form.get('course-duration')
        course.image_link = request.form.get('course-img-URL')

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(e)

    finally:
        db.session.close()

    return redirect(url_for('view_courses', index=index))


@app.route("/course/<int:index>", methods=['DELETE'])
def delete_course(index):
    try:
        result = db.session.query(Course).filter(Course.id == index)
        result = result[0]

        db.session.delete(result)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print(e)

    finally:
        db.session.close()

    return redirect(url_for('view_catalog'))


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


@app.route('/catalog')
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

    #data = data + dummy_course

    return render_template("catalog.html", courses=data)


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

    data = data + dummy_course

    return jsonify(data)
