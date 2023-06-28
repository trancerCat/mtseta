from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Manager(BaseModel):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Project(BaseModel):
    manager = models.ForeignKey(Manager, models.SET_NULL, blank=True, null=True, verbose_name="Menedžeris")
    title = models.CharField(max_length=100, verbose_name="Adrese")
    concrete_column = models.IntegerField(verbose_name="Betona stabi", blank=True, null=True)
    concrete_foundation = models.IntegerField(verbose_name="Betona cokoli", blank=True, null=True)
    concrete_slab = models.IntegerField(verbose_name="Betona pasētas", blank=True, null=True)
    wooden_frame = models.IntegerField(verbose_name="Koka posmi", blank=True, null=True)
    metal_column = models.IntegerField(verbose_name="Metāla stabi", blank=True, null=True)
    forged_window = models.IntegerField(verbose_name="Kaltie posmi", blank=True, null=True)
    panel_3d2d = models.IntegerField(verbose_name="Paneļi 3D/2D", blank=True, null=True)
    mesh_in_roll = models.IntegerField(verbose_name="Siets ruļļos", blank=True, null=True)
    sliding_gate = models.IntegerField(verbose_name="Bīdāmie vārti", blank=True, null=True)
    small_gate = models.IntegerField(verbose_name="Mazie vārti", blank=True, null=True)
    large_gate = models.IntegerField(verbose_name="Lielie vārti", blank=True, null=True)
    automation = models.IntegerField(verbose_name="Aut.", blank=True, null=True)
    description = models.CharField(max_length=250, verbose_name="Objekta apraksts", blank=True, null=True)
    advance_payment_date = models.DateField(verbose_name="Avansa datums")
    delivery_date = models.DateField(verbose_name="Nodošanas datums", blank=True, null=True)
    completed = models.BooleanField(default=False, verbose_name="Pabeigts")
    completion_date = models.DateField(verbose_name="Pabeigšanas datums", blank=True, null=True)
    full_payment = models.BooleanField(default=False, verbose_name="Pilnībā apmaksāts")

    def save(self, *args, **kwargs):
        if not self.delivery_date:
            self.delivery_date = self.advance_payment_date + timedelta(weeks=5)
        super().save(*args, **kwargs)
