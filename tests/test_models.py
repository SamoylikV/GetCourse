from django.test import TestCase
from GetCourse.models import CustomUser
from courses.models import Course, Enrollment, PDFFile
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.teacher = get_user_model().objects.create_user(
            username='teacheruser',
            email='teacher@example.com',
            password='testpass123',
            user_type=1
        )
        # Создаем пользователя-студента
        cls.student = get_user_model().objects.create_user(
            username='studentuser',
            email='student@example.com',
            password='testpass123',
            user_type=2
        )

    def test_user_type(self):
        self.assertEqual(self.teacher.user_type, 1)
        self.assertEqual(self.student.user_type, 2)

    def test_user_str(self):
        self.assertEqual(str(self.teacher), 'teacheruser')
        self.assertEqual(str(self.student), 'studentuser')

class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Course.objects.create(
            title='Introduction to Python',
            description='Learn the basics of Python programming.',
            max_participants=30,
            available=True,
            tag="Курс"
        )

    def test_course_creation(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.title, 'Introduction to Python')
        self.assertEqual(course.description, 'Learn the basics of Python programming.')
        self.assertEqual(course.max_participants, 30)
        self.assertTrue(course.available)


class EnrollmentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username='student', password='testpass123')
        course = Course.objects.create(
            title='Advanced Python',
            description='Deep dive into Python.',
            max_participants=20,
            available=True
        )
        Enrollment.objects.create(student=user, course=course)

    def test_enrollment_creation(self):
        enrollment = Enrollment.objects.get(id=1)
        self.assertEqual(enrollment.student.username, 'student')
        self.assertEqual(enrollment.course.title, 'Advanced Python')

    def test_unique_enrollment(self):
        # Попытка создать дубликат записи должна вызвать ошибку
        user = get_user_model().objects.get(username='student')
        course = Course.objects.get(title='Advanced Python')
        with self.assertRaises(IntegrityError):
            Enrollment.objects.create(student=user, course=course)

class PDFFileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем PDF файл для тестирования
        PDFFile.objects.create(file='course_pdfs/sample.pdf')

    def test_pdf_file_creation(self):
        pdf_file = PDFFile.objects.get(id=1)
        self.assertEqual(pdf_file.file.name, 'course_pdfs/sample.pdf')
