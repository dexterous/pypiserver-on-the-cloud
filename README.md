This is a bare bones application that hosts an instance of pypiserver on the cloud.

Authentication is configured in the `htpasswd` file; currently a single user `foo` exists with password `bar`.

Platforms supported
===================

dotcloud
--------

Runs as a single python3.2 (the latest of version dotcloud supports at the time of this writing) service that hosts an instance of pypiserver.

Uploaded packages are stored in the dotcloud instance persistent directory, `~/data`. AFAIK, this will not scale as `~/data` is not replicated across instances.

heroku
------
Runs the WSGI application in `wsgi.py` using the bottle runner embedded in `pypiserver` in the `web` process.

Uploaded packages are stored in `~/data`. Since heroku does not persist any of the directories on a dyno, you will lose packages between `heroku push`s. Need to figure out a better solution for this.