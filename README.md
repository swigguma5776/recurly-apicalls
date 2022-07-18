# recurly-apicalls
Building a simple flask framework that fetches user information from the Recurly API endpoints integrating the Recurly library 


GET STARTED HERE:

If you want this application to run locally, clone this repo, and do the following:

    cd into the cloned repo recurly_apicalls

Create a Python virtual env:

    python -m venv <name_of_your_env>

Activate Python virtual env AND set Flask ENV variables in terminal/CMD:

  Mac

    source <name_of_your_env>/bin/activate
    export FLASK_APP=apicalls.py
    export FLASK_ENV=development

  Windows

    <name_of_your_env>\Scripts\activate.bat
    set FLASK_APP=apicalls.py
    set FLASK_ENV=development

Install dependencies:

    pip install -r requirements.txt
    
    or
    
    pip3 install -r requirements.txt

Start dev server:

    flask run
