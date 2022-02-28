# pip3 install django-debug-toolbar
# https://django-extra-views.readthedocs.io/en/latest/index.html
import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from rest_framework import generics

from .forms import TodoForm
from .models import Category
from .models import Todo
from .serializers import TodoSerializer
from django_filters import rest_framework as filters

logger = logging.getLogger(__name__)


# @login_required()
class TodoIndexView(ListView):
    model = Todo
    template_name = 'todo/index.html'
    paginate_by = 3

    success_url = reverse_lazy('todo:todo_index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.order_by('pk').all()
        return context

    def get_queryset(self):
        object_list = Todo.objects.order_by('id').all()
        # object_list = Todo.objects.filter(user=self.request.user).order_by('id').all()
        return object_list


class TodoDetailView(DetailView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/detail.html'


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/create.html"
    success_url = reverse_lazy('todo:todo_index')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.user = self.request.user  # Login-userをセットする
        print(self.request.user)
        todo.save()
        messages.success(self.request, 'Todoを新規作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Todoの新規作成に失敗しました。")
        return super().form_invalid(form)


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/update.html"
    success_url = reverse_lazy('todo:todo_index')

    def get_success_url(self):
        return reverse_lazy('todo:todo_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'Todoを更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Todoの更新に失敗しました。")
        return super().form_invalid(form)


class TodoDeleteView(DeleteView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/delete.html"
    success_url = reverse_lazy('todo:todo_index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Todoを削除しました。")
        return super().delete(request, *args, **kwargs)


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.DjangoFilterBackend]

