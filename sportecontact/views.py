from django.shortcuts import render


def frontpage(request):
    context = {
    }
    return render(request, "sportecontact/Secondpage.html", context)