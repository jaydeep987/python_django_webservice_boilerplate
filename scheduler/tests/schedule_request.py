from django.test import TestCase
from scheduler.models import Schedule

class TestScheduleData(TestCase):
  def test_can_send_and_get_response(self):
    data = {
      'schedule_id': '1',
      'client_id': '1',
      'cronpattern': '* * * * 5',
      'frequency': 1,
      'name': 'test',
      'is_active': False,
    }
    response = self.client.post('/scheduler/schedule/', data=data)
    self.assertEqual(Schedule.objects.count(), 1)
    response = self.client.get('/scheduler/schedule/')
    self.assertContains(response, 'schedule_id')
    self.assertContains(response, 'is_active')
