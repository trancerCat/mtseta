from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django_tables2 import SingleTableView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Project
from .tables import ProjectTable, DebtorTable

class ProjectList(LoginRequiredMixin, SingleTableView):
    model = Project
    table_class = ProjectTable
    template_name = 'index.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = ProjectTable(Project.objects.filter(completed=False).order_by('delivery_date'))
        debtor_count = Project.objects.filter(completed=True).filter(full_payment=False).count()
        context['debtor_count'] = debtor_count
        context['table'] = table
        return context

class CheckUpdatesView(APIView):
    def get(self, request, format=None):
        last_update = timezone.now() - timezone.timedelta(seconds=10)
        has_new_data = Project.objects.filter(updated_at__gte=last_update).exists()
        return Response({'has_new_data':has_new_data})

class DebtorList(LoginRequiredMixin, SingleTableView):
    model = Project
    table_class = DebtorTable
    template_name = 'debtors.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = DebtorTable(Project.objects.filter(completed=True).filter(full_payment=False).order_by('delivery_date'))
        debtor_count = Project.objects.filter(completed=True).filter(full_payment=False).count()
        context['debtor_count'] = debtor_count
        context['table'] = table
        return context

