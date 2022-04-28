from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Todo


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

from django.db.models import F  
# Create your views here.
# random_1738_gen
class TodoLoginView(LoginView):
    template_name = 'todoapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todoapp:index')

class RegisterView(FormView):
    template_name = 'todoapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todoapp:index')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todoapp:index')
        return super(RegisterView, self).get(*args, **kwargs)
    


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todoapp/index.html'
    context_object_name = 'task_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        search_text = self.request.GET.get('search-area') or ''
        if search_text:
            context['task_list'] = context['task_list'].filter(task_title__startswith=search_text)
        context['search_text'] = search_text
        return context

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todoapp/detail.html'
    context_object_name = 'task'

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    template_name = 'todoapp/taskCreate.html'
    fields = ['task_title', 'task_description', 'task_deadline', 'is_completed']
    success_url = reverse_lazy('todoapp:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    template_name = 'todoapp/taskCreate.html'
    fields = ['task_title', 'task_description', 'task_deadline', 'is_completed']
    success_url = reverse_lazy('todoapp:index')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todoapp/taskDelete.html'
    success_url = reverse_lazy('todoapp:index') 

