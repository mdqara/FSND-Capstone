from flask import Flask, render_template, request, abort, jsonify, url_for, redirect
from flask_cors import CORS
from models import setup_db, db, Course, Instructor
from .auth.auth import AuthError, requires_auth, AUTH0_DOMAIN, API_AUDIENCE, REDIRECT_URI, CLIENT_ID
import requests
import os

# create and configure the app
def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__)
    cors = CORS(app)
    CORS(app)
    database_path = os.environ.get('DATABASE_URL')
    setup_db(app, database_path)
        
    dummy_course = [{"desc": "Hone specialized skills in Data Product Management and learn how to model data, identify trends in data, and leverage those insights to develop data-backed product strategy.",
                    "duration": "1",
                    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/4FCXQsUpzftEgEdFGqQmXE/8ba5c2e69a5b036d4dafe1ae5803fe60/syllabus__8_.jpg",
                    "name": "Applying Data Science to Product Management",
                    "instructor": "Mohammad Ali"},
                    {"desc": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
                    "duration": "2",
                    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/219UNjX4r925AbuYRhbFYa/cc41f3d6d2a53d23637335a7a81baa1b/syllabus__6_.jpg",
                    "name": "Learn SQL+",
                    "instructor": "Mohammad Ali"},
                    {"desc": "Gain foundational data skills applicable to marketing. Collect and analyze data, model marketing scenarios, and communicate your findings with Excel, Tableau, Google Analytics, and Data Studio.",
                    "duration": "3",
                    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/1rJDmku9XmR3FlxsyJ8JVc/a6442a0ef3d7200af03b9107e15f894c/MAND_Syllabus.jpg",
                    "name": "Become a Marketing Analyst",
                    "instructor": "Mohammad Ali"},
                    {"desc": "Learn foundational machine learning techniques -- from data manipulation to unsupervised and supervised algorithms.",
                    "duration": "3",
                    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/4BPXeRdaDDHpbKZOTJfG0a/4da8801f996950f2f2cb63b4561dbeaf/image-term1.jpg",
                    "name": "Intro to Machine Learning with PyTorch",
                    "instructor": "Mohammad Ali"}]


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PATCH,POST,DELETE,OPTIONS')
        return response

        '''
        <============= Front End =============>
        '''


    @app.route("/")
    @app.route("/index")
    def index():

        return render_template('index.html', login=False)


    @app.route("/login")
    def login():

        return redirect(
            "https://dev-ypnvxc34.us.auth0.com/authorize?audience=course&response_type=token&client_id=j11ADdqp4NY4wjujGfb6IPYupMZDHrbF&redirect_uri=https://fsnd-capstone-2020.herokuapp.com/")


    '''
        function for viewing all courses in front end

        returns:
            A web page that contains all courses
    '''


    @app.route('/catalog')
    @requires_auth('get:course')
    def view_catalog(*args, **kwargs):

        url = 'http://127.0.0.1:5000/api/courses'
        data = requests.get(url)
        data = data.json()

        # data = data + dummy_course

        return render_template("catalog.html", courses=data["courses"])


    '''
        function for showing the add course page in the front end, and it request the name of instructors from the database and send it to the front end.

        returns:
            A web page that contains all courses
    '''


    @app.route("/add-course")
    @requires_auth('post:course')
    def add_course(*args, **kwargs):

        instructors = Instructor.query.all()

        data = []

        for instructor in instructors:
            data.append({
                "id": instructor.id,
                "name": instructor.name,
                "qualification": instructor.qualification
            })

        # print(data)

        return render_template('add-course.html', data=data)


    '''
        function posting a course to the app.

        returns:
            A confirmation message in a wep page that the course has been added
    '''


    @app.route("/create-course", methods=['POST'])
    @requires_auth('post:course')
    def create_course(*args, **kwargs):

        try:
            course_name = request.form.get('course-name')
            description = request.form.get('course-description')
            duration = request.form.get('course-duration')
            imgURL = request.form.get('course-img-URL')
            instructor = request.form.get('instructor')

            course_to_add = Course(
                name=course_name,
                description=description,
                duration=duration,
                image_link=imgURL,
                instructor=instructor
            )

            db.session.add(course_to_add)
            db.session.commit()

        except Exception:
            print(Exception)
            abort(500)

        return render_template("catalog.html", data=course_name)


    '''
        function adding an instructor in the frontend.

        returns:
            A web page that views add instructor form.
    '''


    @app.route("/add-instrcutor")
    @requires_auth('post:instructor')
    def add_instructor(*args, **kwargs):
        return render_template('add-instructor.html')


    @app.route("/create-instructor", methods=['POST'])
    @requires_auth('post:instructor')
    def create_instructor(*args, **kwargs):

        try:
            instructor_name = request.form.get('instructor-name')
            instructor_qualification = request.form.get(
                'instructor-qualification')

            instructor_to_add = Instructor(
                name=instructor_name,
                qualification=instructor_qualification
            )

            db.session.add(instructor_to_add)
            db.session.commit()

        except Exception:
            print(Exception)
            abort(500)

        return render_template("catalog.html", data=instructor_name)


    '''
        function for getting a specific course based on its index from the api endpoint.

        returns:
            A web page that contains the specific course index.
    '''


    @app.route('/course/<int:index>', methods=['GET'])
    @requires_auth('get:course')
    def view_courses(payload, index):

        url = 'http://127.0.0.1:5000/api/course/' + str(index)
        data = requests.get(url)
        data = data.json()

        return render_template('course.html', course=data["course"])


    '''
        function for updating a specific course based on its index.

        returns:
            A web page that contains the edit information of the that specific course index.
    '''


    @app.route("/course/<int:index>", methods=["PATCH"])
    @requires_auth('patch:course')
    def update_course(payload, index):

        try:
            body = request.get_json()

            name = body.get('name', None)
            description = body.get('description', None)
            duration = body.get('duration', None)
            image_link = body.get('image_link', None)

            result = db.session.query(Course).filter(Course.id == index)
            result = result[0]
            course = result

            course.name = name
            course.description = description
            course.duration = duration
            course.image_link = image_link

            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(e)

        finally:
            db.session.close()

        return redirect(url_for('view_courses', index=index))


    '''
        function for deleting a specific course based on its index.

        returns:
            it will returns to the catalog.html page.
    '''


    @app.route("/course/<int:index>", methods=['DELETE'])
    @requires_auth('delete:course')
    def delete_course(payload, index):
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


    '''

    <============= API EndPoints =============>

    '''

    '''
        function for viewing all courses

        returns:
            all JSON object of all courses
    '''


    @app.route('/api/courses')
    @requires_auth('get:course')
    def get_courses_json(*args, **kwargs):

        try:
            courses = Course.query.all()
            data = []

            for course in courses:
                data.append({
                    "id": course.id,
                    "name": course.name,
                    "desc": course.description,
                    "duration": course.duration,
                    "image_link": course.image_link,
                    'instructor': course.instructor
                })

            return jsonify({
                'success': True,
                'courses': data
            })

        except BaseException:
            abort(422)


    '''
        function for getting a specific course based on its index.

        returns:
            A JSON object that contains the course information.
    '''


    @app.route('/api/course/<int:index>', methods=['GET'])
    @requires_auth('get:course')
    def get_course_index_json(payload, index):

        try:
            result = db.session.query(Course).filter(Course.id == index)
            result = result[0]

            data = {
                'id': result.id,
                'name': result.name,
                'desc': result.description,
                'duration': result.duration,
                'image_link': result.image_link,
                'instructor': result.instructor
            }

            return jsonify({
                'message': True,
                'course': data
            })

        except BaseException:
            abort(422)


    '''
        function posting an instuctor to the app.

        returns:
            A web page of a confirmation message in a wep page that the instuctor has been added
    '''


    @app.route('/api/instructor', methods=['GET'])
    def get_instuctor_json(*args, **kwargs):

        try:

            instructors = Instructor.query.all()
            data = []

            for instructor in instructors:
                data.append({
                    "id": instructor.id,
                    "name": instructor.name,
                    "qualification": instructor.qualification
                })

            return jsonify({
                'success': True,
                'courses': data
            })

        except BaseException:
            abort(422)


    @app.route('/api/instructor/<int:index>', methods=['GET'])
    def get_instuctor_index_json(index):

        try:
            result = db.session.query(Instructor).filter(
                Instructor.id == index)
            result = result[0]

            data = []

            data = {
                'id': result.id,
                'name': result.name,
                'qualification': result.qualification
            }

            return jsonify({
                'success': True,
                'courses': data
            })

        except BaseException:
            abort(422)


    '''
        function posting a course to the app.

        returns:
            JSON object confirmation.
    '''


    @app.route("/api/course", methods=['POST'])
    @requires_auth('post:course')
    def create_course_json(*args, **kwargs):
        try:

            data = request.get_json()
            course_name = data['name']
            description = data['desc']
            duration = data['duration']
            imgURL = data['image_link']
            instructor = data['instructor']

            course_to_add = Course(
                name=course_name,
                description=description,
                duration=duration,
                image_link=imgURL,
                instructor=instructor
            )

            db.session.add(course_to_add)
            db.session.commit()

        except Exception:
            print(Exception)
            abort(422)

        return jsonify({
            'message': True,
            'course_name': course_name
        })


    @app.route("/api/instructor", methods=['POST'])
    @requires_auth('post:instructor')
    def create_instructor_json(*args, **kwargs):
        try:

            data = request.get_json()

            instructor_name = data['name']
            instructor_qualification = data['qualification']

            instructor_to_add = Instructor(
                name=instructor_name,
                qualification=instructor_qualification
            )

            db.session.add(instructor_to_add)
            db.session.commit()

        except Exception:
            print(Exception)
            abort(422)

        return jsonify({
            'message': True,
            'name': instructor_name
        })


    @app.route("/api/course/<int:index>", methods=["PATCH"])
    def update_course_json(index):

        try:
            data = request.get_json()

            name = data['name']
            description = data['desc']
            duration = data['duration']
            image_link = data['image_link']
            instructor = data['instructor']

            result = db.session.query(Course).filter(Course.id == index)
            result = result[0]
            course = result

            course.name = name
            course.description = description
            course.duration = duration
            course.image_link = image_link
            course.instructor = instructor

            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(e)
            abort(422)

        finally:
            db.session.close()

        return jsonify({
            'message': True,
            'course_id': index,
            'name': name,
            'description': description,
            'duration': duration,
            'image_link': image_link,
            'instructor': instructor
        })


    @app.route("/api/instructor/<int:index>", methods=["PATCH"])
    def update_instructor_json(index):

        try:

            data = request.get_json()
            name = data['name']
            qualification = data['qualification']

            result = db.session.query(Instructor).filter(
                Instructor.id == index)
            result = result[0]
            instructor = result

            instructor.name = name
            instructor.qualification = qualification

            db.session.commit()

        except Exception:
            print(Exception)
            abort(422)

        return jsonify({
            'message': True,
            'instructor_id': index,
            'instructor_name': name,
            'instructor_qualification': qualification
        })


    @app.route("/api/course/<int:index>", methods=['DELETE'])
    @requires_auth('delete:instructor')
    def delete_course_json(index):
        try:
            result = db.session.query(Course).filter(Course.id == index)
            result = result[0]

            db.session.delete(result)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            print(e)
            abort(404)

        finally:
            db.session.close()

        return jsonify({
            "success": True,
            'message': 'course has been deleted'
        })


    '''
        function for deleting a specific instructor based on its index.

        returns:
            it will returns JSON object that contains the name of the deleted instructor.
    '''


    @app.route("/api/instructor/<int:index>", methods=['DELETE'])
    @requires_auth('delete:instructor')
    def delete_instructor_json(index):
        try:
            result = db.session.query(Instructor).filter(
                Instructor.id == index)
            result = result[0]
            name = result.name

            db.session.delete(result)
            db.session.commit()

        except Exception as e:
            abort(404)

        finally:
            db.session.close()

        return jsonify({
            "success": True,
            'message': 'instrcutor has been deleted successfully',
            'instuctor': name
        })


    '''

    error handling
    using @app.errorhandler

    '''


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request, The server cannot or will not process the request due to an apparent client error."
        }), 400


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found, The requested resource could not be found but may be available in the future."
        }), 404


    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity, The request was well-formed but was unable to be followed due to semantic errors."
        }), 422


    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500


    @app.errorhandler(AuthError)
    def handle_auth_error(exciption):
        response = jsonify(exciption.error)
        response.status_code = exciption.status_code
        return response


    print(__name__, flush=True)

    if __name__ == '__main__':
        if ENV == 'dev':
            app.run(host='127.0.0.1', port=5000, debug=True)
        else:
            app.run(debug=False)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
