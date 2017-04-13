from flask import Blueprint, request, render_template, \
   
                  flash, g, session, redirect, url_for

from app.archive.models import C


mod_users = Blueprint('arc-feeds', __name__)



@mod_users.route('/?????', methods=['GET'])
def archive_feed(fhash):
    exists = Archived_Feeds.query.get(fhash)
    if not exists:
        feed = Feed.query.get(fhash)
        new1 = Article(feed.content,feed.title,feed.image,feed.tstamp,"","",feed.link)
        db.session.add(new1)
        db.session.commit()
        new2 = Archived_Feeds(feed.fhash,new1.id)
        db.session.add(new2)
        db.session.commit()
        return new1
    return Article.query.get(exists.id)

    
#######??????????????##############    
                
