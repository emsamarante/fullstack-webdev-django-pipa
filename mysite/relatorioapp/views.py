from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from relatorioapp.models import Relatorio, Programacao, Carrossel
from relatorioapp.forms import RelatorioForm, ProgramacaoForm, ContactForm, CarrosselForm
from django.views.generic import CreateView,DetailView,ListView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm




########################################################################################################################
#
#                                           Views e Funções associados ao modelo relatorio
#
########################################################################################################################


# Definição da função que fará o upload das imagens
def image_upload_view_relatorio(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form_rel = RelatorioForm(request.POST, request.FILES)
        if form_rel.is_valid():
            form_rel.save()
            # Get the current instance object to display in the template
            img_obj = form_rel.instance
            return render(request, 'relatorioapp/relatorio_list.html', {'form1': form_rel, 'img_obj': img_obj})
    else:
        form_rel = RelatorioForm()
    return render(request, 'relatorioapp/relatorio_list.html', {'form1': form_rel})



# Definindo a função que fará o upload do PDF
def pdf_upload_view_relatorio(request):
    """Process pdfd uploaded by users"""
    if request.method == 'POST':
        form_rel1 = RelatorioForm(request.POST, request.FILES)
        if form_rel1.is_valid():
            form_rel1.save()
            # Get the current instance object to display in the template
            pdf_obj = form_rel1.instance
            return render(request, 'relatorioapp/relatorio_list.html', {'form': form_rel1, 'pdf_obj': pdf_obj})
    else:
        form_rel1 = RelatorioForm()
    return render(request, 'relatorioapp/relatorio_list.html', {'form': form_rel1})


#-------------------    Criando as views usando o CBV    -------------------

class RelatorioCreateView(LoginRequiredMixin, CreateView):
    model = Relatorio
    form_class = RelatorioForm
    template_name = 'relatorioapp/relatorio_form.html'
    success_url = reverse_lazy('relatorio:home')


class RelatorioListView(ListView):
    model = Relatorio
    #permission_required = "app.view_relatorio_list"
    queryset = Relatorio.objects.order_by('data')
    #queryset = Relatorio.objects.all()
    context_object_name = "lista_de_relatorios"

    def get_queryset(self):
        tipo = self.request.GET.get('tipo')
        if tipo:
            return Relatorio.objects.filter(tipo=tipo)
        else:
            return Relatorio.objects.filter(tipo=tipo)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.request.GET.get('tipo')
                
        if tipo == 'Noticia':
            context['tipo_nome']='noticias'         
            
        elif tipo == 'Pesquisa':
            context['tipo_nome']='pesquisa'

        elif tipo == 'Pipacast':
            context['tipo_nome']='pipacast'

        elif tipo == 'Relatorio_de_audiencia':
            context['tipo_nome']='relatorio_de_audiencia'
            #context['preposicao'] =  'dos'
        return context


class RelatorioDetailView(DetailView):
    model = Relatorio


class RelatorioUpdateView(LoginRequiredMixin, UpdateView):
    model = Relatorio
    fields = '__all__'
    success_url = reverse_lazy('relatorio:list_relatorio')


class RelatorioDeleteView(LoginRequiredMixin, DeleteView):
    model = Relatorio
    success_url = reverse_lazy('relatorio:list_relatorio')


class SignUpView(CreateView):
    form_class = UserCreationForm 
    success_url = reverse_lazy('login')
    template_name = 'relatorioapp/signup.html'



#--------------------------    Criando a view usando Função    ------------------
#@login_required 
def home(request):
    relatorios = [
        {'nome_modelo': Relatorio._meta.verbose_name_plural, 'registros': Relatorio.objects.all()},
        {'nome_modelo': Programacao._meta.verbose_name_plural, 'registros': Programacao.objects.all()},
        {'nome_modelo': Carrossel._meta.verbose_name_plural, 'carrosseis':Carrossel.objects.all()},
    ]
    
    return render(request, 'relatorioapp/home.html', {'relatorios':relatorios})


def conceitospage(request):
    return render(request, 'relatorioapp/conceitos-audiencia.html')


def outraview(request):
    relatorios = Carrossel.objects.all()
    return render(request, 'relatorioapp/outraview.html', {'relatorios':relatorios})
########################################################################################################################
#
#                                           Views e Funções associados ao modelo programação
#
########################################################################################################################


# Definição da função que fará o upload das imagens
def image_upload_view_programacao(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form_prg = ProgramacaoForm(request.POST, request.FILES)
        if form_prg.is_valid():
            form_prg.save()
            # Get the current instance object to display in the template
            img_obj = form_prg.instance
            return render(request, 'relatorioapp/programacao_list.html', {'form1': form_prg, 'img_obj': img_obj})
    else:
        form_prg = ProgramacaoForm()
    return render(request, 'relatorioapp/programacao_list.html', {'form1': form_prg})



# Definindo a função que fará o upload do PDF
def pdf_upload_view_programacao(request):
    """Process pdfd uploaded by users"""
    if request.method == 'POST':
        form_prg1 = ProgramacaoForm(request.POST, request.FILES)
        if form_prg1.is_valid():
            form_prg1.save()
            # Get the current instance object to display in the template
            pdf_obj = form_prg1.instance
            return render(request, 'relatorioapp/programacao_list.html', {'form': form_prg1, 'pdf_obj': pdf_obj})
    else:
        form_prg1 = ProgramacaoForm()
    return render(request, 'relatorioapp/programacao_list.html', {'form': form_prg1})


# --------------------    Criando as views usando o CBV   --------------------------------------------------


class ProgramacaoCreateView(LoginRequiredMixin, CreateView):
    model = Programacao
    form_class = ProgramacaoForm
    template_name = 'relatorioapp/programacao_form.html'
    success_url = reverse_lazy('relatorio:home')


class ProgramacaoListView(ListView):
    model = Programacao
    queryset = Programacao.objects.order_by('data')
    #queryset = Relatorio.objects.all()
    context_object_name = "lista_da_programacao"

    def get_queryset(self):
        tipo = self.request.GET.get('tipo')
        if tipo:
            return Programacao.objects.filter(tipo=tipo)
        else:
            #return Programacao.objects.filter(tipo=tipo)
            return Programacao.objects.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipo = self.request.GET.get('tipo')
        subtipo = self.request.GET.get('subtipo')
                    
        if tipo == 'Programacao':
            context['tipo_nome']='programacao'

        elif tipo == 'Pipacast':
            context['tipo_nome']='pipacast'

        if subtipo == 'pdf':
            context['subtipo_nome']='pdf'

        elif subtipo =='blog':
            context['subtipo_nome']='blog'

        return context


class ProgramacaoDetailView(DetailView):
    model = Programacao


class ProgramacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Programacao
    fields = '__all__'
    success_url = reverse_lazy('relatorio:list_programacao')


class ProgramacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Programacao
    success_url = reverse_lazy('relatorio:list_programacao')


########################################################################################################################
#
#                                           View do Forms para contato e receber e-mail
#
##################################################################################################


def contato(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'pipapesquisas@rebahia.com.r', ['pipapesquisas@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("relatorio:home")
      
	form = ContactForm()
	return render(request, "relatorioapp/contato.html", {'form':form})

def sucesso(request):
    return render(request, 'relatorioapp/sucesso.html')





########################################################################################################################
#
#                                           Views e Funções associados ao modelo Carrossel
#
########################################################################################################################

# Definição da função que fará o upload das imagens
def image_upload_view_carrossel_principal(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form_carrossel_pr = CarrosselForm(request.POST, request.FILES)
        if form_carrossel_pr.is_valid():
            form_carrossel_pr.save()
            # Get the current instance object to display in the template
            img_obj = form_carrossel_pr.instance
            return render(request, 'relatorioapp/programacao_list.html', {'form_carrossel_pr': form_carrossel_pr, 'img_obj': img_obj})
    else:
        form_carrossel = CarrosselForm()
    return render(request, 'relatorioapp/home.html', {'form_carrossel': form_carrossel_pr})


def image_upload_view_carrossel_secundaria(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form_carrossel_sc = CarrosselForm(request.POST, request.FILES)
        if form_carrossel_sc.is_valid():
            form_carrossel_sc.save()
            # Get the current instance object to display in the template
            img_obj = form_carrossel_sc.instance
            return render(request, 'relatorioapp/programacao_list.html', {'form_carrossel': form_carrossel_sc, 'img_obj': img_obj})
    else:
        form_carrossel_sc = CarrosselForm()
    return render(request, 'relatorioapp/home.html', {'form_carrossel': form_carrossel_sc})



class CarrosselCreateView(LoginRequiredMixin, CreateView):
    model= Carrossel
    form_class = CarrosselForm
    template_name = 'relatorioapp/carrossel_form.html'
    success_url = reverse_lazy('relatorio:home')



class CarrosselListView(ListView):
    model = Carrossel
    queryset = Carrossel.objects.all()
    context_object_name = "lista_carrossel"


class CarrosselUpdateView(LoginRequiredMixin, UpdateView):
    model = Carrossel
    fields = '__all__'
    success_url = reverse_lazy('relatorio:home')


class CarrosselDeleteView(LoginRequiredMixin, DeleteView):
    model = Carrossel
    success_url = reverse_lazy('relatorio:home')