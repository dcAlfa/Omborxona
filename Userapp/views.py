from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self,request):
        log = request.POST.get("l")
        par = request.POST.get("p")
        userlar = authenticate(request, username=log, password=par)
        if userlar is None:
            return redirect("home")
        login(userlar)
        return render(request, "home.html")



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")






