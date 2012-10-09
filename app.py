#!/usr/bin/python
from google.appengine.ext.webapp.util import run_wsgi_app
from config import ROOT_DIRECTORY

import os, sys
sys.path.append(os.path.join(ROOT_DIRECTORY,"packages"))
sys.path.append(os.path.join(ROOT_DIRECTORY,"packages","Flask"))
from application import app

run_wsgi_app(app)