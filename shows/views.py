from django.shortcuts import render

def rate_show(request, show_id):
    # Show rating
    return render(request, 'rate_show.html')
