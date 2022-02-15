# Create your views here.
from pathlib import Path

from django.views.generic import TemplateView

BASE_DIR = Path(__file__).resolve().parent.parent


# @login_required
class BatchIndexView(TemplateView):
    template_name = 'batch/index.html'

