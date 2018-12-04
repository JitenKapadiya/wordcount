
#from django.contrib import admin
from django.urls import path
from.import view

#urlpatterns = [
   # path('admin/', admin.site.urls),
#]

urlpatterns = [
  path('',view.homepage),
  path('contact/', view.contact),
  path('service/', view.service),
  path('wordcal/', view.wordcal),
  path('counts/', view.count, name='count'),
  
]