# Flashcard Application using Django REST API
Using this project we can render own flashcard app and maintain the data as per the requirement.
To develop this project I have used Django and also used ajax to send a RESTFUL API request.

## Installation

To run this code you would need:

1. Download/ Clone the project
```git
  git clone https://github.com/saras108/Flashcard
```

2. Get inside the downloaded folder
```git
    cd Flashcard
```

3. Create a virtual environment
```python3
  python -m venv env
```

4. Activate the virtual environment
```
  source env/bin/activate (for linux)
  .\env\Scripts\activate (for window)
```

5. Install the required packages
```python3
  pip3 install -r requirements
``` 

6. Get into the project project
```git
  cd flashcard
``` 

7. Make a connection to database
```python3
    python .\manage.py makemigrations
```
```python3
    python .\manage.py migrate
```

8. Run the server
```python3
    python .\manage.py runserver
```

### Enjoy The System.