from django.shortcuts import render


def get_location(request):

    loc = request.GET.get('location')
    print('***************')
    print(loc)


    return render(request, 'getlocation/get_location.html')
