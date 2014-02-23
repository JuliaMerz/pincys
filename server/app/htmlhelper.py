#magic function that takes in a sorted list of suggestion objects and returns html
from flask import render_template

def get_suggest_html(sorted_sugg_list):
    return render_template("extension.html", suggestions=sorted_sugg_list)    
