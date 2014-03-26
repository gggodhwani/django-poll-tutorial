from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context, loader, RequestContext
from polls.models import Poll, Choice

def vote(request, poll_id):
	poll_object = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = poll_object.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html', {
			'poll':	poll_object,
			'error_message': "You didn't select a choice.",
		}, context_instance=RequestContext(request))
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls_results', args=(poll_object.id,)))
