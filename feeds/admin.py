from django.contrib import admin
from .models import ClassicCafeFeedbackModel
# Register your models here.

admin.site.register(ClassicCafeFeedbackModel)

admin.site.index_title = "Classic Cafe's"
admin.site.site_title = "Darius Classic Cafe's"
