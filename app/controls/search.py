from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify,json
from sqlalchemy.orm import load_only
from app.models.user_mod import User
from app import db
import sys
mod_user = Blueprint('users',__name__)
mod_perform_search = Blueprint('search',__name__)

@mod_perform_search.route('/search',methods = ["GET","POST"])
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
    searchstring = request.args["searchString"]
    tempArr=User.query.with_entities(User.id,User.name,User.handle)
    searchArrayUser=list(map(lambda x:{"id":x[0],"name":x[1],"handle":x[2]},tempArr))

    resultNames = quicksearch(searchstring,searchArrayUser,8, lambda x: x["name"])
    resultHandles = quicksearch(searchstring,searchArrayUser,8, lambda x: x["handle"])

    FinalResult = resultNames+resultHandles
    removeDuplicates(FinalResult,lambda x: x["id"],lambda x: x["distance"])

    resultUsers = sorted(FinalResult,key = lambda x: x["distance"])[:8]

        # searchArrayCircle=circle.query.with_entities(circle.id,circle.name)
        # keyCircle = lambda x: x[1]
        # resultCircles = quicksearch(searchstring,searchArrayCircle,8,keyCircle);
        #
        # searchArrayTopic=topics.query.with_entities(topic.id,topic.name)
        # keyTopic = lambda x: x[1]
        # resultTopics = quicksearch(searchstring,searchArrayTopics,8,keyTopic);
    print(resultUsers)
    return json.dumps({"searchResults":resultUsers})
