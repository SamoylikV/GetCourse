from django.test import TestCase
from courses.forms import CourseForm, PDFFileForm
from GetCourse.forms import CustomUserCreationForm, CustomAuthenticationForm, TeacherProfileForm, StudentProfileForm

class TestCourseForm(TestCase):
    def test_course_form_valid_data(self):
        form = CourseForm(data={'title': 'New Course', 'description': 'Learn something new', 'max_participants': 10, 'available': True, 'tag': 'python'})
        self.assertTrue(form.is_valid())

    def test_course_form_no_data(self):
        form = CourseForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        
        
class TestPDFFileForm(TestCase):
    def test_pdf_file_form_valid_data(self):
        form = PDFFileForm(data={'file': 'test.pdf'})
        self.assertTrue(form.is_valid())

    def test_pdf_file_form_no_data(self):
        form = PDFFileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
        
        
class TestCustomUserCreationForm(TestCase):
    def test_custom_user_creation_form_valid_data(self):
        form = CustomUserCreationForm(data={'username': 'testuser', 'password1': 'testpass', 'password2': 'testpass'})
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_no_data(self):
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
        
class TestCustomAuthenticationForm(TestCase):
    def test_custom_authentication_form_valid_data(self):
        form = CustomAuthenticationForm(data={'username': 'testuser', 'password': 'testpass'})
        self.assertTrue(form.is_valid())

    def test_custom_authentication_form_no_data(self):
        form = CustomAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        
class TestTeacherProfileForm(TestCase):
    def test_teacher_profile_form_valid_data(self):
        form = TeacherProfileForm(data={'first_name': 'John', 'last_name': 'Doe'})
        self.assertTrue(form.is_valid())

    def test_teacher_profile_form_no_data(self):
        form = TeacherProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
        
class TestStudentProfileForm(TestCase):
    def test_student_profile_form_valid_data(self):
        form = StudentProfileForm(data={'first_name': 'John', 'last_name': 'Doe'})
        self.assertTrue(form.is_valid())

    def test_student_profile_form_no_data(self):
        form = StudentProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)