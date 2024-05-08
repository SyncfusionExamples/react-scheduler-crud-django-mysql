from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from schedulerCrud.serializers import ScheduleEventsSerializer
from schedulerCrud.models import ScheduleEvents

# views.py
@csrf_exempt
def GetData(request):
    
        schedule_events = ScheduleEvents.objects.all()
        schedule_events_serializer=ScheduleEventsSerializer(schedule_events,many=True)
        return JsonResponse(schedule_events_serializer.data,safe=False)

@csrf_exempt
def UpdateData(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if 'added' in data and len(data['added']) > 0:
            schedule_events_data = data['added'][0]  # Get the first event from the 'added' list
            schedule_events_serializer = ScheduleEventsSerializer(data=schedule_events_data)
            if schedule_events_serializer.is_valid():
                schedule_events_serializer.save()
                return GetData(request)            
            else:
                return JsonResponse(schedule_events_serializer.errors, safe=False, status=400)

        elif 'changed' in data and len(data['changed']) > 0:
            for item in data['changed']:
                event = ScheduleEvents.objects.get(pk=item['Id'])
                schedule_events_serializer = ScheduleEventsSerializer(event, data=item)
                if schedule_events_serializer.is_valid():
                    schedule_events_serializer.save()
                    return GetData(request)
                else:
                    return JsonResponse(schedule_events_serializer.errors, safe=False, status=400)
            return JsonResponse("Updated Successfully", safe=False)

        elif 'deleted' in data and len(data['deleted']) > 0:
            for item in data['deleted']:
                event = ScheduleEvents.objects.get(pk=item['Id'])
                event.delete()
            return GetData(request)
        else:
            return JsonResponse({"error": "No events to add, update or delete"}, status=400)
    else:
        return JsonResponse({"error": "Invalid method"}, status=405)
    
