from django.shortcuts import render, redirect
from django.views import View
from .models import *

from Userapp.models import Ombor


class BolimView(View):
    def get(self, request):
        return render(request, "bulimlar.html")

class ClientView(View):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        c = Client.objects.filter(ombor=o)
        return render(request, "clients.html", {"clientlar":c})


    def post(self, request):

        o = Ombor.objects.get(user=request.user)

        Client.objects.create(
            ism = request.POST.get("i"),
            tel = request.POST.get("t"),
            dokon = request.POST.get("d"),
            manzil = request.POST.get("m"),
            qarz = request.POST.get("q"),
            ombor = o
        )
        return  redirect("client")

class ProView(View):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        m = Maxsulot.objects.filter(ombor=o)
        return render(request, "products.html",{"mahsulot": m})

    def post(self,request):
        o = Ombor.objects.get(user=request.user)

        Maxsulot.objects.create(
            nom = request.POST.get("n"),
            miqdor = request.POST.get("m"),
            brend = request.POST.get("b"),
            kelgan_narx = request.POST.get("kn"),
            sotuvdagi_narx = request.POST.get("sn"),
            ombor=o,
        )
        return redirect("pro")



class Pro_UpView(View):
    def get(self, request):
        return render(request, "product_update.html")


class Client_UpView(View):
    def get(self, request):
        return render(request, "client_update.html")
