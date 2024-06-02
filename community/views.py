from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Region, Forum, Message
# from .forms import MessageForm

# Create your views here.
@login_required
def community_home(request):
    regions = Region.objects.all()
    forums = Forum.objects.all()

    context = {
        'regions': regions,
        'forums': forums
    }

    return render(request, 'community/index.html', context)


@login_required
def forum(request, forum_id):
    regions = Region.objects.all()
    forum = Forum.objects.get(id=forum_id)
    messages = Message.objects.filter(forum=forum).select_related('media', 'sender')
    # form = MessageForm()

    context = {
        'regions': regions,
        'forum': forum,
        'messages': messages,
        # 'form': form
    }

    return render(request, 'community/forum.html', context)
