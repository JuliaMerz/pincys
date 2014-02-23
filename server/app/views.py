from app import app, db
from flask import request
@app.route('/')
@app.route('/index')
def index():
    return '<meta http-equiv="refresh" content="0; url=https://github.com/SebastianMerz/pincys" />'

@app.route('/get_suggestions/<pin_id>', methods=['POST'])
def process_input(pin_id):
    #basically, call the db on pin_id, find the suggestions that result, sort them then 
    #if there are no suggestions, search macys api
    pinid = request.form['ID']
    desc = request.form['DESCRIPTION']
    
    return 'HTMLGOESHERE'

@app.route('/add_turksuggest/')
def addTS():
    return "NOT IMPLEMENTED YET"