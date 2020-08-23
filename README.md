![](https://github.com/mdqara/FSND-Capstone/blob/master/application/static/images/screenshot.png?raw=true)

# People's Academy 📚

This is an application of full stack web development for the capstone project in Udacity FSND, the stack includes: flask, SQLAlchemy, Auth0, Bootstrap. Basically it is a web application that let instructors to add themselves and others and create course that students can view.

## Live App:

You can check the live app that deployed in Heroku on the like: https://fsnd-capstone-project.herokuapp.com/	



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

- ### Endpoints

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