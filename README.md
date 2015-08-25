# Save your Yahoo Pipes definitions

You can use this Python script to download your published Yahoo Pipes definitions as JSON files. Any pipes you created that are not published will be ignored.

Follow these steps:

* Clone this repo.
* Create a virtualenv.
* Install the requirements.
* Find out your user id by going to http://pipes.yahoo.com/pipes/person.info. It is the value of the `guid` parameter of the redirected URL.
* Run ypdl.py providing your Yahoo Pipes user id as an argument.

Depending on the number of published pipes this may take a while. For each saved pipe definition a status message is printed.