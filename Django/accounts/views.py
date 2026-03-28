from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm()  # Display blank registration form.
    else:
        form = UserCreationForm(data=request.POST)  # Process complete form.

        if form.is_valid():
            new_user = form.save()

            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.xhtml', context)
