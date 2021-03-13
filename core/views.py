from django.views.generic import TemplateView
from .models import Service, Employee, Feature, Plan


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['featurescolumn1'] = Feature.objects.order_by('?').all()[:3]
        context['featurescolumn2'] = Feature.objects.order_by('?').all()[3:6]
        context['plans'] = Plan.objects.all()

        return context

