from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class GradeCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.subject_input = TextInput(hint_text="Enter your Subject")
        self.add_widget(self.subject_input)

        self.total_marks_input = TextInput(hint_text="What's the total marks", input_filter='int')
        self.add_widget(self.total_marks_input)

        self.earned_marks_input = TextInput(hint_text="What's the total marks you've earned", input_filter='int')
        self.add_widget(self.earned_marks_input)

        self.calculate_button = Button(text="Calculate")
        self.calculate_button.bind(on_press=self.calculate_grades)
        self.add_widget(self.calculate_button)

        self.result_label = Label(text="")
        self.add_widget(self.result_label)

    def calculate_grades(self, instance):
        subject = self.subject_input.text
        total_marks = int(self.total_marks_input.text)
        earned_marks = int(self.earned_marks_input.text)
        percentage = (earned_marks / total_marks) * 100
        gpa = percentage / 25
        
        grade = "Invalid score"
        if percentage < 60:
            grade = "GRADE F"
        elif 60 <= percentage < 70:
            grade = "GRADE D"
        elif 70 <= percentage < 80:
            grade = "GRADE C"
        elif 80 <= percentage < 90:
            grade = "GRADE B"
        elif 90 <= percentage < 100:
            grade = "GRADE A"

        self.result_label.text = f"The percentage you earned in {subject} is {percentage:.2f}\n" \
                                 f"The GPA you earned in {subject} is {gpa:.2f}\n" \
                                 f"As per your GPA in {subject}, you received {grade}"

class GradeApp(App):
    def build(self):
        return GradeCalculator()

if __name__ == '__main__':
    GradeApp().run()
