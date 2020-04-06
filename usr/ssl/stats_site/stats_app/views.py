from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
import json

from .models import User, Statistic

# Create your views here.
def users(request, page_index=0, num_per_page=50):
    #top_users_by_id = User.objects.order_by('id')[:50]
    start = num_per_page*page_index
    end = num_per_page*(page_index+1)
    top_users_by_id = User.objects.order_by('id')[start:end]
    #output = ', '.join([u.first_name for u in top_users_by_id])

    #template = loader.get_template('stats/users.html')
    context = {
        'users': top_users_by_id
    }
    return render(request, 'stats/users.html', context)
    #return HttpResponse(template.render(context, request))

def user_stat(request, user_id):
    print("USER_ID=", user_id)
    try:
        user = User.objects.get(pk=user_id)
        #user.stats...
        user_stats = Statistic.objects.filter(user_id=user.pk).order_by('-date')[:20]
        for r in user_stats:
            print(r.id,r.user_id,r.date,r.clicks)
        context = {
            'user': user,
            'user_stats': user_stats
        }
        #return render(request, 'stats/user.html', context)
        out = [{'user_id': r.user_id, 'date': str(r.date), 'clicks': r.clicks} for r in user_stats]
        print(out)
        return HttpResponse(json.dumps(out))
    except User.DoesNotExist:
        raise Http404("User does not exist")

