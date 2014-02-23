from app import app, db, models, sorter, htmlhelper
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return '<meta http-equiv="refresh" content="0; url=https://github.com/SebastianMerz/pincys" />'

@app.route('/get_suggestions/', methods=['POST'])
def process_input():
    #basically, call the db on pin_id, find the suggestions that result, sort them then 
    #if there are no suggestions, search macys api
    
    #get info from the request
    pinid = request.form['ID']
    desc = request.form['DESCRIPTION']
    picurl = request.form['PICURL']
    
    #get item in the db or none if its not there
    picobj = models.pintrest_picture.query.filter_by(pintrest_ID=pinid).first()
    
    #get the suggestion objects etc
    sorted_sugg_list = get_suggestions(picobj, pinid, desc, picurl)
    
    #convert it to html and return it (sebastian do this)
    return get_suggest_html(sorted_sugg_list)

@app.route('/send_top_to_turk/', methods=['POST'])
def execute():
    #goes to mTurk and submits the top 50 suggestion_pinid by viewcount
    #this gets matching ID's for the hits.
    
    if request.form['KEY'] != youSUREyouWANTtoSPENDmoney: return "401"
    
    totallist = models.suggestion.query.order_by(suggestion.view_count)
    
    for sugg in totallist:
        k = 0
        if sugg.mrating_count < 2 && k < 50:
            pinim_url = sugg.pintrest_id.picture_URL
            pin_desc = sugg.pintrest_id.pin_desc
            new_sugg_hit(pinim_url, pin_desc)
            k += 1

@app.route('/send_ratings_to_turk/', methods['POST'])
def execute():
    #goes to mTurk and submits the top 500 suggestions to be rated.





