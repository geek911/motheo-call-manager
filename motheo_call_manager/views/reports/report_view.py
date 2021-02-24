from django.apps import apps as django_apps

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin


class ReportView(NavbarViewMixin, EdcBaseViewMixin, TemplateView):

    template_name = 'motheo_call_manager/reports/call_log_entry_report.html'
    navbar_name = 'motheo_call_manager'
    navbar_selected_item = 'reports'
    model = 'motheo_call_manager.call'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            calls=self.calls)
        return context

    @property
    def calls(self):
        call_model_cls = django_apps.get_model(self.model)
        return call_model_cls.objects.all()
