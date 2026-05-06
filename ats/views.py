from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ResumeForm
from .models import Resume
from .utils import extract_text, calculate_score


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)

    if request.method == 'POST':
        file = request.FILES.get('file')

        if file:
            text = extract_text(file)
            score, skills = calculate_score(text)

            resume = Resume.objects.create(
                user=request.user,
                file=file,
                score=score
            )

            resume.skills = ",".join(skills)
            resume.save()

            return redirect('dashboard')

    form = ResumeForm()

    scores = [r.score for r in resumes]

    return render(request, 'dashboard.html', {
        'form': form,
        'resumes': resumes,
        'scores': scores
    })

