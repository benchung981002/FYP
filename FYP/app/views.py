from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db

from .models import MyUser, Activity, Type, Place, Payment, Forum, Post, Comment, Booking, Login, FAQ, Feedback, Review, \
    Rating, Blog, Blogtype, Ticket, Shophistory, News, Contact, Company, Country, Travel, \
    Flight, Webannouncement, Partyroom, Partyroombooking


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

class BlogView(ModelView):
    datamodel = SQLAInterface(Blog)


class BlogtypeView(ModelView):
    datamodel = SQLAInterface(Blogtype)


class TicketView(ModelView):
    datamodel = SQLAInterface(Ticket)


class ShophistoryView(ModelView):
    datamodel = SQLAInterface(Shophistory)


class NewsView(ModelView):
    datamodel = SQLAInterface(News)


class ContactView(ModelView):
    datamodel = SQLAInterface(Contact)


class CompanyView(ModelView):
    datamodel = SQLAInterface(Company)


class CountryView(ModelView):
    datamodel = SQLAInterface(Country)


class TravelView(ModelView):
    datamodel = SQLAInterface(Travel)


class FlightView(ModelView):
    datamodel = SQLAInterface(Flight)


class WebannouncementView(ModelView):
    datamodel = SQLAInterface(Webannouncement)


class PartyroomView(ModelView):
    datamodel = SQLAInterface(Partyroom)

class PartyroombookingView(ModelView):
    datamodel = SQLAInterface(Partyroombooking)

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
appbuilder.add_view(RatingView, "Rating", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(BlogView, "Blog", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(BlogtypeView, "Blogtype", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(TicketView, "Ticket", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(ShophistoryView, "Shophistory", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(ContactView, "Contact", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(CompanyView, "Company", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(CountryView, "Country", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(TravelView, "Travel", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(FlightView, "Flight", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(WebannouncementView, "Webannouncement", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(PartyroomView, "Partyroom", icon="fa-folder-open-o", category='Manage', )
appbuilder.add_view(PartyroombookingView, "Partyroombooking", icon="fa-folder-open-o", category='Manage', )