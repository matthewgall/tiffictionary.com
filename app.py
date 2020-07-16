#!/usr/bin/env python3

import os, logging, argparse, json, datetime
import requests, redis
from bottle import route, request, response, redirect, hook, error, default_app, view, static_file, template

def set_content_type(fn):
	def _return_type(*args, **kwargs):
		if request.headers.get('Accept') == "application/json":
			response.headers['Content-Type'] = 'application/json'
		if request.headers.get('Accept') == "text/plain":
			response.headers['Content-Type'] = 'text/plain'
		if request.method != 'OPTIONS':
			return fn(*args, **kwargs)
	return _return_type

def enable_cors(fn):
	def _enable_cors(*args, **kwargs):
		response.headers['Access-Control-Allow-Origin'] = '*'
		response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
		response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

		if request.method != 'OPTIONS':
			return fn(*args, **kwargs)
	return _enable_cors
		
@error('404')
@error('403')
def returnError(code, msg, contentType="text/plain"):
	response.status = int(code)
	response.content_type = contentType
	return template('error')

@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, root='views/static')
		
@route('/version')
def version():
	try:
		dirname, filename = os.path.split(os.path.abspath(__file__))
		del filename
		f = open(os.getenv('VERSION_PATH', dirname + '/.git/refs/heads/master'), 'r')
		content = f.read()
		response.content_type = 'text/plain'
		return content
	except:
		return "Unable to open version file."

@route('/definition/<word>')
@route('/definition/<word>.<ext>')
@set_content_type
@enable_cors
def loadWord(word, ext='html'):
	try:
		if word == "":
			raise ValueError
		if not ext in ["html","json"]:
			raise ValueError
	except ValueError:
		return returnError(404, "Not Found", "text/html")

	if ext in ["json"]:
		response.content_type = 'application/json'

	# We make a request to get information
	try:
		data = r.get(word.lower().replace(' ', '+'))
		data = json.loads(data)
	except:
		return returnError(404, "Not Found", "text/html")
	
	if response.content_type == 'application/json':
		return json.dumps({
			'results': {
				'name': word.lower(),
				'data': data,
			}
		})
	else:
		return template('word', {
			'name': word.lower(),
			'data': data
		})

@route('/', ('GET', 'POST'))
def index():
	if request.method == "POST":
		word = request.forms.get('word', '')

		if word != '':
			return redirect("/definition/{}".format(word.lower().replace(' ', '+')))
		else:
			return returnError(404, "We were not able to figure out what you were asking for", "text/html")
	
	return template("home")

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	# Server settings
	parser.add_argument("-i", "--host", default=os.getenv('HOST', '127.0.0.1'), help="server ip")
	parser.add_argument("-p", "--port", default=os.getenv('PORT', 5000), help="server port")

	# Redis settings
	parser.add_argument("--redis", default=os.getenv('REDISTOGO_URL', os.getenv('REDIS', 'redis://localhost:6379/0')), help="redis connection string")

	# Bootstrap settings
	parser.add_argument("--skipboot", help="skip bootstrapping of definitions to redis", action="store_true")

	# Verbose mode
	parser.add_argument("--verbose", "-v", help="increase output verbosity", action="store_true")
	args = parser.parse_args()

	if args.verbose:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO)
	log = logging.getLogger(__name__)

	try:
		r = redis.StrictRedis.from_url(args.redis)
	except:
		log.error("Unable to connect to redis at {}".format(args.redis))

	# Now to bootstrap redis
	if args.skipboot != True:
		log.info("Bootstrapping redis...")
		try:
			for filename in os.listdir('definitions'):
				with open('definitions/{}'.format(filename), 'r') as f:
					content = f.read()
					r.set('{}'.format(filename.split('.')[0]), content)				
		except:
			pass

	try:
		app = default_app()
		app.run(host=args.host, port=args.port, server='tornado')
	except:
		log.error("Unable to start server on {}:{}".format(args.host, args.port))