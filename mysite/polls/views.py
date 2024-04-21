from django.shortcuts import render
from .models import To_do_list, Done_list

def index(request):
    latest_to_do_list = To_do_list.objects.order_by('-deadline')[:]
    done_list = Done_list.objects.all()
    context = {
        'latest_to_do_list': latest_to_do_list,
        'done_list': done_list,
    }
    return render(request, 'polls/index.html', context)

