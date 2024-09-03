from django.db import models

# Create your models here.
class CalculadoraResultado(models.Model):
    consumo_anterior = models.IntegerField()
    consumo_actual = models.IntegerField()
    precio_kwh = models.FloatField()
    nivel_ingresos = models.CharField(max_length=20)
    consumo_total = models.IntegerField()
    costo_total = models.FloatField()
    fecha_calculo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resultado {self.id} - Costo Total: ${self.costo_total:.2f}"

    class Meta:
        ordering = ['-fecha_calculo']

