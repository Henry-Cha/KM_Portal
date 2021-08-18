from django.contrib import admin
from .models import * # 수정 : Post, Anser >> * 변경


admin.site.register(FreePosting)
admin.site.register(FreeAnswer)
                    
                    
# admin ID : root
# admin PW : root