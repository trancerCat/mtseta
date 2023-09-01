import django_tables2 as tables
from datetime import datetime, timedelta
from django.utils.safestring import SafeString
from .models import Project


def project_delivery_status_class(value):
    if isinstance(value, SafeString):
        value = datetime.strptime(str(value), "%d.%m.%Y.").date()
    today = datetime.today().date()
    if value <= today:
        return "table-danger"
    elif value <= today + timedelta(days=7):
        return "table-warning"
    else:
        None

class ProjectTable(tables.Table):
    row_number = tables.TemplateColumn('{{ row_counter|add:"1" }}', verbose_name='#')
    manager = tables.Column(verbose_name="M.")
    title = tables.Column(
        verbose_name="Adrese",
        attrs={
            "th":{
                "width":"250",
                "class":"text-start",
            },
            "td":{
                "class":"text-start"
            }
        }
    )
    concrete_column = tables.Column(
        footer=lambda table: sum(x.concrete_column for x in table.data if x.concrete_column is not None))

    description = tables.Column(
        attrs={
            'th':{
                'width':'500'
            },
            'td':{
                'class':'col-description',
            },
        }
    )

    delivery_date = tables.DateColumn(
        format='d.m.Y.',
        attrs={
            "td": {
                "class": lambda value: project_delivery_status_class(value)
            }
        }
    )

    class Meta:
        model = Project
        default = ""
        attrs = {
            "class": "table table-sm table-striped table-bordered text-center align-middle",
            "id": "mt-darbi"
                }
        template_name = "django_tables2/bootstrap5-responsive.html"
        sequence = ('row_number','manager','title','concrete_column','concrete_foundation','concrete_slab','wooden_frame','metal_column','forged_window','panel_3d2d','mesh_in_roll','sliding_gate','small_gate','large_gate','automation','description','delivery_date')
        exclude = ('id', 'created_at', 'updated_at', 'advance_payment_date', 'completed', 'completion_date', 'full_payment')

class DebtorTable(tables.Table):
    row_number = tables.TemplateColumn('{{ row_counter|add:"1" }}', verbose_name='#')
    class Meta:
        model = Project
        default = ""
        attrs = {
            "class": "table table-sm table-striped table-bordered text-center align-middle",
            "id": "mt-debtors"
                }
        template_name = "django_tables2/bootstrap5-responsive.html"
        exclude = ('id','manager','concrete_column','concrete_foundation','concrete_slab','wooden_frame','metal_column','forged_window', 'panel_3d2d', 'mesh_in_roll','sliding_gate','small_gate','large_gate','automation','description','created_at','updated_at','completed','full_payment')
        sequence = ('row_number','title','advance_payment_date')
