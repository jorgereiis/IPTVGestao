from django.urls import path
from .views import Login, pagar_mensalidade, cancelar_cliente, TabelaDashboard, Teste

urlpatterns = [
    path('pagar_mensalidade/<int:mensalidade_id>/', pagar_mensalidade, name='pagar_mensalidade'),
    path('cancelar_cliente/<int:cliente_id>', cancelar_cliente, name='cancelar_cliente'),
    path('dashboard/', TabelaDashboard.as_view(), name='dashboard'),
    path('teste/', Teste, name="teste"),
    path('', Login, name='login'),
]