from app import app, db, models

#needs to return a sorted list of the suggestions
def get_suggestions(pint_obj, pinid, desc, purl)):
    #check if we were passed an empty object (look it up on macys)
    if desc == None:
        #add a new pintrest pic obj
        u = models.pintrest_picture(pintrest_ID=pinid, pin_desc = desc picture_URL=purl)
        db.session.add(u)
        db.session.commit()
    #now we know the obj exists, so lets find some suggestions
    
    