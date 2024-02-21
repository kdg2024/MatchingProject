# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserEditForm

class SignUpView(generic.CreateView):
  # form_class = UserCreationForm
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/signup.html'


@login_required
def CustomUserEdit(request):
  # 自分の情報を編集しか認めないためidはいらない
  user = request.user
  if request.method == 'POST':
    form = CustomUserEditForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect("matching:index")
  else:
    form = CustomUserEditForm(instance=user)
    context = {
      "form":form
    }
    return render(request, 'accounts/edit.html', context)
## クラス版も余裕があれば書く
## ドキュメントも添えて

@login_required
def CustomUserDetail(request, id):
  user_object = CustomUser.objects.get(pk=id)
  context = {
    "user_object":user_object
  }
  return render(request, 'accounts/detail.html', context)

# classベースなら以下が一例（動作未確認）
# class CustomUserDetailView(LoginRequiredMixin, DetailView):
#   template_name = 'accounts/detail.html'
#   model = CustomUser
#   context_object_name = "user_object"




