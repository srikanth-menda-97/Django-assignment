from django.contrib import admin

# Register your models here.
from .models import Candidate, Experience, Education

admin.site.register(Candidate)
admin.site.register(Experience)
admin.site.register(Education)
