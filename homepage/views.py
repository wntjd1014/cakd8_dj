from django.shortcuts import render

# 이걸 클라이언트에게 보여주는거다.
def landing(request):
    return render(
        request,
        'homepage/landing.html'
    )

def about_me(request):
    return render(
        request,
        'homepage/about_me.html'
    )