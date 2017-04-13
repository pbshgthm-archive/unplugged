from sqlalchemy import TypeDecorator
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext import mutable

from sqlalchemy.orm import sessionmaker



Base = declarative_base()




class feed(Base):
    __tablename__ = 'feeds'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    summary = Column(String)
    link = Column(String)
    image = Column(String)
    date = Column(String)
    tag = Column(String)
    topic = Column(String)
    code = Column(String)
    
    def __repr__(self):
        #return "(id='%d', name='%s')" % (self.id, self.name)
        return self.id

engine = create_engine('sqlite:///:main1.db')
 
Base.metadata.create_all(engine)



f1=feed(title="aaa",summary="sum",link="lnk",image='img',date="dt",tag="tg",topic="tpc",code="cde")
f2=feed(title="999",summary="sum",link="lnk",image='img',date="dt",tag="tg",topic="tpc",code="cde")

Session=sessionmaker(bind=engine)
session=Session()

#session.add(f1)
#session.add(f2)

session.commit()


temp=session.query(feed).filter_by(title="999").first()
print(temp.id)


