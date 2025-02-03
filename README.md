# Number Classification API
This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact. The API is built using Django REST Framework (DRF).

## Description
This API provides details about the number you input, including:

* Whether the number is a prime number
* Whether it is a perfect number
* Its mathematical properties (Armstrong, odd, even).
* The sum of its digits.
* A fun fact from [Numbers API](http://numbersapi.com)

## Technologies Used
* **Python:** Programming Language
* **Django REST Framework(DRF):** Web Framework for building the API
* **Django:** Web Framework for managing the project
* **Numbers API:** For fetching fun facts about numbers

## Installation
1. Make sure you have python3 installed, then clone this repository.
2. Set up a virtual environment for this project to avoid unnecessary conflicts and isolate this projects dependencies.

  Navigate to the directory you cloned the code to
  '''
  cd project_dir
  '''
  Create a virtual environment
  '''python
  python3 -m venv env
  '''
3. Install Dependencies
  '''
  pip install -r requirements.txt
  '''
4. Create your .env file and place secrets in it(SECRET_KEY and ALLOWED_HOSTS)

5. Apply database migrations(within the django project directory)
   '''python
   python manage.py migrate
   '''
6. Run the Development server
   '''python
   python manage.py runserver
  '''
The API will be accessible at http://localhost:8000

To make the API publicly accessible you will have to configure gunicorn and nginx(for reverse proxy) on a public cloud virtual machine.

## Usage
To classify a number, send a *GET* request to the /api/classify-number endpoint with a number query parameter.

Example Request:
'''
GET http://your-api-url/api/classify-number?number=371
'''

Example Respone(200 OK):
'''
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
'''

Example Response(400 Bad Request):
'''
{
    "number": "alphabet",
    "error": true
}
'''

## Response Format
* **200 OK:** Returns the classification details in JSON format.
* **400 Bad Request:** If the input is not a valid integer.
   
   
