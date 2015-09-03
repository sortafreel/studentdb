# coding=utf8

from django.shortcuts import render
from django.http import HttpResponse

def students_list(request):
	students = (
	{'id': 1,
		'first_name': u'Віталій',
		'last_name': u'Подоба',
		'ticket': 235,
		'image': 'https://pbs.twimg.com/profile_images/614442111585357824/EXxEgSVg.jpg'},
	{'id': 2,
		'first_name': u'Корост',
		'last_name': u'Андрій',
		'ticket': 652,
		'image': 'https://pbs.twimg.com/profile_images/504022545582936064/fekCxnPx.jpeg'},
	{'id': 3,
		'first_name': u'Гупало',
		'last_name': u'Василь',
		'ticket': 894,
		'image': 'https://pbs.twimg.com/profile_images/378800000265428737/2053abf1a678b9d9724d21d98e62481f.jpeg'},
	{'id': 4,
		'first_name': 'Лапошка',
		'last_name': 'Микола',
		'ticket': 912,
		'image': 'https://pbs.twimg.com/profile_images/3491338437/bd2a80a1d368223e0b10ddd49a3ef503.jpeg'},
	{'id': 5,
		'first_name': 'Негайло',
		'last_name': 'Антон',
		'ticket': 653,
		'image': 'https://pbs.twimg.com/profile_images/652322198/IMG_5402_tvitt.jpg'},
	)
	return render(request, 'students/students_list.html', {'students': students})
	
def students_add(request):
	return HttpResponse('<h1>Student Add Form</h1>')
def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid)
def students_delete(request, sid):
	return HttpResponse('<h1>Delete Student %s</h1>' % sid)
	
	
def groups_list(request):
	groups = (
	{'id': 1,
		'group_name': u'МП-28',
		'starosta_name': u'Василь Гупало'},
	{'id': 2,
		'group_name': u'ПНК-11',
		'starosta_name': u'Тетяна Дрищло'},
	)
	return render(request, 'students/groups_list.html', {'groups': groups})
	
def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
