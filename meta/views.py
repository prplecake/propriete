import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .forms import (
    OwnerInfoForm,
    PolicyInfoForm,
)

from .models import (
    OwnerInfo,
    PolicyInfo,
)

from view_classes import (
    BaseAddView,
    BaseUpdateView,
)

logger = logging.getLogger(__name__)


class IndexView(LoginRequiredMixin, TemplateView):
    logger.info('IndexView')
    template_name = 'meta/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['owner_info'] = OwnerInfo.objects.get(pk=1)
        except OwnerInfo.DoesNotExist:
            pass
        try:
            context['policy_info'] = PolicyInfo.objects.get(pk=1)
        except PolicyInfo.DoesNotExist:
            pass
        return context


class OwnerInfoCreate(BaseAddView):
    form_class = OwnerInfoForm
    template_name = 'meta/generic_form.html'
    redirect_target = 'meta:index'


class OwnerInfoUpdate(BaseUpdateView):
    model_class = OwnerInfo
    form_class = OwnerInfoForm
    template_name = 'meta/generic_form.html'
    redirect_target = 'meta:index'

    def get(self, request, *args, **kwargs):
        id = 1
        return super().get(request, id)

    def post(self, request, *args, **kwargs):
        id = 1
        return super().post(request, id)


class PolicyInfoCreate(BaseAddView):
    form_class = PolicyInfoForm
    template_name = 'meta/generic_form.html'
    redirect_target = 'meta:index'


class PolicyInfoUpdate(BaseUpdateView):
    model_class = PolicyInfo
    form_class = PolicyInfoForm
    template_name = 'meta/generic_form.html'
    redirect_target = 'meta:index'

    def get(self, request, *args, **kwargs):
        id = 1
        return super().get(request, id)

    def post(self, request, *args, **kwargs):
        id = 1
        return super().post(request, id)
