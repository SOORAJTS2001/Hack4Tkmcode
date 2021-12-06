from django.http.response import HttpResponse
from firebase import firebase  
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import MyPredictModel
# Create your views here.
def index(request):
    firebase1 =firebase.FirebaseApplication('https://nodemcu-fb649-default-rtdb.firebaseio.com/', None)  
    result = firebase1.get('/','') 
    print(type(result)) 
    data = {"result":result}
    #return HttpResponse(f"<h1>Voltage is {result['voltage']} and Current is {result['current']} with total {power} Watts </h1>")
    return render(request,'kseb_monitor/index.html',data)
def update(request):
    if request.method == 'POST':
        if 'content' in request.POST:
            firebase1 =firebase.FirebaseApplication('https://nodemcu-fb649-default-rtdb.firebaseio.com/', None)  
            result = firebase1.get('/','') 
            id = request.POST['content']
            print(result)
            print(id)
            if id in result:
                if result[id]['Cut'] == "False":
                    firebase1.put(f'/{id}','Cut',"True")
                    return render(request,'kseb_monitor/Success.html',{"Status":"Turn Off"})
                elif result[id]['Cut'] == "True":
                    firebase1.put(f'/{id}','Cut',"False")
                    return render(request,'kseb_monitor/Success.html',{"Status":"Turn On"})
            else:
                return render(request,'kseb_monitor/Failed.html')
            
    else:
        return HttpResponse("Not valid")
def predict(request):
    if request.method == "GET":
        form = MyPredictModel()
    else:
        form = MyPredictModel(request.POST)
        if form.is_valid():
            time = int(form.cleaned_data['Time'])
            ptot = (-.6489*(time**6))+(50.7865*(time**5))-(1614.671*(time**4))+(26642.2752*(time**3))-(240228.9394*(time**2))+(1120988.2977*time)-2113610.2246
            pcom = (-0.00100959*(time**11))+(0.0699646*(time**10))-(2.1341*(time**9))+(37.7226*(time**8))-(428.061*(time**7))+(3263.01*(time**6))-(16979*(time**5))+(60001.8*(time**4))-(140203*(time**3))+(204522*(time**2))-(165624*time)+55411.9
            phome = (-1.26262*(time**10))-(7*11)+(8.7500*(time**10))-(6*10)-(0.00026689*(time**9))+(.00471771*(time**8))-(0.0535*(time**7))+(0.4080*(time**6))-(2.12345*(time**5))+(7.504*(time**4))-(17.5343*(time**3))+(25.57*(time**2))-(20.7135*time)+7.346
            messages.success(request,f'The total load at {time} will be {abs(ptot)} KW')
            messages.success(request,f'The commercial load at {time} will be {abs(pcom)} KW and The house load at {time} will be {abs(phome)} KW')
            return redirect('predict')
    return render(request,'kseb_monitor/predict.html',{"form":form})
def dataplot(request):
    return render(request,'kseb_monitor/dataplot.html')