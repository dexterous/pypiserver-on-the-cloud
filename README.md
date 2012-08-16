This is a bare bones dotcloud app with a single python3.2 (the latest of version dotcloud supports at the time of this writing)  service that hosts an instance of pypiserver.

Authentication is configured in the `htpasswd` file; currently a single user `foo` exists with password `bar`.

Uploaded packages are stored in the dotcloud instance persistent directory, `~/data`. AFAIK, this will not scale as `~/data` is not replicated across instances.
