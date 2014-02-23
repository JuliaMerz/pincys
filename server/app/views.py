from app import app, db, models, sorter
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
    sorted_sugg_list = get_suggestions(picobj, pinid, desc)
    
    #convert it to html and return it (sebastian do this)
    return get_html(sorted_sugg_list)

@app.route('/add_turksuggest/')
def addTS():
    return "Not implemented."