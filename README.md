![](https://github.com/mdqara/FSND-Capstone/blob/master/application/static/images/screenshot.png?raw=true)

# People's Academy 📚

This is an application of full stack web development for the capstone project in Udacity FSND, the stack includes: flask, SQLAlchemy, Auth0, Bootstrap. Basically it is a web application that let instructors to add themselves and others and create course that students can view.

## Live App

You can check the live app that deployed in Heroku on the like: https://fsnd-capstone-project.herokuapp.com/	



## Table of content

[TOC]

## Getting Started



### Installing the project

#### Project dependencies

To try this project you need to install the following:

- Python3 (https://www.python.org/) 
- Code Editor Visual Studio Code (https://code.visualstudio.com/). 
- PostgreSQL from https://www.postgresql.org/

Then download the project from the get download button above, and open the project directory in the command line the type: 

```shell
pip3 install pipenv
```

then activate your shell using:

```
pipenv shell
```

after that install all dependencies using the command:

```
pipenv install -r ./requirements.txt
```



#### Running the serve on local environment

After installing all dependencies, type the following the run the server:

```
flask run --reload
```



## API Reference

### Endpoints

- GET '/api/courses'

- GET '/api/course/int:index'

- GET '/api/instructor'

- GET '/api/instructor/int:index'

- POST '/api/courses'

- POST '/api/instructor'

- PATCH '/api/course/int:id'

- PATCH '/api/instructor/int:id'

- DELETE '/api/course/int:id'

- DELETE '/api/instructor/int:id'

  

#### GET '/api/courses'

- Fetches all courses.
- Returns list of courses ordered by id.

```
{
  "courses": [
    {
      "desc": "Hone specialized skills in Data Product Management and learn how to model data, identify trends in data, and leverage those insights to develop data-backed product strategy.", 
      "duration": "3", 
      "id": 2, 
      "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/1rJDmku9XmR3FlxsyJ8JVc/a6442a0ef3d7200af03b9107e15f894c/MAND_Syllabus.jpg", 
      "instructor": "Mohammad Ali", 
      "name": "Applying Data Science to Product Management"
    }
  ], 
  "success": true
}
```



#### GET '/api/course/int:index'

- Fetches  specific course based on its index
- A JSON object that contains the course information like the following:

```
{
  "course": {
    "desc": "Hone specialized skills in Data Product Management and learn how to model data, identify trends in data, and leverage those insights to develop data-backed product strategy.", 
    "duration": "1", 
    "id": 8, 
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/4FCXQsUpzftEgEdFGqQmXE/8ba5c2e69a5b036d4dafe1ae5803fe60/syllabus__8_.jpg", 
    "instructor": "Mohammad Ali", 
    "name": "Applying Data Science to Product Management"
  }, 
  "message": true
}
```



#### GET '/api/instructor'

- Fetches all instructors.
- Returns list of instructors ordered by id.

```
{
  "courses": [
    {
      "id": 1,
      "name": "Khaled Omar",
      "qualification": "Python Developer"
    },
    {
      "id": 2,
      "name": "Mohammad Ali",
      "qualification": "UX Designer"
    }
  ],
  "success": true
}

```



#### GET '/api/instructor/int:index'

- Fetches  specific instructor based on its index
- A JSON object that contains the course information like the following:

```
{
  "courses": {
    "id": 9, 
    "name": "Khaled Omar", 
    "qualification": "Python Developer"
  }, 
  "success": true
}
```



#### POST '/api/course'

- Posting a course using the endpoint

- post request using postman will be on the form of the following:

  ```
  {
      "desc": "Gain foundational data skills applicable to marketing. Collect and analyze data, model marketing scenarios, and communicate your findings with Excel, Tableau, Google Analytics, and Data Studio.",
      "duration": "3",
      "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/1rJDmku9XmR3FlxsyJ8JVc/a6442a0ef3d7200af03b9107e15f894c/MAND_Syllabus.jpg",
      "name": "Become a Marketing Analyst",
      "instructor": "Mohammad Ali"
  }
  ```

- Returns confirmation JSON object.

  ```
  { "course_name": "Become a Marketing Analyst", "message": true }
  ```

  

#### POST '/api/instructor'

- Posting a instructor using the endpoint

- post request using postman will be on the form of the following:

  ```
  {
      "name": "Mohammad Ali",
      "qualification" : "Python Developer"
  }
  ```

- Returns confirmation JSON object.

  ```
  { "message": true, "name": "Mohammad Ali" }
  ```

  

#### PATCH '/api/course/int:id'

- Patching a course using the endpoint

- PATCH request using postman will be on the form of the following:

  ```
  {
      "desc": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.",
      "duration": "2",
      "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/219UNjX4r925AbuYRhbFYa/cc41f3d6d2a53d23637335a7a81baa1b/syllabus__6_.jpg",
      "name": "Learn SQL+",
      "instructor": "Omar Jamal"
  }
  ```

- Returns confirmation JSON object.

  ```
  {
    "course_id": 8, 
    "description": "Learn SQL, the core language for Big Data analysis, and enable insight-driven decision-making and strategy for your business.", 
    "duration": "2", 
    "image_link": "https://www.udacity.com/www-proxy/contentful/assets/2y9b3o528xhq/219UNjX4r925AbuYRhbFYa/cc41f3d6d2a53d23637335a7a81baa1b/syllabus__6_.jpg", 
    "instructor": "Omar Jamal", 
    "message": true, 
    "name": "Learn SQL+"
  }
  
  ```

  

#### PATCH '/api/instructor/int:id'

- Patching an instructor using the endpoint

- PATCH request using postman will be on the form of the following:

  ```
  {
      "name": "khaled",
      "qualification" : "SWIFT Developer"
  }
  ```

- Returns confirmation JSON object.

  ```
  {
    "instructor_id": 10, 
    "instructor_name": "KHALED", 
    "instructor_qualification": "SWIFT Developer", 
    "message": true
  }
  ```

  

#### DELETE '/api/course/int:id'

- Delete a course using the endpoint with specific index.

- Returns confirmation JSON object.

  ```
  {
    "message": "course has been deleted", 
    "success": true
  }
  ```

  

#### DELETE '/api/instructor/int:id'

- Delete a course using the endpoint with specific index.

- Returns confirmation JSON object.

  ```
  {
    "instuctor": "Khaled Omar", 
    "message": "instrcutor has been deleted successfully", 
    "success": true
  }
  ```

  

## Authentication

- This app can be run at: https://fsnd-capstone-project.herokuapp.com/
- To sign up or login: https://fsnd-capstone-project.herokuapp.com/login

- there are two users:
  1. **Student: who has the following:**
     - get:course
  2. **Instructor: who has the following permissions:**
     - get:course
     - get:instructor
     - post:course
     - post:instructor
     - patch:course
     - patch:instructor
     - delete:course
     - delete:instructor



## Deployment

This app is deployed on Heroku. For deployment, you need to:

- Install Heroku CLI and login to Heroku on the terminal
- create a [.env](https://github.com/mdqara/FSND-Capstone/blob/master/.env) file and declare all your variables in the file
- Install gunicorn

```
    pip install gunicorn
```

- Create a [Procfile](https://github.com/mdqara/FSND-Capstone/blob/master/Procfile) and add the line below. The Procfile instructs Heroku on what to do. Make sure that **your app** is housed in **[__init__.py](https://github.com/mdqara/FSND-Capstone/blob/master/application/__init__.py)**

```
web: gunicorn wsgi:app 
```

- Install the following requirements

```
    pip install flask_script
    pip install flask_migrate
    pip install psycopg2-binary
```

- Freeze your requirements in the [requirements.txt](https://github.com/mdqara/FSND-Capstone/blob/master/requirements.txt) file

```
    pip freeze > requirements.txt
```

- Link your GitHub repo with Heroku dashboard
- Then, all the Variables in Heroku under settings, you can visit this video for more [instructions](https://www.youtube.com/watch?v=FKy21FnjKS0).

```
    # This should already exist from the last step
    DATABASE_URL
    # Get these from Auth0
    AUTH0_DOMAIN
    ALGORITHMS
    API_AUDIENCE
```

- Push any changes to your GitHub Repository then it will deployed on Heroku.



## Testing

Make sure to create database called `academy_test` and restore a copy from pre-created database with pre-defined information, using the following commands:

```
dropdb academy_test
createdb academy_test
psql academy_test < academy.psql
python test_app.py
```

