from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from schedulerCrud.serializers import ScheduleEventsSerializer
from schedulerCrud.models import ScheduleEvents

def GetData(request):
    
        schedule_events = ScheduleEvents.objects.all()
        schedule_events_serializer=ScheduleEventsSerializer(schedule_events,many=True)
        return JsonResponse(schedule_events_serializer.data,safe=False)

def UpdateData(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if 'added' in data and len(data['added']) > 0:
            for item in data['added']:
                schedule_events_serializer = ScheduleEventsSerializer(data=item)
                if schedule_events_serializer.is_valid():
                    schedule_events_serializer.save()
                else:
                    return JsonResponse(schedule_events_serializer.errors, safe=False, status=400)

        if 'changed' in data and len(data['changed']) > 0:
            for item in data['changed']:
                event = ScheduleEvents.objects.get(pk=item['Id'])
                schedule_events_serializer = ScheduleEventsSerializer(event, data=item)
                if schedule_events_serializer.is_valid():
                    schedule_events_serializer.save()
                else:
                    return JsonResponse(schedule_events_serializer.errors, safe=False, status=400)

        if 'deleted' in data and len(data['deleted']) > 0:
            for item in data['deleted']:
                event = ScheduleEvents.objects.get(pk=item['Id'])
                event.delete()
        
        return GetData(request)

    else:
        return JsonResponse({"error": "Invalid method"}, status=405)