from app import app, db, models
import random
from apihelper import macy_search
from rake import rake

#needs to return a sorted list of the suggestions,
#returns None if no suggestions can be found
def get_suggestions(pint_obj, pinid, desc, purl):
        
    #check if we were passed an empty object (look it up on macys)
    if pint_obj == None:
        #add a new pintrest pic obj
        pint_obj = models.pintrest_picture(pintrest_ID=pinid, pin_desc = desc, picture_URL=purl)
        db.session.add(pint_obj)
        db.session.commit()
        
    #now we know the obj exists, so lets find some suggestions
    currsug = list(pint_obj.suggestions.all())
    listwords = rake(desc)
    while len(currsug) < 5 and i < len(listwords)-1:
        i = 0
        vals = macy_search(listwords[i] + listwords[i+1]);
        if vals[0] != 0: 
            #this means we got data back
            k = 1
            #create new suggestion obj
            while vals[k] != None and k < 16:
                s = models.suggestion(pintrest_id=pint_obj,product_title=vals[k],
                    product_URL=vals[k+1], picture_URL=vals[k+2])
                db.session.add(s)
                db.session.commit()
                currsug.append(s)
                k += 3
        i += 1
    if len(currsug) == 0:
        #we have no suggestions :(
        return None
    weights = [5,4,3,2,1]
    z = 0
    for k in currsug:
        k.sort_val = (k.user_rating * 5 + k.mturk_rating * 3 + weights[z] * 2 + random.randrange(10))
        weights[k] = weight
        k += 1
    currsug.sort(key = lambda k: k.sort_vaL)

    print currsug;
    #need to actually order the suggestions according to their weights
    #higher == better
    return currsug 
    
    
