from django.urls import path
from . import views


app_name = "relatorio"

urlpatterns = [

    # URLs associadas ao modelo Relatorio

    path('relatorio/add/', views.RelatorioCreateView.as_view(), name='create_relatorio'),
    path('relatorio/list/', views.RelatorioListView.as_view(), name='list_relatorio'),
    path('relatorio/detail/<int:pk>', views.RelatorioDetailView.as_view(), name='detail_relatorio'),
    #path('relatorio/update/<int:pk>', views.RelatorioUpdateView.as_view(), name='update_relatorio'),
    path('relatorio/delete/<int:pk>', views.RelatorioDeleteView.as_view(), name='delete_relatorio'),
    path('home/', views.home, name='home'),
    path('conceitos-audiencia/', views.conceitospage, name='conceitos_audiencia'),

    # URLs associadas ao modelo Programacao

    path('programacao/add/', views.ProgramacaoCreateView.as_view(), name='create_programacao'),
    path('programacao/list/', views.ProgramacaoListView.as_view(), name='list_programacao'),
    path('programacao/detail/<int:pk>', views.ProgramacaoDetailView.as_view(), name='detail_programacao'),
    #path('programacao/update/<int:pk>', views.ProgramacaoUpdateView.as_view(), name='update_programacao'),
    path('programacao/delete/<int:pk>', views.ProgramacaoDeleteView.as_view(), name='delete_programacao'),

    # URL do login

    path('signup/', views.SignUpView.as_view(), name='signup'),

    # URL da tela de contato
    path('contato/', views.contato, name='contato'),
    path('sucesso/', views.sucesso, name='sucesso'),

    # URL do Carrossel
    path('carrossel/add/', views.CarrosselCreateView.as_view(), name='create_carrossel'),
    path('outraview/', views.outraview, name='outra_view'),
    path('carrossel/list/', views.CarrosselListView.as_view(), name='list_carrossel'),
    path('carrossel/delete/<int:pk>', views.CarrosselDeleteView.as_view(), name='delete_carrossel'),
    path('carrossel/update/<int:pk>', views.CarrosselUpdateView.as_view(), name='update_carrossel'),
]


