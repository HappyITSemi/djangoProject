# Create your views here.
from pathlib import Path

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

BASE_DIR = Path(__file__).resolve().parent.parent


def get_button(request):
    if request.method == 'POST':
        if 'button_1' in request.POST:
            # ボタン1がクリックされた場合の処理
            pass


# @login_required
class BatchIndexView(TemplateView):
    template_name = 'batch/index.html'
    success_url = reverse_lazy('todo:todo_index')

    txt = """This is test text
    """

    param = {
        'return_text': txt
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        if object_list is None:
            object_list = self.param
        context = super().get_context_data()
        context['param'] = object_list
        return context

    # get処理
    def get(self, request, *args, **kwargs):
        aaa = self.request.GET.get('button_1')
        return super().get(request, *args, **kwargs)

    # post処理
    def post(self, request, *args, **kwargs):
        self.kwargs["message"] = "Post処理"
        return render(request, self.template_name, context=self.kwargs)


