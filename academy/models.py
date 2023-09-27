from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FinancialLiteracy(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="user_financial_literacy")
    FINANCIAL_LITERACY = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )

    financial_literacy = models.CharField(
        choices=FINANCIAL_LITERACY,
        default='no',
        max_length=10)


class AdviceRequests(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="user_advice_requests")
    ADVICE_REQUESTS = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )
    phone_number = PhoneNumberField(default='+989121111111', null=False, blank=False)
    advice_requests = models.CharField(
        choices=ADVICE_REQUESTS,
        default='YES',
        max_length=10)
    active = models.BooleanField(default=False)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return f'{self.first_name}-{self.last_name}'


class Courses(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    active = models.BooleanField(default=False)
    default_course = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class MyCoursesList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE, blank=True,related_name='my_courses')
    added_date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default=1)


class Exams(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    position = models.IntegerField("position", null=True, blank=False)

    def active_exam(self):
        if Courses.active:
            Exams.active = True

    class Meta:
        unique_together = [

            ("course", "position")
        ]

    def __str__(self):
        str_position = str(self.position)
        return f"{self.course}, for exam {str_position}"


class Questions(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE, related_name="question")
    question = models.TextField(max_length=2500, null=False)
    option_a = models.TextField(max_length=500, default='a')
    option_b = models.TextField(max_length=500, default='b')
    option_c = models.TextField(max_length=500, default='c')
    option_d = models.TextField(max_length=500, default='d')
    position = models.IntegerField("position", default=1, null=False, blank=False)

    class Meta:
        unique_together = [

            ("exam", "position")
        ]
        ordering = ("position",)

    def __str__(self):
        str_position = str(self.position)
        return f"exam {self.exam},question with position {str_position}"


ANSWER = [(1, 1), (2, 2), (3, 3), (4, 4)]


class CorrectAnswer(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="correct_answer")
    answer = models.IntegerField(choices=ANSWER, blank=False)

    class Meta:
        # no duplicated question per exam
        unique_together = [
            'exam', 'question', 'answer'
        ]


class ResponseExam(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="user_response")
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="response")
    answer = models.IntegerField(choices=ANSWER)
    score = models.IntegerField(default=0)

    class Meta:
        # no duplicated question per exam
        unique_together = [
            'user', 'exam', 'question'
        ]


class Video(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_videos')
    video_field = models.TextField('https://heepnow.arvanvod.com/bl4v5dXOWJ/Mz51Xr0EYx'
                                   '/origin_KrCCiqJrEAIpUFHijkD05HkRM3z5zzG9mzwwXgTp.mp4', )
