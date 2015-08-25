# Save your Yahoo Pipes definitions

You can use this Python script to download your published Yahoo Pipes definitions as JSON files. Any pipes you created that are not published will be ignored.

Follow these steps:

Clone this repo and change to the created directory:

    git clone https://github.com/yaph/yahoo-pipes-dl.git
    cd yahoo-pipes-dl

Create a virtualenv (optional) with either of these 2 commands:

    pyvenv /your/virtualenvs/yahoo-pipes-dl  # Python 3 command
    mkvirtualenv --python=/usr/bin/python3 yahoo-pipes-dl # virtualenvwrapper command

Install the requirements:

    pip install -r requirements.txt

Find out your Yahoo Pipes user id by going to http://pipes.yahoo.com/pipes/person.info. You need to be logged in. The user id is the value of the `guid` parameter of the redirected URL.

Run `ypdl.py` providing your Yahoo Pipes user id as an argument.

    ypdl.py YOURGUID

Depending on the number of published pipes this may take a while. For each saved pipe definition a status message is printed.