from django.contrib import admin
from .models import Manager, Project

# Register your models here.

@admin.register(Manager, Project)

class ManagerAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display_links = ['title']

    def get_list_display(self, request):
        if request.user.is_superuser:
            return [field.name for field in self.model._meta.fields]
        else:
            return ['manager','title','completed','full_payment','concrete_column','concrete_foundation','concrete_slab','wooden_frame','metal_column','forged_window','panel_3d2d','mesh_in_roll','sliding_gate','small_gate','large_gate','automation','description','advance_payment_date_formatted','delivery_date_formatted','completion_date_formatted']

    def advance_payment_date_formatted(self, obj):
        if obj.advance_payment_date:
            return obj.advance_payment_date.strftime('%d.%m.%Y.')
        else:
            return None

    def delivery_date_formatted(self, obj):
        if obj.delivery_date:
            return obj.delivery_date.strftime('%d.%m.%Y.')
        else:
            return None

    def completion_date_formatted(self, obj):
        if obj.completion_date:
            return obj.completion_date.strftime('%d.%m.%Y.')
        else:
            return None

    advance_payment_date_formatted.short_description = 'Avansa datums'
    delivery_date_formatted.short_description = 'Nodošanas datums'
    completion_date_formatted.short_description = 'Pabeigšanas datums'

    class Media:
        css = {
            'all' : ('admin/mt-seta_admin.css',)
        }
