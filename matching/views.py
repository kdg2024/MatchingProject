from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def index(request):
  if request.user.registration_type == 'mentee':
    objects = CustomUser.objects.filter(registration_type='mentor')
  elif request.user.registration_type == 'mentor':
    objects = CustomUser.objects.filter(registration_type='mentee')
  else:
    return redirect('accounts:edit')
  context = {
    'objects': objects,
  }
  return render(request, 'matching/index.html', context)

