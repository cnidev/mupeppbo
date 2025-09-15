from django.contrib import admin
from django.contrib import messages

from .models import (
    Mutualist,
    Sms,
)

from . import tasks
from .api_cache import get_api_key

@admin.register(Mutualist)
class MutualistAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number"]
    list_filter = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name", "phone_number"]
    ordering = ("last_name",)


@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    list_display = ["id", "content"]

    actions = ["send_sms"]

    @admin.action(description="Envoyer les sms sélectionnés")
    def send_sms(self, request, queryset):
        
        access_token = get_api_key()

        content_list = "".join([q.content for q in queryset])

        phone_number_list = []
        for q in queryset:
            mutualists_list = q.mutualists.all()
            for m in mutualists_list:
                phone_number_list.append(m.phone_number)

        
        tasks.send_mass_sms_task.delay(phone_number_list, content_list, access_token)
        self.message_user(
            request, "Message(s) envoyés à tous les mutualistes", messages.SUCCESS,
        )
        
