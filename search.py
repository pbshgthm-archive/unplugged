from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify
from sqlalchemy.orm import load_only
from app.models.user_mod import User
from app import db
import app
import json

# @mod_user.route('/search')
def performSearch(searchstring):
    def splitPairs(string) : # auxilliary function to build immutable sets of pairs of consecutive characters
        return {frozenset((string[i],string[i+1])) for i in range(len(string)-1)}

    def distance2(s1,s2): # the custom distance function
        s1 = splitPairs(s1)
        s2 = splitPairs(s2)
        return abs( len(s1.union(s2)) - len(s1.intersection(s2)) ) # the distance metric

    def quicksearch(s1,arr,size = 20,keyfunc = None): # composing mapping and finding distance
        lst = map(lambda x: [x,distance2(keyfunc(s1),keyfunc(x))],arr)
        return [i for i in sorted(lst,key = lambda x: x[1])[:size]]

    def removeDuplicates(arr,keyname,keyvalue ):
        from itertools import combinations
        toremove = []
        for i in combinations(arr,2):
            if keyname(i[0]) == keyname(i[1]):
                toremove.append((lambda x: x[0] if keyvalue(x[0])< keyvalue(x[1]) else x[1])(i))
        for i in toremove:
            arr.remove(i)

    searchArrayUser=User.query.with_entities(User.id,User.name,User.handle)
    searchArrayUser = map(lambda x: list(x),searchArrayUser)
    resultNames = quicksearch(searchstring,searchArrayUser,8,lambda x: x[1]);

    resultHandles = quicksearch(searchstring,searchArrayUser,8,lambda x: x[2]);

    FinalResult = resultNames+resultHandles
    removeDuplicates(FinalResult,lambda x: x[0],lambda x: x[1])

    resultUsers = [i for i in sorted(FinalResult,key = lambda x: x[1])[:8]]

        # searchArrayCircle=circle.query.with_entities(circle.id,circle.name)
        # keyCircle = lambda x: x[1]
        # resultCircles = quicksearch(searchstring,searchArrayCircle,8,keyCircle);
        #
        # searchArrayTopic=topics.query.with_entities(topic.id,topic.name)
        # keyTopic = lambda x: x[1]
        # resultTopics = quicksearch(searchstring,searchArrayTopics,8,keyTopic);

    return resultUsers
