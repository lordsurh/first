from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from Order.models import *
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.contrib.auth import *
from django.contrib import messages
from django.utils.translation import string_concat
#see https://docs.djangoproject.com/en/dev/topics/auth/
@login_required
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list}, context_instance=RequestContext(request))

@login_required
def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

@login_required
def vote_view(request,poll_id):
    error = "Sorry, but you have already voted."
    p = get_object_or_404(Poll, pk=poll_id)
    result = string_concat(error, ': ', user_logged_in)
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    if Voter.objects.filter(poll_id=poll_id, user_id=request.user.id).exists():
        user = Voter.user
        return render(request, 'polls/index.html', {
        'latest_poll_list':latest_poll_list,
        'error_message':  error
        })
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        v = Voter(user=request.user, poll=p)
        v.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

@login_required
def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

