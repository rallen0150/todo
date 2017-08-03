from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from datetime import datetime

from django.contrib.auth.models import User

from todo_list.models import Todo

class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('todo_view')

    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)

class TodoView(ListView):
    model = Todo

    def get_context_data(self):
        context = super().get_context_data()
        context['login'] = AuthenticationForm
        context['list'] = Todo.objects.all()
        return context

class TodoCreateView(CreateView):
    model = Todo
    fields = ('title', 'description', 'complete', 'date', 'time')
    success_url = reverse_lazy('todo_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class TodoItemDetailView(DetailView):
    model = Todo

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['item'] = Todo.objects.get(id=self.kwargs['pk'])
        return context

class TodoItemUpdateView(UpdateView):
    template_name = 'todo_list/complete_update.html'
    model = Todo
    fields = ('complete', )
    success_url = reverse_lazy('todo_view')
