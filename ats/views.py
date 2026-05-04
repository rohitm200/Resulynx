from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ResumeForm
from .models import Resume

# Simple fake "AI scoring"
def calculate_score(filename):
    score = 50
    if "python" in filename.lower():
        score += 20
    if "ai" in filename.lower():
        score += 20
    return min(score, 100)

def home(request):
    return render(request, 'index.html')

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.score = calculate_score(resume.file.name)
            resume.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()

    scores = [r.score for r in resumes]

    return render(request, 'dashboard.html', {
        'form': form,
        'resumes': resumes,
        'scores': scores
    })

