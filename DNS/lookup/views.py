from django.shortcuts import render

# Create your views here.
import dns.resolver
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'lookup/home.html')


def lookup(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        try:
            answers = dns.resolver.resolve(domain, 'A')
            ips = [rdata.address for rdata in answers]
            context = {'domain': domain, 'ips': ips}
            return render(request, 'lookup/lookup.html', context)
        except dns.resolver.NXDOMAIN:
            error = 'Доменное имя не существует'
            return render(request, 'lookup/home.html', {'error': error})
    return render(request, 'lookup/home.html')