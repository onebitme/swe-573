from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(DataType)
admin.site.register(FormField)
admin.site.register(CommunityTag)
#admin.site.register(DataField)