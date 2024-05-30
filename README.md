# tutorial_2024
# class code for web server computing 
https://www.django-rest-framework.org/tutorial/1-serialization/

Setting up a new environment
Before we do anything else we'll create a new virtual environment, using venv. This will make sure our package configuration is kept nicely isolated from any other projects we're working on.

python3 -m venv env
source env/bin/activate
Now that we're inside a virtual environment, we can install our package requirements.

pip install django
pip install djangorestframework
pip install pygments  # We'll be using this for the code highlighting
