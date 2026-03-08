from django.shortcuts import render


rooms=[
    {"id":1,"name":"Python"},
    {"id":2,"name":"Design"},
    {"id":3,"name":"AI ML"},
]

def home(request):
    return render(request, 'home.html', {"rooms": rooms})
def room(request, pk):
    return render(request, 'room.html', {"room_id":pk})