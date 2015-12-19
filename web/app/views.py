import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

class APPException(Exception):
    pass

def _appresp(r, success=True):
    R = {'success': success}
    R['result' if success else 'message'] = r
    r = json.dumps(R)
    return HttpResponse(r, content_type='application/json')

# Create your views here.
def home(req):
    return render_to_response(
        'home.html'
    )

