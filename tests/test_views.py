from django.test import TestCase, Client
from django.urls import reverse
from courses.models import Course, Enrollment, PDFFile
from GetCourse.models import CustomUser

class CourseViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(title='Test Course', description='Test Description')

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')

class EnrollmentViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')

    def test_enrollment_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('courses:enroll', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')

    def test_enrollment_view_redirect(self):
        response = self.client.get(reverse('courses:enroll', args=[self.course.id]))
        self.assertRedirects(response, reverse('courses:list'))
        
    def test_enrollment_view_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('courses:enroll', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')
        self.assertTrue(self.user.enrollments.filter(course=self.course).exists())
        
class PDFViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        self.pdf_file = PDFFile.objects.create(file='test.pdf', course=self.course)

    def test_pdf_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('courses:pdf', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')
        self.assertContains(response, 'test.pdf')
        self.assertTrue(self.user.pdf_files.filter(course=self.course).exists())
        
class CourseCreateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        
    def test_course_create_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('courses:create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')
        self.assertTrue(self.user.courses.filter(title='Test Course').exists())
        
class CourseUpdateViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        self.course = Course.objects.create(title='Test Course', description='Test Description')
        
    def test_course_update_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('courses:update', args=[self.course.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Course')
        self.assertTrue(self.user.courses.filter(title='Test Course').exists())