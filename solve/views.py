from django.shortcuts import render,redirect
from .models import Comment,Error
from .forms import ErrorForm
# Create your views here.
def index(request):

    return render (request, 'index.html')

def error(request):
    # current_user = request.user.id
    # user_instance =User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = ErrorForm(request.POST, request.FILES)
        if form.is_valid():
            error = form.save(commit=False)
            # error.profile__user = current_user
            # error.user=user_instance
            error.save()
            return redirect('index')
    else:
        form = ErrorForm()
    return render(request, 'error.html', {"form": form})

def search(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")

        errors = Error.search(search_term)
        message = f"{search_term}"
        print(errors)
        return render(request, 'search.html',{"message":message,"errors": errors})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
