from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auction.views import *  # Importing all views
from auction.views import Home  # Explicitly importing the Home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('user_home', Bidder_Home.as_view(), name="user_home"),
    path('trainer_home', Auction_User.as_view(), name="trainer_home"),
    path('login_user', Login_User.as_view(), name="login_user"),
    path('contact', Contact.as_view(), name="contact"),
    path('about', About.as_view(), name="about"),
    path('edit_profile', Edit_Profile.as_view(), name="edit_profile"),
    path('edit_category(&lt;int:pid&gt;)', Edit_Category, name='edit_category'),
    path('product_detail(&lt;int:pid&gt;)', product_detail, name='product_detail'),
    path('edit_subcategory(&lt;int:pid&gt;)', Edit_SubCategory, name='edit_subcategory'),
    path('edit_session_date(&lt;int:pid&gt;)', Edit_Session_date, name='edit_session_date'),
    path('edit_session_time(&lt;int:pid&gt;)', Edit_Session_time, name='edit_session_time'),
    path('delete_category(&lt;int:pid&gt;)', delete_category, name='delete_category'),
    path('delete_subcategory(&lt;int:pid&gt;)', delete_subcategory, name='delete_subcategory'),
    path('delete_session_date(&lt;int:pid&gt;)', delete_session_date, name='delete_session_date'),
    path('delete_session_time(&lt;int:pid&gt;)', delete_session_time, name='delete_session_time'),
    path('load-courses/', load_courses, name='ajax_load_courses'),
    path('load-courses1/', load_courses1, name='ajax_load_courses1'),
    path('product_detail2(&lt;int:pid&gt;)', product_detail2, name='product_detail2'),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)