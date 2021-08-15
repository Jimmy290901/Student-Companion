from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def send_reminder_emails():
    tasks = Tasks.objects.filter(rem_d_and_t = timezone.now(), completed = False)
    for task in tasks:
        context = {
            'desc':task.task_desc,
            'first_name': task.person.first_name,
        }
        body = render_to_string('todo/email_template.html', context)
        email = EmailMessage (
            'Reminder: ' + task.task_desc,
            body,
            settings.EMAIL_HOST_USER,
            [task.person.colleg_mail]
        )
        email.fail_silently = False
        email.send()
        print("Email sent" + str(task.id))

