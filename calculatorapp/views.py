from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    num1 = int(request.GET['number1'])
    num2 = int(request.GET['number2'])
    opt = request.GET['opt']

    
    if opt== "+":
        ans = num1 + num2

    elif opt== "-":    
        ans = num1 - num2

    elif opt== "*":    
        ans = num1 * num2

    else:
        ans = num1 / num2
    
    con_dict = {'ans':ans}
    return render(request, 'result.html', context=con_dict)