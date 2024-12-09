from django.contrib import admin

from common.models import Country, CustomerFeedback, Media, OurInstagramStory, Region, Settings

# Register your models here.


admin.site.register(Country)
admin.site.register(Media)
admin.site.register(OurInstagramStory)
admin.site.register(Region)
admin.site.register(Settings)


class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "customer_name", "customer_position", "rank"]
    list_filter = ["customer_name", "customer_position"]
    search_fields = ["rank"]

    #Admindan qo'shish funksiyasini olib tashaydi
    def has_add_permission(self, request):
        return False

admin.site.register(CustomerFeedback, CustomerFeedbackAdmin)
