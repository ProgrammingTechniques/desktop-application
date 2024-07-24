from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NewMemberEntry
from django.db.models import Q
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io


def initial_page_view(request):
    return render(request, "initial_page.html")


def filter_data_view(request):
    queryset = NewMemberEntry.objects.all()

    if request.method == "POST":
        search_data = {
            "date_from": request.POST.get("date_from"),
            "date_to": request.POST.get("date_to"),
            "pin": request.POST.get("pin"),
            "name": request.POST.get("name"),
            "i_card_number": request.POST.get("i_card_number"),
            "paper_meg_channel": request.POST.get("paper_meg_channel"),
            "email": request.POST.get("email"),
            "phone_no": request.POST.get("phone_no"),
            "remark": request.POST.get("remark"),
            "executive": request.POST.get("executive"),
        }

        # Filtering
        if search_data["date_from"]:
            queryset = queryset.filter(date_of_birth__gte=search_data["date_from"])
        if search_data["date_to"]:
            queryset = queryset.filter(date_of_birth__lte=search_data["date_to"])
        if search_data["pin"]:
            queryset = queryset.filter(pin__icontains=search_data["pin"])
        if search_data["name"]:
            queryset = queryset.filter(name__icontains=search_data["name"])
        if search_data["i_card_number"]:
            queryset = queryset.filter(
                i_card_number__icontains=search_data["i_card_number"]
            )
        if search_data["paper_meg_channel"]:
            queryset = queryset.filter(
                paper_meg_channel__icontains=search_data["paper_meg_channel"]
            )
        if search_data["email"]:
            queryset = queryset.filter(email__icontains=search_data["email"])
        if search_data["phone_no"]:
            queryset = queryset.filter(phone_no__icontains=search_data["phone_no"])
        if search_data["remark"]:
            queryset = queryset.filter(remark__icontains=search_data["remark"])
        if search_data["executive"]:
            queryset = queryset.filter(
                executive_name__icontains=search_data["executive"]
            )

        if "generate_pdf" in request.POST:
            selected_ids = request.POST.getlist("selected_ids")
            selected_entries = queryset.filter(id__in=selected_ids)
            selected_fields = request.POST.getlist("fields")

            response = HttpResponse(content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="filtered_data.pdf"'

            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=A4)
            width, height = A4
            y = height - 40
            x = 40

            for obj in selected_entries:
                for field in selected_fields:
                    value = getattr(obj, field, "")
                    p.drawString(x, y, f"{field}: {value}")
                    y -= 20
                    if y < 40:
                        p.showPage()
                        y = height - 40
                y -= 20  # Space between records

            p.save()
            buffer.seek(0)
            response.write(buffer.read())
            buffer.close()
            return response

    return render(
        request,
        "filter_data.html",
        {
            "queryset": queryset,
            "field_names": [f.name for f in NewMemberEntry._meta.get_fields()],
            "filters": request.POST,
        },
    )


# def filter_data_view(request):
#     queryset = NewMemberEntry.objects.all()

#     if request.method == "POST":
#         # Extract filter values from POST data
#         date_from = request.POST.get("date_from")
#         date_to = request.POST.get("date_to")
#         pin = request.POST.get("pin")
#         name = request.POST.get("name")
#         i_card_number = request.POST.get("i_card_number")
#         paper_meg_channel = request.POST.get("paper_meg_channel")
#         email = request.POST.get("email")
#         phone_no = request.POST.get("phone_no")
#         remark = request.POST.get("remark")

#         # Build query filters based on POST data
#         filters = Q()
#         if date_from:
#             filters &= Q(valid_upto__gte=date_from)
#         if date_to:
#             filters &= Q(valid_upto__lte=date_to)
#         if pin:
#             filters &= Q(pin=pin)
#         if name:
#             filters &= Q(name__icontains=name)
#         if i_card_number:
#             filters &= Q(i_card_number__icontains=i_card_number)
#         if paper_meg_channel:
#             filters &= Q(paper_meg_channel__icontains=paper_meg_channel)
#         if email:
#             filters &= Q(email__icontains=email)
#         if phone_no:
#             filters &= Q(phone_no__icontains=phone_no)
#         if remark:
#             filters &= Q(remark__icontains=remark)

#         queryset = queryset.filter(filters)

#         if "fields" in request.POST:
#             selected_fields = request.POST.getlist("fields")
#             response = HttpResponse(content_type="application/pdf")
#             response["Content-Disposition"] = 'attachment; filename="filtered_data.pdf"'

#             p = canvas.Canvas(response, pagesize=A4)
#             width, height = A4
#             y = height - 40
#             x = 40

#             for obj in queryset:
#                 for field in selected_fields:
#                     value = getattr(obj, field, "")
#                     p.drawString(x, y, f"{field}: {value}")
#                     y -= 20
#                 y -= 20  # Space between records
#                 if y < 40:
#                     p.showPage()
#                     y = height - 40

#             p.save()
#             return response

#     field_names = [f.name for f in NewMemberEntry._meta.get_fields()]

#     return render(
#         request,
#         "filter_data.html",
#         {
#             "queryset": queryset,
#             "field_names": field_names,
#         },
#     )


# # views.py (continuation)
# def generate_pdf(request):
#     if request.method == "POST":
#         selected_fields = request.POST.getlist("fields")
#         queryset = (
#             NewMemberEntry.objects.all()
#         )  # You can apply additional filtering here if needed

#         response = HttpResponse(content_type="application/pdf")
#         response["Content-Disposition"] = 'attachment; filename="filtered_data.pdf"'

#         p = canvas.Canvas(response, pagesize=A4)
#         width, height = A4
#         y = height - 40
#         x = 40

#         for obj in queryset:
#             for field in selected_fields:
#                 value = getattr(obj, field, "")
#                 p.drawString(x, y, f"{field}: {value}")
#                 y -= 20
#             y -= 20  # Space between records
#             if y < 40:
#                 p.showPage()
#                 y = height - 40

#         p.save()
#         return response

#     return HttpResponse("No data to generate PDF")
