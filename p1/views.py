from django.shortcuts import render
from p1.models import User
from django.core.paginator import Paginator


# Create your views here.


def User_Data(request):
    all_user = User.objects.all()
    # print(f"\n 1) {all_user}")

    paginator = Paginator(all_user, 4, orphans=2)
    # print(f"\n 2) {paginator}")

    page_number = request.GET.get('page')
    # print(f"\n 3) {page_number}")

    page_obj = paginator.get_page(page_number)
    # print(f"\n 4) {page_obj}")

    # return render(request, "index.html", {'users': all_user})
    return render(request, 'index.html', {'page_obj': page_obj})