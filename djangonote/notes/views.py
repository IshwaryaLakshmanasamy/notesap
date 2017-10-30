
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from notes import models
from notes import forms


# Create your views here.

def index_view(request):

    note = models.Note.objects.all().order_by('-timestamp')
    return render(request,'notes/index.html',{'notes': note})

def add_note(request):

    id=request.GET.get('id',None)
    if id is not None:
        note=models.Note.objects.get(id=id)
    else:
        note=None

    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.INFO, 'NOTE Added !!')
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            form = forms.NoteForm()
            return HttpResponseRedirect(reverse('notes:add_note'))

    return render(request, 'notes/add_note.html', {'forms': forms})




def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(models.Tag, id=id)
    else:
        tag = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = forms.TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = forms.TagForm(instance=tag)

    return render(request, 'notes/add_tag.html', {'forms': forms, 'tag': tag})