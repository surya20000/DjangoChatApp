from django.shortcuts import render, redirect

# Create your views here.
def chatPage(req, *args, **kwargs):
    if not req.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(req, "chat/chatPage.html", context)
