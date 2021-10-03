from django.shortcuts import render, redirect
from . models import Task
from . forms import UpdateForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'edit.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('todo:listview')
        # return reverse_lazy('todo:detailview',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name ='delete.html'
    success_url = reverse_lazy('todo:listview')

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        priority=request.POST['priority']
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()

    task=Task.objects.all()
    return render(request,'home.html',{'tasks':task})


def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task.objects.get(id=id)
    form=UpdateForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'task':task,'form':form})
