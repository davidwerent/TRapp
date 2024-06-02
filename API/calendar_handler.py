from fastapi import APIRouter, Body
from pydantic import BaseModel

from database.calendar import get_free_slot_func, set_slot_status, get_all_slot_by_date

router = APIRouter()


class EventStatus(BaseModel):
    status: int = None


class EventDate(BaseModel):
    date: str = None


@router.get('/calendar/get_free_slot')
async def check_calendar():
    array = get_free_slot_func()
    events = {
        'events': array
    }
    return events


@router.get('/calendar/get_all_slot')
async def get_all_slot(event: EventDate):
    get_all_slot_by_date(event.date)
    return 'not ready yet'


@router.post('/calendar/event/{event_id}/set_busy')
async def change_slot_busy_router(event_id: int, event: EventStatus):
    set_slot_status(event_id, event.status)

    print(f'For EVENT_ID={event_id} status change to {event.status}')

    return f'all is OK={event_id}'
