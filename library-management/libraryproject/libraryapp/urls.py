from django.conf.urls import url
from django.urls import path
from .views import *
from .templates import *
from django.conf.urls import url, include


app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='books'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^$', home, name='home'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^book/form$', book_form, name='book_form'),
    url(r'^libraries$', library_list, name='libraries'),
    url(r'^library/form$', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    # path('books/<int:book_id>/', book_details, name='book')
]