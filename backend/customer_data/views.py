from django.shortcuts import render
from django.http import HttpResponse
import pymongo

# Create your views here.
def home(request):
    return render(request, "home.html")

def customers(request):
    client = pymongo.MongoClient("mongodb+srv://vishnu:YHwvgPjn7XfDLxJL@cluster0.ragko.mongodb.net/mycustomers?retryWrites=true&w=majority")
    db = client["mycustomers"]
    collection = db["customers_data"]
    data = collection.find()
    return render(request, "customers.html", {'datas': data})
    #return render(request, "customers.html")