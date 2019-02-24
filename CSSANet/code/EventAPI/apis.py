import secrets
from .forms import *
from .models import *

def get_ticket(user_id, event_id, is_paid=False):
    '''
    Create Ticket for event attendent
    '''
    if user and event:
        ticket = AttendEventForm
        ticket.attendedEventId = event_id
        ticket.attendUserId = user_id
        _token = None
        event = Event.objects.get(pk=event_id)
        if event.isFree:
            while not _token:
                _token = secrets.token_urlsafe(256)
                check_duplicate_token = AttendEvent.objects.filter(token=_token).first()
                if check_duplicate_token:
                    _token = None
                else:
                    new_ticket = AttendEvent(
                        attendedEventId = event_id,
                        attendedUserId = user_id,
                        paid = is_paid,
                        token = _token,
                    )
                    instance = new_ticket.save()
                    return instance
        else:
            new_ticket = AttendEvent(
                attendedEventId = event_id,
                attendedUserId = user_id,
                paid = is_paid,
            )
            instance = new_ticket.save()
            return instance          
    else:
        return False


def TicketsCheckIn(token):
    pass