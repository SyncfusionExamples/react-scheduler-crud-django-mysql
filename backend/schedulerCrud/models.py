from django.db import models

# Create your models here.
from django.db import models

class ScheduleEvents(models.Model):
    Id = models.IntegerField(primary_key=True)
    Subject = models.CharField(max_length=200, null=True, blank=True)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    StartTimezone = models.CharField(max_length=200, null=True, blank=True)
    EndTimezone = models.CharField(max_length=200, null=True, blank=True)
    Location = models.CharField(max_length=200, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    IsAllDay = models.BooleanField()
    RecurrenceID = models.IntegerField(null=True, blank=True)
    FollowingID = models.IntegerField(null=True, blank=True)
    RecurrenceRule = models.CharField(max_length=200, null=True, blank=True)
    RecurrenceException = models.CharField(max_length=200, null=True, blank=True)
    IsReadonly = models.BooleanField(null=True, blank=True)
    IsBlock = models.BooleanField(null=True, blank=True)
    RoomID = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schedule_events'