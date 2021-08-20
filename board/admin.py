from django.contrib import admin
from .models import * # 수정 : Post, Anser >> * 변경


admin.site.register(FreePosting)
admin.site.register(FreeAnswer)
admin.site.register(EngPosting)
admin.site.register(EngAnswer)
admin.site.register(SciPosting)
admin.site.register(SciAnswer)         
admin.site.register(MedPosting)
admin.site.register(MedAnswer)              
admin.site.register(ArtPosting)
admin.site.register(ArtAnswer)   
admin.site.register(SocPosting)
admin.site.register(SocAnswer)   
# # admin ID : root
# # admin PW : root