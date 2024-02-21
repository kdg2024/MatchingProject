from django.shortcuts import render
from accounts.models import CustomUser
from .models import MessageTable, RoomTable
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Count

@login_required
def index(request):
  rooms = RoomTable.objects.filter(
    members=request.user
  )
  context = {
    "rooms": rooms,
  }
  return render(request, 'message/index.html', context)

@login_required
def room(request, room_id):
  room = RoomTable.objects.get(pk=room_id)
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      message = form.save(commit=False)
      message.sender = request.user
      message.room = room
      message.save()
      return redirect('message:room', room_id=room_id)
  else:
    form = MessageForm()
    messages = MessageTable.objects.filter(
      room=room
    ).order_by('at')
    context = {
      "messages": messages,
      "form": form,
      "room": room,
    }
    return render(request, 'message/room.html', context)

@login_required
def direct(request, user_id):
  recipient = CustomUser.objects.get(pk=user_id)
  rooms = RoomTable.objects.annotate(
    num_members=Count('members')
  ).filter(
    members=request.user
  ).filter(
    members=recipient
  ).filter(
    num_members=2
  )
  if rooms.exists():
    return redirect('message:room', room_id=rooms.first().id)
  else:
    room = RoomTable(
      name=f"{request.user.username}, {recipient.username}")
    room.save()
    room.members.add(request.user)
    room.members.add(recipient)
    room.save()
    return redirect('message:room', room_id=room.id)

