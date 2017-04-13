

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker


engine=create_engine('sqlite:///:memory',echo=False)
session=sessionmaker()
session.configure(bind=engine)
ses=session()

Base=declarative_base()
class test(Base):
	__tablename__="just"
	id=Column(Integer,primary_key=True)
	text=Column(String(10))

	def __repr__(self):
		return self.text


#print test.__table__

t1=test(text="awe")
ses.add(t1)
print "1"
#ses.commit()
print "2"
print ses.query(test).filter_by(text="awe").first()
print "3"