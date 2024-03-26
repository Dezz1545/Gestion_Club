from django.contrib import admin

# Register your models here.
from .models import Quittance
from .models import Commune
from .models import Category
from .models import Menbre




admin.site.register(Quittance) 
admin.site.register(Commune)
admin.site.register(Category)
admin.site.register(Menbre)