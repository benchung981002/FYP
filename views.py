from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db

from .models import MyUser, Activity, Type, Place, Payment, Forum, Post, Comment, Booking, Login, FAQ, Feedback, Review, Rating



def department_query():
    return db.session.query(Department)


class MyUserView(ModelView):
    datamodel = SQLAInterface(MyUser)

class ActivityView(ModelView):
    datamodel = SQLAInterface(Activity)

class TypeView(ModelView):
    datamodel = SQLAInterface(Type)

class PlaceView(ModelView):
    datamodel = SQLAInterface(Place)

class PaymentView(ModelView):
    datamodel = SQLAInterface(Payment)

class ForumView(ModelView):
    datamodel = SQLAInterface(Forum)

class PostView(ModelView):
    datamodel = SQLAInterface(Post)

class CommentView(ModelView):
    datamodel = SQLAInterface(Comment)

class BookingView(ModelView):
    datamodel = SQLAInterface(Booking)

class LoginView(ModelView):
    datamodel = SQLAInterface(Login)

class FAQView(ModelView):
    datamodel = SQLAInterface(FAQ)

class FeedbackView(ModelView):
    datamodel = SQLAInterface(Feedback)

class ReviewView(ModelView):
    datamodel = SQLAInterface(Review)

class RatingView(ModelView):
    datamodel = SQLAInterface(Rating)

db.create_all()

appbuilder.add_view(MyUserView, "MyUser", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(ActivityView, "Activity", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(TypeView, "Type", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(PlaceView, "Place", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(PaymentView, "Payment", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(ForumView, "Forum", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(PostView, "Post", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(CommentView, "Comment", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(BookingView, "Booking", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(LoginView, "Login", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(FAQView, "FAQ", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(FeedbackView, "Feedback", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(ReviewView, "Review", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(RatingView, "Rating,", icon="fa-folder-open-o", category='Manage', )

