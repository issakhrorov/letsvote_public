from django.contrib import admin
from .models import Category, Element, Promotion, Vote, Voter

admin.site.register(Category)
admin.site.register(Element)
admin.site.register(Promotion)
admin.site.register(Vote)
admin.site.register(Voter)