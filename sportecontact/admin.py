from django.contrib import admin
from .models.athletes import Athlete
from .models.sponsors import Sponsor
from .models.sports import Sport

# Register your models here.

admin.site.register(Athlete)  
admin.site.register(Sponsor)  
admin.site.register(Sport)




