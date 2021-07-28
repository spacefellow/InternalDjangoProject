from django.shortcuts import render, get_object_or_404
import requests
from .models import BlockInfo
from django.core.paginator import Paginator
from django.views.generic import DetailView


def index(request):
    url = 'https://bcschain.info/api/blocks'
    res = requests.get(url).json()
    BlockInfo.objects.all().delete()
    for el in res:
        elem = BlockInfo(height=el['height'],
                         hash=el['hash'],
                         timestamp=el['timestamp'],
                         miner=el['miner'],
                         transactionCount=el['transactionCount'],
                         slug=el['height'])
        elem.save()
    blocks = BlockInfo.objects.all()
    paginator = Paginator(blocks, 50)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        'MainApp/index.html',
        {
            'page_obj': page_obj,
            'paginator': paginator,
            'page_number': int(page_number)
        }
    )


# class BlockDetailView(DetailView):
#     model = BlockInfo
#     template_name = 'MainApp/details_view.html'
#     context_object_name = 'blockes'


def detail(request, block_slug):
    block = get_object_or_404(BlockInfo, slug=block_slug)
    return render(request, 'MainApp/details_view.html', {'blockes': block})
