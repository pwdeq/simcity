from django.shortcuts import render,get_object_or_404, redirect
from .models import ticket
from .forms import TicketForm, StatusForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='common:login')
def index(request):

    if request.method == 'POST':
        form = request.POST
        if 'approve' in request.POST:
            form = request.POST['approve']
            status = ticket.objects.get(id=form)
            status.action = "승인"
            status.save()
            return redirect('/trans')

        if 'decline' in request.POST:
            form = request.POST['decline']
            status = ticket.objects.get(id=form)
            status.action = "취소"
            status.save()
            return redirect('/trans')
    else:
        form = StatusForm()
    if request.user.is_staff != True:
        ticket_list = ticket.objects.filter(author=request.user).order_by('-create_date')
    else:
        ticket_list = ticket.objects.order_by('-create_date')
    page = request.GET.get('page', '1')
    paginator = Paginator(ticket_list, 10)
    page_obj = paginator.get_page(page)
    context = {'ticket_list': page_obj,
               'form': form}

    return render(request, 'trans/ticket_list.html', context)





# def trans_create(request):
#     form = TicketForm()
#     return render(request, 'trans/trans_form.html', {'form': form})

@login_required(login_url='common:login')
def trans_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            trans = form.save(commit=False)
            trans.author = request.user
            # trans.transfered_chip_count = trans.chip_count *100
            trans.chip_count = float(trans.chip_count.replace(',',''))
            trans.create_date = timezone.now()
            trans.action = "대기"
            trans.save()
            return redirect('/trans')
    else:
        form = TicketForm()
    context = {'form': form}
    return render(request, 'trans/trans_form.html', context)

