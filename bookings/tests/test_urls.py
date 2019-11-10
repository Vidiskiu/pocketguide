from django.urls import reverse, resolve

class TestUrls:

    def test_index_url(self):
        path = reverse('bookings:index', kwargs={'user_id': 1})
        assert resolve(path).view_name == 'bookings.index'