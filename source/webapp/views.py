from django.shortcuts import render


def sum_calc(request):
    if request.method == "GET":
        return render(request, 'create.html')
    elif request.method == 'POST':
        number_1 = request.POST.get('first_number')
        number_2 = request.POST.get('second_number')
        if request.POST.get('add') == 'add':
            result = int(number_1) + int(number_2)
            context = {
                "first_number": number_1,
                "second_number": number_2,
                "sign": "+",
                "equals": "=",
                "result": result
            }
            return render(request, 'create.html', context)
        elif request.POST.get('subtract') == 'subtract':
            result = int(number_1) - int(number_2)
            context = {
                "first_number": number_1,
                "second_number": number_2,
                "sign": "-",
                "equals": "=",
                "result": result
            }
            return render(request, 'create.html', context)
        elif request.POST.get('multiply') == 'multiply':
            result = int(number_1) * int(number_2)
            context = {
                "first_number": number_1,
                "second_number": number_2,
                "sign": "*",
                "equals": "=",
                "result": result
            }
            return render(request, 'create.html', context)
        elif request.POST.get('divide') == 'divide':
            result = int(number_1) // int(number_2)
            context = {
                "first_number": number_1,
                "second_number": number_2,
                "sign": "//",
                "equals": "=",
                "result": result
            }
            return render(request, 'create.html', context)
