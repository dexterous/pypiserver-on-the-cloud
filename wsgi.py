import errno
import os
import os.path as path

import pypiserver


CWD = os.getcwd()
PACKAGES = path.expanduser('~/data')
HTPASSWD = path.join(CWD, 'htpasswd')

try:
    os.makedirs(PACKAGES)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

application = pypiserver.app(root=PACKAGES, password_file=HTPASSWD)
