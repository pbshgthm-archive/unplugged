from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, jsonify,json
from sqlalchemy.orm import load_only
from app.models.user_mod import User
from app.models.circle_mod import Circle
from app.models.archive_mod import Archive
from app import db
from app.controls.frame_cont import t
import sys
mod_user = Blueprint('users',__name__)
mod_perform_search = Blueprint('search',__name__)
p = []
for i in t:
    a = {}
    a['name'] = t[i]
    a['id'] = i
    p.append(a)
print(p)
@mod_perform_search.route('/search',methods = ["POST"])
def perform_search():
    def splitPairs(string) : # auxilliary function to build immutable sets of pairs of consecutive characters
        return {frozenset((string[i],string[i+1])) for i in range(len(string)-1)}

    def distance2(s1,s2): # the custom distance function
        s1 = splitPairs(s1)
        s2 = splitPairs(s2)
        return abs( len(s1.union(s2)) - len(s1.intersection(s2)) ) # the distance metric

    def quicksearch(s1,arr,size = 8,keyfunc = None): # composing mapping and finding distance
        lst = list(map(lambda x: dict(x,**{"distance": distance2(s1,keyfunc(x))}),arr))
        print(lst)
        return sorted(lst,key = lambda x: x["distance"])[:size]

    def removeDuplicates(arr,keyname,keyvalue ):
        from itertools import combinations
        toremove = []
        for i in combinations(arr,r=2):
            if keyname(i[0]) == keyname(i[1]):
                toremove.append((lambda x: x[0] if keyvalue(x[0])< keyvalue(x[1]) else x[1])(i))
        for i in toremove:
            arr.remove(i)

    a = request.json
    searchstring = a['string'];
    tempArr=User.query.with_entities(User.id,User.name,User.handle,User.picture)
    searchArrayUser=list(map(lambda x:{"id":x[0],"name":x[1],"handle":x[2],"image":x[3]},tempArr))
    resultNames = quicksearch(searchstring.lower() ,searchArrayUser,15, lambda x: x["name"].lower())
    resultHandles = quicksearch(searchstring.lower(),searchArrayUser,15, lambda x: x["name"].lower())

    FinalResult = resultNames+resultHandles
    removeDuplicates(FinalResult,lambda x: x["id"],lambda x: x["distance"])

    resultUsers = sorted(FinalResult,key = lambda x: x["distance"])[:15]



    
    tempArr= Archive.query.with_entities(Archive.id,Archive.title,Archive.image)
    searchArrayCircle=list(map(lambda x:{"id":x[0],"title":x[1],"image":x[2]},tempArr))
    resultNames = quicksearch(searchstring.lower(),searchArrayCircle,15, lambda x: x["title"].lower())

    FinalResult = resultNames
    removeDuplicates(FinalResult,lambda x: x["id"],lambda x: x["distance"])

    resultCircles = sorted(FinalResult,key = lambda x: x["distance"])[:15]

    
###    searchArrayTopic=topics.query.with_entities(topic.id,topic.name)
   # keyTopic = lambda x: x[1]
    resultTopics = quicksearch(searchstring.lower(),p,15,lambda x: x["name"].lower());
    r = sorted(resultTopics,key = lambda x:x["distance"])[:15]
    return jsonify([resultUsers,resultCircles,resultTopics])
                   #,resultCircles[::-1],resultTopics[::-1]])
