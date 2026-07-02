from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import student, teacher, admin, exam, pdf

Builder.load_file('main.kv')

class MainScreen(Screen):
    pass

class StudentScreen(Screen):
    def add_student(self):
        name = self.ids.student_name.text
        student_id = self.ids.student_id.text
        student.add_student(name, student_id)
        self.ids.student_name.text = ''
        self.ids.student_id.text = ''

class TeacherScreen(Screen):
    def add_teacher(self):
        name = self.ids.teacher_name.text
        subject = self.ids.subject.text
        teacher.add_teacher(name, subject)
        self.ids.teacher_name.text = ''
        self.ids.subject.text = ''

class AdminScreen(Screen):
    def add_admin(self):
        admin_name = self.ids.admin_name.text
        admin_id = self.ids.admin_id.text
        admin.add_admin(admin_name, admin_id)
        self.ids.admin_name.text = ''
        self.ids.admin_id.text = ''

class SearchStudentScreen(Screen):
    def search_student(self):
        student_id = self.ids.search_id.text
        result = student.search_student(student_id)
        if result:
            self.ids.result.text = f"Name: {result['name']}, ID: {result['student_id']}"
        else:
            self.ids.result.text = "Student not found"

class SearchTeacherScreen(Screen):
    def search_teacher(self):
        name = self.ids.search_name.text
        result = teacher.search_teacher(name)
        if result:
            self.ids.result_teacher.text = f"Name: {result['name']}, Subject: {result['subject']}"
        else:
            self.ids.result_teacher.text = "Teacher not found"

class SearchAdminScreen(Screen):
    def search_admin(self):
        admin_name = self.ids.search_admin_name.text
        result = admin.search_admin(admin_name)
        if result:
            self.ids.result_admin.text = f"Name: {result['name']}, ID: {result['admin_id']}"
        else:
            self.ids.result_admin.text = "Admin not found"

class GenerateCertificateScreen(Screen):
    def generate_certificate(self):
        student_name = self.ids.certificate_name.text
        pdf.generate_certificate(student_name)
        self.ids.certificate_name.text = ''

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(StudentScreen(name='student'))
sm.add_widget(TeacherScreen(name='teacher'))
sm.add_widget(AdminScreen(name='admin'))
sm.add_widget(SearchStudentScreen(name='search_student'))
sm.add_widget(SearchTeacherScreen(name='search_teacher'))
sm.add_widget(SearchAdminScreen(name='search_admin'))
sm.add_widget(GenerateCertificateScreen(name='certificate'))

class SchoolApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    SchoolApp().run()
