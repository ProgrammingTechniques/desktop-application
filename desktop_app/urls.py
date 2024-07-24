from django.contrib import admin
from django.urls import path
from dp_algos.views import initial_page_view, filter_data_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", initial_page_view, name="initial_page"),
    path("filter-data/", filter_data_view, name="filter_data_view"),
    # path("generate-pdf/", generate_pdf, name="generate_pdf"),
]
