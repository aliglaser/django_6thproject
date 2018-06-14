from django.shortcuts import render, get_object_or_404


from .models import Mineral
# Create your views here.


def mineral_list(request):
	'''Show the page of minerals'''
	minerals = Mineral.objects.all()
	return render(request, 'minerals/mineral_list.html', {'minerals':minerals})


def mineral_detail(request, pk):
	'''Show the detail information of the specific mineral'''
	mineral = get_object_or_404(Mineral, pk=pk)
	return render(request, 'minerals/mineral_detail.html', {'mineral':mineral})
