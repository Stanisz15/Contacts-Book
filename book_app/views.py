from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError
from book_app.models import Person, Address, Phone, Email, Groups

# Create your views here.


def new_person(request):
    if request.method == 'GET':
        return render(request, 'new_person.html', {})

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        new = Person.objects.create(first_name=first_name, last_name=last_name, description=description)
        person = new.id
        return HttpResponseRedirect('/show/{}'.format(person))


def modify_person(request, id):
    if request.method == 'GET':
        person = get_object_or_404(Person, pk=id)
        return render(request, 'modify_person.html', {"person": person})

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        Person.objects.filter(pk=id).update(first_name=first_name, last_name=last_name, description=description)
        return HttpResponseRedirect('/show/{}'.format(id))


def del_person(request, id):
    Person.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/')


def show_person(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, "person.html", {"person": person})


def person_list(request):
    persons = Person.objects.all().order_by('last_name')
    if request.GET.get('first_name'):
        persons = persons.filter(first_name__icontains=request.GET['first_name'])

    if request.GET.get('last_name'):
        persons = persons.filter(last_name__icontains=request.GET['last_name'])
    return render(request, 'person_list.html', {'persons': persons, 'filters': request.GET})


def add_address(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'GET':
        return render(request, 'add_address.html', {})

    if request.method == 'POST':
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_num = request.POST.get('house_num')
        apartment_num = request.POST.get('apartment_num')
        Address.objects.create(city=city, street=street, house_num=house_num, apartment_num=apartment_num, person=person)
        return HttpResponseRedirect('/modify/{}'.format(id))


def del_address(request, id_person, id_address):
    Person.objects.filter(pk=id_person)
    Address.objects.filter(pk=id_address).delete()
    return HttpResponseRedirect('/modify/{}'.format(id_person))


def add_phone(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'GET':
        return render(request, 'add_phone.html', {})

    if request.method == 'POST':
        try:
            number = request.POST.get('number')
            type = request.POST.get('type')
            Phone.objects.create(number=number, type=type, person=person)
            return HttpResponseRedirect('/modify/{}'.format(id))
        except IntegrityError:
            return render(request, 'error.html', {'person': person})


def add_email(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'GET':
        return render(request, 'add_email.html', {})

    if request.method == 'POST':
        try:
            mail = request.POST.get('mail')
            type = request.POST.get('type')
            Email.objects.create(mail=mail, type=type, person=person)
            return HttpResponseRedirect('/modify/{}'.format(id))
        except IntegrityError:
            return render(request, 'error.html', {'person': person})


def del_phone(request, id_person, id_phone):
    Person.objects.filter(pk=id_person)
    Phone.objects.filter(pk=id_phone).delete()
    return HttpResponseRedirect('/modify/{}'.format(id_person))


def del_email(request, id_person, id_email):
    Person.objects.filter(pk=id_person)
    Email.objects.filter(pk=id_email).delete()
    return HttpResponseRedirect('/modify/{}'.format(id_person))


def modify_address(request, id_person, id_address):
    if request.method == 'GET':
        address = get_object_or_404(Address, pk=id_address)
        return render(request, 'modify_address.html', {'address': address})

    if request.method == 'POST':
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_num = request.POST.get('house_num')
        apartment_num = request.POST.get('apartment_num')
        Address.objects.filter(pk=id_address).update(city=city, street=street, house_num=house_num,
                                                     apartment_num=apartment_num)
        return HttpResponseRedirect('/modify/{}'.format(id_person))


def modify_phone(request, id_person, id_phone):
    if request.method == 'GET':
        phone = get_object_or_404(Phone, pk=id_phone)
        return render(request, 'modify_phone.html', {'phone': phone})

    if request.method == 'POST':
        number = request.POST.get('number')
        type = request.POST.get('type')
        Phone.objects.filter(pk=id_phone).update(number=number, type=type)
        return HttpResponseRedirect('/modify/{}'.format(id_person))


def modify_email(request, id_person, id_email):
    if request.method == 'GET':
        email = get_object_or_404(Email, pk=id_email)
        return render(request, 'modify_email.html', {'email': email})

    if request.method == 'POST':
        mail = request.POST.get('mail')
        type = request.POST.get('type')
        Email.objects.filter(pk=id_email).update(mail=mail, type=type)
        return HttpResponseRedirect('/modify/{}'.format(id_person))


def groups_list(request):
    groups = Groups.objects.all().order_by('name')
    return render(request, 'groups_list.html', {'groups': groups})


def new_group(request):
    if request.method == 'GET':
        return render(request, 'new_group.html', {})

    if request.method == 'POST':
        name = request.POST.get('name')
        Groups.objects.create(name=name)
        return HttpResponseRedirect('/groups')


def show_group(request, id):
    groups = get_object_or_404(Groups, pk=id)
    return render(request, "group.html", {"groups": groups})


def add_to_group(request, id):
    person = get_object_or_404(Person, pk=id)
    groups = Groups.objects.all()
    if request.method == 'GET':
        return render(request, 'add_to_group.html', {'groups': groups})

    if request.method == 'POST':
        choice = Groups.objects.get(name=request.POST['name'])
        choice.persons.add(person)
        return HttpResponseRedirect('/modify/{}'.format(id))


def del_group(request, id):
    Groups.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/groups')


def mod_group(request, id_group):
    if request.method == 'GET':
        group = get_object_or_404(Groups, pk=id_group)
        return render(request, 'modify_group.html', {"groups": group})

    if request.method == 'POST':
        name = request.POST.get('name')
        Groups.objects.filter(pk=id_group).update(name=name)
        return HttpResponseRedirect('/show_group/{}'.format(id_group))


def back_to_group(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, "back_to_group.html", {"person": person})


def del_from_group(request, id_person, id_group):
    person = get_object_or_404(Person, pk=id_person)
    group = get_object_or_404(Groups, pk=id_group)
    group.persons.remove(person)
    return HttpResponseRedirect('/modify/{}'.format(id_person))
