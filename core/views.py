from django.shortcuts import get_object_or_404, render
from .models import Service


def home(request):
    return render(request, 'core/index.html')


def service(request):
    services = Service.objects.all()
    return render(request, 'core/service.html', {'services': services})


def about(request):
    return render(request, 'core/about.html')


def service_details(request):
    return render(request, 'core/service_details.html')


def elements(request):
    return render(request, 'core/elements.html')


def blog(request):
    return render(request, 'core/blog.html')


def single_blog(request):
    return render(request, 'core/single_blog.html')


def contact(request):
    return render(request, 'core/contact.html')


def service_detail(request, service_id):
    current_service = get_object_or_404(Service, id=service_id)
    all_services = Service.objects.all()

    return render(request, 'core/service_details.html', {
        'current_service': current_service,
        'all_services': all_services
    })
