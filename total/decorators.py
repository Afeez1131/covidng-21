from total.models import Count

def add_get_request(function):
	def get_request(request, *args, **kwargs):
		if request.method == 'GET':
			print(request.method)

			obj, created = Count.objects.get_or_create()
			obj.count +=1 
			obj.save()
		else:
			print(request.method)
	return get_request