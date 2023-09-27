from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Exams, Questions


@receiver(post_save, sender=Exams)
def create_exam_questions(sender, instance, created, **kwargs):
    if created:
        Questions.objects.get_or_create(exam=instance)


post_save.connect(create_exam_questions, sender=Exams)
