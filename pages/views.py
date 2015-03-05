from django.views.generic import TemplateView
from django.template import RequestContext


class TemplateViewWithContext(TemplateView):

    context_data = {}

    def get_context_data(self, **kwargs):
        context_data = super(TemplateViewWithContext, self).get_context_data(**kwargs)
        if self.context_data:
            context_data.update(self.context_data)
        return context_data

    def get(self, request, *args, **kwargs):
        return self.render_to_response(RequestContext(request, self.get_context_data(**kwargs)))