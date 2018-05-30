from django.shortcuts import render
from .models import Comment,error

# Create your views here.
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
            return redirect('welcome')
    else:
        form = ErrorForm()
    return render(request, 'error.html', {"form": form})
