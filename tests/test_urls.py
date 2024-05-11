from django.test import SimpleTestCase
from django.urls import reverse, resolve
from courses.views import course_list
from GetCourse.models import CustomUser

class TestUrls(SimpleTestCase):
    def test_course_list_url(self):
        url = reverse('courses:list')
        self.assertEquals(resolve(url).func, course_list)
        
        
    def test_course_detail_url(self):
        url = reverse('courses:detail', args=[1])
        self.assertEquals(resolve(url).func, course_list)
    
    def test_course_enroll_url(self):
        url = reverse('courses:enroll', args=[1])
        self.assertEquals(resolve(url).func, course_list)
        
    def test_course_pdf_url(self):
        url = reverse('courses:pdf', args=[1])
        self.assertEquals(resolve(url).func, course_list)
        
    def test_course_create_url(self):
        url = reverse('courses:create')
        self.assertEquals(resolve(url).func, course_list)
    