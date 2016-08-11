from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activity' not in request.session:
		request.session['activity'] = []
	return render(request, 'gold/index.html' )

def process(request):
	if request.method == 'POST':
		if request.POST['building'] == 'farm':
			earn = random.randrange(10,21)
			request.session['gold'] += earn
			request.session['activity'].append('You earned ' + str(earn) + ' gold!')
		elif request.POST['building'] == 'cave':
			earn = random.randrange(5,11)
			request.session['gold'] += earn
			request.session['activity'].append('You earned ' + str(earn) + ' gold!')
		elif request.POST['building'] == 'house':
			earn = random.randrange(2,6)
			request.session['gold'] += earn
			request.session['activity'].append('You earned ' + str(earn) + ' gold!')
		elif request.POST['building'] == 'casino':
			if request.session['gold'] < 50:
				print '*' * 50
				print request.session['activity']
				print 'why is activity not appending below?'
				print '*' * 50
				request.session['activity'].append(u'you dont have enough money')
				print request.session['activity']
			else:
				chance = random.randrange(0, 11)
				earn = random.randrange(1,51)
				if chance > 8:
					request.session['gold'] += earn
					request.session['activity'].append('You earned ' + str(earn) + ' gold!')
				else:
					request.session['gold'] -= earn
					request.session['activity'].append('You lost ' + str(earn) + ' gold!')
	return redirect('/')

def reset(request):
	if request.method == 'POST':
		del request.session['activity']
		del request.session['gold']
		return redirect('/')
		