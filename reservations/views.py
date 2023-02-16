from django.shortcuts import render
from .models import Reservation


def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})


def reservation_detail(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})


def reservation_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')
        time = request.POST.get('time')
        num_of_guests = request.POST.get('num_of_guests')
        Reservation.objects.create(name=name, email=email, phone_number=phone_number,
        date=date, time=time, num_of_guests=num_of_guests)
        return redirect('reservation_list')
    return render(request, 'reservation_create.html')


def reservation_update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
        reservation.name = request.POST.get('name')
        reservation.email = request.POST.get('email')
        reservation.phone_number = request.POST.get('phone_number')
        reservation.date = request.POST.get('date')
        reservation.time = request.POST.get('time')
        reservation.num_of_guests = request.POST.get('num_of_guests')
        reservation.save()
        return redirect('reservation_list')
    return render(request, 'reservation_update.html', {'reservation': reservation})


def reservation_delete(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    reservation.delete()
    return redirect('reservation_list')
