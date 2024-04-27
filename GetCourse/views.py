from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.user_type == 1:
            return reverse_lazy('teacher_dashboard')
        elif self.request.user.user_type == 2:
            return reverse_lazy('student_dashboard')
        else:
            return super().get_success_url()


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('courses')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def student_dashboard(request):
    if request.user.user_type != 2:
        return redirect('home')
    return render(request, 'student_dashboard.html')


@login_required
def teacher_dashboard(request):
    if request.user.user_type != 1:
        return redirect('home')
    return render(request, 'teacher_dashboard.html')
