import os
import wsgi
import pypiserver.bottle as bottle

bottle.run(
    app=wsgi.application,
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000))
)
