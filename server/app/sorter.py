from app import app, db, models
from apihelper import macy_search
from rake import rake

#needs to return a sorted list of the suggestions
def get_suggestions(pint_obj, pinid, desc, purl)):
        
    #check if we were passed an empty object (look it up on macys)
    if pint_obj == None:
        #add a new pintrest pic obj
        pint_obj = models.pintrest_picture(pintrest_ID=pinid, pin_desc = desc picture_URL=purl)
        db.session.add(u)
        db.session.commit()
        
    #now we know the obj exists, so lets find some suggestions
    currsug = list(pint_obj.suggestions.all())
    listwords = rake(desc)
    while len(currsug) < 5 && i < len(listwords):
        i = 0
        vals = macy_search(listwords[i]);
        if vals[0] != 0: 
            #this means we got data back
            k = 1
            while vals[k] != None && k < 16:
                s = models.suggestion(pintrest_id=pint_obj,picture,product_title=vals[k],
                    product_URL=vals[k+1], picture_URL=vals[k+2])
                currsug.append(s)
                k += 3
        i += 1
    if len(currsug) == 0:
        return None
    #sort suggestions    
    return currsug
    
    