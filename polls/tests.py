from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        # 新建一个未来发布的问题
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_one_question(self):
        question = create_question(question_text="Past question.", days=0)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Past question.")


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        # client用于模拟用户和视图层代码的交互
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
