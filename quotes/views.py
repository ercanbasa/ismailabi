# Create your views here.
import random
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from quotes.models import Quote

def home(request):
    # random_quote = Quote.objects.order_by('?')
    random_quote = random.choice(Quote.objects.all())
    if not random_quote.exists():
        return HttpResponse('no data available.')
    return HttpResponseRedirect(random_quote.get_absolute_url())

def quote(request, id):
    quote = get_object_or_404(Quote, id=id)
    return render_to_response('quote.html', context_instance=RequestContext(request, {
        'quote' : quote
    }))