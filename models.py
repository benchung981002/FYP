from flask_appbuilder import Model
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Float, Text, DateTime
from sqlalchemy.orm import relationship
import datetime


class MyUser(Model):
    __tablename__ = 'myuser'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    birth = Column(Date)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20))
    nation = Column(String(20))

    def __repr__(self):
        return self.username

class Activity(Model):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(200))
    price = Column(Float)
    date = Column(Date)
    place_id = Column(Integer, ForeignKey('place.id'))
    place = relationship("Place")
    type_id = Column(Integer, ForeignKey('type.id'))
    type = relationship("Type")

    def __repr__(self):
        return self.title


class Type(Model):
    __tablename__ = 'type'
    id = Column(Integer, primary_key=True)
    category = Column(String(20))

    def __repr__(self):
        return self.category


class Place(Model):
    __tablename__ = 'place'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

    def __repr__(self):
        return self.name


class Payment(Model):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship('Activity')
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.time


class Forum(Model):
    __tablename__ = 'forum'
    id = Column(Integer, primary_key=True)
    category = Column(String(20))

    def __repr__(self):
        return self.category


class Post(Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    date = Column(Date)
    forum_id = Column(Integer, ForeignKey('forum.id'))
    forum = relationship("Forum")
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.title


class Comment(Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(200))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post")
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.title


class Booking(Model):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity")
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.time


class Login(Model):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")


    def __repr__(self):
        return self.time

class FAQ(Model):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(200))

    def __repr__(self):
        return self.title


class Feedback(Model):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")

    def __repr__(self):
        return self.title


class Review(Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity")
    rating_id = Column(Integer, ForeignKey('rating.id'))
    rating = relationship("Rating")


    def __repr__(self):
        return self.title


class Rating(Model):
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)
    grade = Column(String(20))

    def __repr__(self):
        return self.title
    
class Partyroom(Model):
    __tablename__ = 'partyroom'
    id = Column(Integer, primary_key=True)
    name = Column(String(20)
    price = Column(Float)
    decription = Column(String(200))
    address = Column(String(200))
           
    def __repr__(self):
        return self.name
                  
 class PartyroomBooking(Model):
    __tablename__ = 'partyroombooking'
    id = Column(Integer, primary_key=True)
    time = Column(Date)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    partyroom_id = Column(Integer, ForeignKey('partyroom.id'))
    partyroom = relationship('Partyroom')
                  
     def __repr__(self):
        return self.time
                  
class Blog(Model):
    __tablename__ = 'Blog'
    id = Column(Integer, primary_key=True)  
    title = Column(String(50))
    date = Column(Date)
    content = Column(String(1000))
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    blogtype_id = Column(Integer, ForeignKey('blogtype.id'))
    blogtype = relationship('Blogtype')
                  
    def __repr__(self):
        return self.title
                  
class Blogtype(Model): 
    __tablename__ = 'Blogtype'
    id = Column(Integer, primary_key=True)
    category = Column(String(20))

    def __repr__(self):
        return self.category       
                  
class Ticket(Model):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)                 
    name = Column(String(50))
    quantity= Column(Integer)
    type = Column(String(20))
    price = Column(Float)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity")

    def __repr__(self):
        return self.name
                  
class Shophistory(Model):
    __tablename__ = 'shophistory'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")              
    ticket_id= Column(Integer, ForeignKey('ticket.id'))
    ticket= relationship('Ticket')
                  
    def __repr__(self):
        return self.date
                  
class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    content= Column(String(500))
    date = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity")    
      
    def __repr__(self):
        return self.title
                  
class Contact(Model):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    phone = Column(Integer)
    email = Column(String(50))
                  
    def __repr__(self):
        return self.name
                  
class Company(Model):
    __tablename__ = 'Company'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    email = Column(String(100))
    phone = Column(Integer)
                  
    def __repr__(self):
        return self.name
                  
class Country(Model):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
                  
    def __repr__(self):
        return self.name
                  
class Travel(Model):
    __tablename__ = 'travel'
    id = Column(Integer, primary_key=True)
    detail = Column(String(1000))
    date = Column(Date)     
    country_id= Column(Integer, ForeignKey('country.id'))
    country = relationship('Country')
             
    def __repr__(self):
        return self.date
                  
class Flight(Model):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    checkindate= Column()
    checkoutdate= Column()
    country_id= Column(Integer, ForeignKey('country.id'))
    country = relationship('Country')
    user_id = Column(Integer, ForeignKey('myuser.id'))
    user = relationship("MyUser")
    company_id = Column(Integer, ForeignKey('company_id'))
    company = relationship('Company')
                  
    def __repr__(self):
        return self.quantity
                  
class Webannouncement(Model):
    __tablename__ = 'webannouncement'
    id = Column(Integer, primary_key=True)
    date = Column(Date)   
    title = Column(String(20))
    content= Column(String(500))    
                  
    def __repr__(self):
        return self.title                  
