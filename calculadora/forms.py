from django import forms

class CalculadoraForm(forms.Form):
    consumo_anterior = forms.IntegerField(
        label='Lectura anterior',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    consumo_actual = forms.IntegerField(
        label='Lectura actual',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    precio_kwh = forms.FloatField(
        label='Precio del Kwh',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    nivel_ingresos = forms.ChoiceField(
        label='Nivel de ingresos',
        choices=[
            ('ingresos_altos', 'Nivel 1 - Ingresos Altos'),
            ('ingresos_bajos', 'Nivel 2 - Ingresos Bajos'),
            ('ingresos_medios', 'Nivel 3 - Ingresos Medios')
        ],
        widget=forms.Select(attrs={'class': 'form-select text-center'})
    )
    orden = forms.ChoiceField(
        label='Orden',
        choices=[
            ('asc', 'Ascendente'),
            ('desc', 'Descendente')
        ],
        widget=forms.Select(attrs={'class': 'form-select text-center'})
    )

class CalculadoraMultipleForm(forms.Form):
    consumo_anterior = forms.IntegerField(
        label='Lectura anterior',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    consumo_actual1 = forms.IntegerField(
        label='Lectura actual 1',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    consumo_actual2 = forms.IntegerField(
        label='Lectura actual 2',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'}),
        required=False
    )
    consumo_actual3 = forms.IntegerField(
        label='Lectura actual 3',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'}),
        required=False
    )
    precio_kwh = forms.FloatField(
        label='Precio del Kwh',
        widget=forms.NumberInput(attrs={'class': 'form-control text-center'})
    )
    nivel_ingresos = forms.ChoiceField(
        label='Nivel de ingresos',
        choices=[
            ('ingresos_altos', 'Nivel 1 - Ingresos Altos'),
            ('ingresos_bajos', 'Nivel 2 - Ingresos Bajos'),
            ('ingresos_medios', 'Nivel 3 - Ingresos Medios')
        ],
        widget=forms.Select(attrs={'class': 'form-select text-center'})
    )
    orden = forms.ChoiceField(
        label='Orden',
        choices=[
            ('asc', 'Ascendente'),
            ('desc', 'Descendente')
        ],
        widget=forms.Select(attrs={'class': 'form-select text-center'})
    )
    

