class User(Model):
    __tablename__ = 'user'
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
    place = relationship('Place')
    type_id = Column(Integer, ForeignKey('type.id'))
    type = relationship('Type')
    
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
    id = Column(Integer, primary_key=true) 
    time = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship('Acivity')
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
    
    def __repr__(self):
        return self.time
      
class Forum(Model):
    __tablename__ = 'forum'
    id = Column(Integer, primary_key=true)
    category = Column(String(20))
    
        def __repr__(self):
            return self.category
        
class Post(Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=true)
    title = Column(String(50))
    date = Column(Date)
    forum_id = Column(Integer, ForeignKey('forum.id'))
    forum = relationship('Forum')
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
   
    def __repr__(self):
        return self.title
      
class Comment(Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=true)
    title = Column(String(50))
    content = Column(String(200))
    post_id = Column(Integer, ForeignKey('post.id'))
    post= relationship('Post')
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
    
        def __repr__(self):
        return self.title
      
class Booking(Model):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=true)
    time = Column(Date)
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship('Acivity')
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
    
    def __repr__(self):
        return self.time

 class Login(Model):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=true)
    time = Column(Date)
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
      
class FAQ(Model):
    __tablename__ = 'faq'
    id = Column(Integer, primary_key=true)
    title = Column(Sting(50))
    comtent = Column(String(200))
    
     def __repr__(self):
        return self.title 
      
  class Feedback(Model):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=true)
    title = Column(String(50))
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')    
    
     def __repr__(self):
        return self.title
      
   class Review(Model):
     __tablename__ = 'review'
    id = Column(Integer, primary_key=true)
    title = Column(String(50))   
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('user.id'))
    user= relationship('User')
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship('Acivity')
    rating_id = Column(Integer, ForeignKey('rating.id'))
    rating = relationship('Rating')
    
    def __repr__(self):
        return self.title

 class Rating(Model):
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=true)
    grade = Column(String(20))
    
     def __repr__(self):
        return self.title
     
