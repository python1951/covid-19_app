from django.shortcuts import render
import requests
import json


#print(response.text)
# Create your views here.
def helloworldview(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    headers = {
        'x-rapidapi-key': "f2f2579376msh06e9cd9bfae806bp1d99b3jsnc657b69271fe",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers).json()
    no_of_results = int(response["results"])
    mylist = []
    for i in range(1,no_of_results):
        mylist.append(response['response'][i]['country'])
    string = "EveryOne!!"
    if request.method == "POST":
        mylist = []
        string = "EveryOne!!"
        for i in range(1,no_of_results):
            mylist.append(response['response'][i]['country'])
        selectedcountry = request.POST['selectedcountry']
        for x in range(0,no_of_results):
            if selectedcountry == response['response'][x]['country']:
                new=response["response"][x]['cases']['new']
                recovered=response["response"][x]['cases']['recovered']
                total=response["response"][x]['cases']['total']
                critical=response["response"][x]['cases']['critical']
                active=response["response"][x]['cases']['active']
                deaths=int(total) - int(active) - int(recovered)
                context = {"selectedcountry":selectedcountry,"mylist":mylist,"new":new,"recovered":recovered,"total":total,"critical":critical,"active":active,"deaths":deaths}
                return render (request,'index.html',context)
    mylist = []
    string = "EveryOne!!"
    for i in range(1,no_of_results):
        mylist.append(response['response'][i]['country'])
    context={"string":string,"mylist":mylist}
    return render(request,'index.html',context)
