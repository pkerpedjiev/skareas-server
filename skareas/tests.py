from __future__ import print_function

import django.test as dt
import skareas.models as skm

# Create your tests here.
class SkiAreaTest(dt.TestCase):
    def test_add_name(self):
        o = skm.SkiArea.objects.create(uid='aa', name='blah')

        res = self.client.get('/skiareas/')
        print("res:", res)

        
