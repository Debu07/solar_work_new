from django.shortcuts import render,redirect
from .forms import ReplyForm,ThreadForm
from django.views.decorators.http import require_POST
from .models import Thread


def index(request):
    form=ThreadForm()
    threads=Thread.objects.all()

    context={
        'form':form,
        'threads':threads
    }
    return render(request,'forum/index.html',context)


def thread(request,thread_id):
    thread=Thread.objects.get(pk=thread_id)

    form = ReplyForm()

    if request.method=='POST':
        form=ReplyForm(request.POST)
        reply= form.save(commit=False) #to save in database
        reply.thread=thread
        reply.user=request.user
        reply.save()

        return redirect('forum:thread',thread_id=thread.id)

    context={'thread':thread , 'form':form }
    return render(request,'forum/thread.html',context)

@require_POST
def new_thread(request):
    form=ThreadForm(request.POST)
    thread=form.save()
    return redirect('forum:thread',thread_id=thread.id)
