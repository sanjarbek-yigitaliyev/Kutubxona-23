from django.shortcuts import render
from .models import Mualif
from django.db.models import F, ExpressionWrapper, fields
from datetime import date

def mualiflar(request):
    current_year = date.today().year
    mualiflar = Mualif.objects.annotate(
        yosh=ExpressionWrapper(current_year - F('t_yil'), output_field=fields.IntegerField())
    ).filter(yosh__gt=45)  # Yoshni 45 dan katta qilish

    return render(request, 'mualiflar.html', {'mualiflar': mualiflar})