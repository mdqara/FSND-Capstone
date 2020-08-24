import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from models import setup_db, db, Course, Instructor
from unittest.mock import patch
from app import create_app


class PeoplesAcademyTestCase(unittest.TestCase):
    """This class represents the PeoplesAcademy test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql://postgres:postgres@localhost:5432/academy_test"
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    """
    ################## Test cases ##################
    """

    # GET REQUESTS #

    def test_get_courses_success(self):
        res = self.client().get('/api/courses')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertEqual(res.status_code, 200)

    def test_get_courses_failure(self):
        res = self.client().get('/api/coooourse')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_get_course_index_success(self):
        res = self.client().get('/api/course/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertEqual(res.status_code, 200)

    def test_get_courses_index_failure(self):
        res = self.client().get('/api/course/999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_get_instructor_success(self):
        res = self.client().get('/api/instructor')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertEqual(res.status_code, 200)

    def test_get_instructor_failure(self):
        res = self.client().get('/api/instructooor')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_get_instructor_index_success(self):
        res = self.client().get('/api/instructor/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertEqual(res.status_code, 200)

    def test_get_instructor_index_failure(self):
        res = self.client().get('/api/instructor/999')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    # POST REQUESTS #

    def test_post_course_success(self):
        res = self.client().post('/api/course',
                                 json={
                                     "desc": "Gain foundational data skills applicable to marketing. Collect and analyze data, model marketing scenarios, and communicate your findings with Excel, Tableau, Google Analytics, and Data Studio.",
                                     "duration": "3",
                                     "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/1rJDmku9XmR3FlxsyJ8JVc/a6442a0ef3d7200af03b9107e15f894c/MAND_Syllabus.jpg",
                                     "name": "Become a Marketing Analyst",
                                     "instructor": "Mohammad Ali"
                                 })
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_post_course_failure(self):
        res = self.client().post('/api/course',
                                 json={
                                     "desc": "Gain foundational data skills applicable to marketing. Collect and analyze data, model marketing scenarios, and communicate your findings with Excel, Tableau, Google Analytics, and Data Studio.",
                                     "duration": "3"
                                 })
        data = json.loads(res.data)
        self.assertEqual(data['error'], 422)
        self.assertEqual(res.status_code, 422)

    def test_post_instructor_success(self):
        res = self.client().post('/api/instructor',
                                 json={
                                     "name": "Mohammad Ali",
                                     "qualification": "Python Developer"
                                 })
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_post_instructor_failure(self):
        res = self.client().post('/api/instructor',
                                 json={
                                     "name": "Mohammad Ali"
                                 })
        data = json.loads(res.data)
        self.assertEqual(data['error'], 422)
        self.assertEqual(res.status_code, 422)

    # PATCHES REQUESTS #
    def test_patch_course_success(self):
        res = self.client().patch('/api/course/2',
                                  json={
                                      "desc": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
                                      "duration": "2",
                                      "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/219UNjX4r925AbuYRhbFYa/cc41f3d6d2a53d23637335a7a81baa1b/syllabus__6_.jpg",
                                      "name": "Learn SQL+",
                                      "instructor": "Omar Jamal"
                                  })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_course_failure(self):
        res = self.client().patch('/api/course/2',
                                  json={
                                      "desc": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
                                      "duration": None
                                  })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_patch_instructor_success(self):
        res = self.client().patch('/api/instructor/2',
                                  json={
                                      "name": "khaled",
                                      "qualification": "SWIFT Developer"
                                  })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

    def test_patch_instructor_failure(self):
        res = self.client().patch('/api/instructor/2',
                                  json={
                                      "qualification": None
                                  })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    # DELETE REQUESTS #

    def test_delete_course_success(self):
        res = self.client().delete('/api/course/2')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_delete_course_failure(self):
        res = self.client().delete('/api/course/999')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)

    def test_delete_instructor_success(self):
        res = self.client().delete('/api/instructor/2')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)

    def test_delete_instructor_failure(self):
        res = self.client().delete('/api/instructor/999')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
