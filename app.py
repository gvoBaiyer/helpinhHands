import datetime

from flask import Flask , request , jsonify
# from flask_mysqldb import MySQL
from newsapi import NewsApiClient
from predicthq import Client

import requests
import json

app = Flask(__name__)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'rtd'
# app.config['MYSQL_PASSWORD'] = 'rtd_password'
# app.config['MYSQL_DB'] = 'RealTimeDisasters'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#
# mysql = MySQL(app)

with app.app_context():
	with open('conf.json') as file:
		j = json.loads(file.read())
		newsapikey = j['newsapikey']
		hazardskey = j['hazardskey']
		demokey = j['demokey']


@app.route('/news' , methods = ['GET'])
def news() :
	global newsapikey
	newsapi = NewsApiClient(api_key = newsapikey)
	params = request.args
	if 'country' in params :
		try : response = newsapi.get_top_headlines(q = 'hazard' , country = params['country'])
		except ValueError as e : response = { "articles" : [] }
	else :
		from_date = (datetime.datetime.now() - datetime.timedelta(days = 7)).date()
		response = newsapi.get_everything(q = "hazard" , language = 'en' , from_param = str(from_date) ,
		                                  sort_by = 'popularity')
	return jsonify(articles = response['articles'])


@app.route('/demo' , methods = ['GET'])
def demo() :
	global demokey
	params = request.args
	x = params.get('x')
	y = params.get('y')
	bufferUnits = 'esriKilometers'
	bufferRadi = 15
	url = "https://geoenrich.arcgis.com/arcgis/rest/services/World/geoenrichmentserver/GeoEnrichment/enrich"

	payload = \
		"f=json" \
		f"&token={demokey}" \
		"&inSR=4326" \
		"&outSR=4326" \
		"&returnGeometry=true" \
		f"&studyAreas=%5B%0A%20%20%7B%0A%20%20%20%20%22geometry%22%3A%7B%0A%20%20%20%20%20%20%22x%22%3A{x}7%2C%0A%20%20%20%20%20%20%22y%22%3A{y}%0A%20%20%20%20%7D%0A%20%20%7D%0A%5D" \
		f"&studyAreasOptions=%7B%0A%20%20%22areaType%22%3A%22RingBuffer%22%2C%0A%20%20%22bufferUnits%22%3A%22{bufferUnits}%22%2C%0A%20%20%22bufferRadii%22%3A%5B{bufferRadi}%5D%0A%7D" \
		"&dataCollections=KeyGlobalFacts"

	headers = {
	  'Content-Type' :    "application/x-www-form-urlencoded" ,
	  # 'User-Agent' :      "PostmanRuntime/7.18.0" ,
	  'Accept' :          "*/*" ,
	  'Cache-Control' :   "no-cache" ,
	  # 'Postman-Token' :   "49fc9b08-420e-401b-acf6-e51e6946f2d6,8fd66cfb-526b-4cfb-9c43-424105f4898f" ,
	  'Host' :            "geoenrich.arcgis.com" ,
	  # 'Accept-Encoding' : "gzip, deflate" ,
	  # 'Content-Length' :  "572" ,
	  'Connection' :      "keep-alive" ,
	  'cache-control' :   "no-cache"
	  }

	response = requests.request("POST" , url , data = payload , headers = headers)
	response = response.json()
	response = response['results'][0]['value']['FeatureSet'][0]['fields']
	return jsonify(response)


# todo

@app.route('/hazards' , methods = ['GET'])
def hazards() :
	global hazardskey
	phq = Client(access_token = hazardskey)
	keeps = ['scope', 'start', 'active', 'timezone', 'title', 'description', 'country', 'labels', 'location']
	params = request.args
	# token = 'VCAUrlQIK04kDFk6AE6_hvR-922LbO8gtrPaUCWN'
	# url = 'https://api.predicthq.com/v1/events/?category=disasters&offset=10&state=active'

	# if 'country' in params : url += f'&country={params["country"]}'
	# if 'from_date' in params : url += f'%start.gt={params["from_date"]}'
	#
	# # response = requests.get(url , headers = { 'Authorization' : f'Bearer {token}' })
	# result = response.json()['results']
	# result = sorted(result , key = lambda r : r['rank'])
	final_result = []
	for j in phq.events.search(category = 'disasters', state = 'active', country = params.get('country')):
		obj = {k: v for k,v in j.items() if k in keeps}
		final_result.append(obj)
	return jsonify(final_result)


# @app.route('/ong' , methods = ['GET' , 'POST'])
# def ong() :
# 	if request.method == 'POST':
# 		params = request.get_json()
# 		name = params.get('name')
# 		description = params.get('description')
# 		url = params.get('url')
# 		phone = params.get('phone')
# 		if not name or not url or not phone :
# 			return 'Fields missing' , 400
# 		cur = mysql.connection.cursor()
# 		cur.execute("INSERT INTO ong(name, description, url, phone) VALUES (%s, %s, %s, %s)" ,
# 		            (name , description , url , phone))
# 		mysql.connection.commit()
# 		cur.close()
# 		return 200
# 	elif request.method == 'GET':
# 		pass
# 	return 405




if __name__ == '__main__' :
	app.run()
