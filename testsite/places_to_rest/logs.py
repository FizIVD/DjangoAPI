from django.contrib.admin.models import LogEntry

logs = LogEntry.objects.all() # You can also filter
for l in logs:
    print(l.action_time)