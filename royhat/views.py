from django.shortcuts import render, redirect
from royhat.forms import AddAuto, EditAuto
from royhat.models import UzAuto


def first_page(request):
    auto = UzAuto.objects.all()
    uzavto = {
        'auto':auto,
    }
    return render(request, 'first_page.html', uzavto)

def post_jonatish(request):
    return render(request, 'post_jonatish.html')

def addAuto(request):
    if request.method =='POST':
        form = AddAuto(request.POST)
        if form.is_valid():
            data = UzAuto()
            data.nomi = form.cleaned_data['nomi']
            data.rangi = form.cleaned_data['rangi']
            data.narxi = form.cleaned_data['narxi']
            data.save()
            return redirect('first_page')


def edit_auto(request, id):
    auto = UzAuto.objects.get(pk=id)
    if request.method == 'POST':
        form = EditAuto(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('first_page')
        else:
            return redirect('edit_auto')
    else:
        form = EditAuto(instance=auto)
        context = {
            'form': form,
            'auto': auto,
        }
    return render(request, 'EditAuto.html', context)


def delate_auto(request, id):
    auto = UzAuto.objects.get(pk=id)
    auto.delete()
    return redirect('first_page')
