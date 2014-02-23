from app import app, db, models, sorter, htmlhelper
from flask import request
import json

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

@app.route('/')
@app.route('/index')
def index():
    return '<meta http-equiv="refresh" content="0; url=https://github.com/SebastianMerz/pincys" />'

@app.route('/get_suggestions/', methods=['POST', 'OPTIONS'])
@crossdomain(origin="*")
def process_input():
    #basically, call the db on pin_id, find the suggestions that result, sort them then 
    #if there are no suggestions, search macys api
    
    #get info from the request
    data = json.loads(request.data)
    print 'Attempting to run requst'
    
    print data
    pinid = data['pinid']
    if "description" in data:
        desc = data['description']
    else:
        desc = ''
    picurl = data['picurl']
    
    #get item in the db or none if its not there
    picobj = models.pintrest_picture.query.filter_by(pintrest_ID=pinid).first()
    
    #get the suggestion objects etc
    sorted_sugg_list = sorter.get_suggestions(picobj, pinid, desc, picurl)
    
    #convert it to html and return it (sebastian do this)
    print sorted_sugg_list
    return htmlhelper.get_suggest_html(sorted_sugg_list)

@app.route('/add_turksuggest/')
def addTS():
    #this takes the result from a hit and adds it to the database,
    #if the suggestion already exists, modifies rating accordingly.
    return "Not implemented."


@app.route('/send_top_to_turk/', methods=['POST'])
def execute():
    #goes to mTurk and submits the top 50 suggestion_pinid by viewcount
    #this gets matching ID's for the hits.
    
    if request.form['KEY'] != youSUREyouWANTtoSPENDmoney: return "401"
    
    totallist = models.suggestion.query.order_by(suggestion.view_count)
    k = 0
    for sugg in totallist:
        if sugg.mrating_count < 2 and k < 50:
            pinim_url = sugg.pintrest_id.picture_URL
            pin_desc = sugg.pintrest_id.pin_desc
            new_sugg_hit(pinim_url, pin_desc)
            k += 1

@app.route('/send_ratings_to_turk/', methods=['POST'])
def execute():
    #goes to mTurk and submits the top 500 suggestions to be rated.
    if request.form['KEY'] != youSUREyouWANTtoSPENDmoney: return "401"
    
    totallist = models.suggestion.query.order_by(suggestion.view_count)
    k = 0
    for sugg in totallist:
        if sugg.mrating_count < 2 and k < 500:
            pinim_url = sugg.pintrest_id.picture_URL
            pin_desc = sugg.pintrest_id.pin_desc
            macyimurl = sugg.picture_URL
            macytitle = sugg.product_title
            new_rate_hit(pinim_url, pin_desc, macyimurl, macytitle)
            k += 1
            
@app.route('/rate/<id>/<rating>') #id, rating
def rate(id,rating):
    sugg = models.suggestion.query.get(idval)
    oldrtg = sugg.user_rating
    oldcount = sugg.urating_count
    newrtg = (oldrtg * oldcount + rating) / (oldcount + 1 )
    sugg.user_rating = newrtg
    db.session.commit()
    
