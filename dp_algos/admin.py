from django.contrib import admin
from .models import (
    State,
    City,
    ChannelMaster,
    DesignationMaster,
    ProfessionMaster,
    ExecutiveMaster,
    NewMemberEntry,
)

from django.urls import path
from django.shortcuts import redirect
from .views import filter_data_view


# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]
    ordering = ("name",)


admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ["state", "name"]
    list_filter = ["state"]


admin.site.register(City, CityAdmin)


class ChannelMasterAdmin(admin.ModelAdmin):
    list_display = ["channel"]


admin.site.register(ChannelMaster, ChannelMasterAdmin)


class DesignationMasterAdmin(admin.ModelAdmin):
    list_display = ["designation"]


admin.site.register(DesignationMaster, DesignationMasterAdmin)


class ProfessionMasterAdmin(admin.ModelAdmin):
    list_display = ["profession"]


admin.site.register(ProfessionMaster, ProfessionMasterAdmin)


class ExecutiveMasterAdmin(admin.ModelAdmin):
    list_display = ["employee_code", "name"]


admin.site.register(ExecutiveMaster, ExecutiveMasterAdmin)


class NewMemberEntryAdmin(admin.ModelAdmin):
    list_display = [
        "i_card_number",
        "name",
        "designation",
        "paper_meg_channel",
        "valid_upto",
        "executive_name",
        "father_name",
        "phone_no",
        "mobile_no",
        "email",
        "state",
        "city",
        "pin",
        "date_of_birth",
        "qualification",
        "profession",
        "introducer_name",
        "remark",
        "nature",
    ]

    actions = ["custom_action"]

    def custom_action(self, request, queryset):
        # Handle custom action here
        self.message_user(request, "Custom action executed")
        return redirect("/filter-data/")  # Redirect to a custom URL

    custom_action.short_description = "Filter and Report"


admin.site.register(NewMemberEntry, NewMemberEntryAdmin)
