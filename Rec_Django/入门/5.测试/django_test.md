## 基于shell的测试
```python
python manage.py shell

```

## 基于继承的测试
系统自动在所有以**tests**开头的py文件中寻找测试
```python
from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    # 
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

# 通过 manage.py 运行测试
python manage.py test polls
```
## 测试工具 Client
该工具模拟用户发送网络请求并获取回应，一般用于测试视图函数
```python
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )
```
## 测试命令
```shell
./manage.py test animals/ #指定文件夹
./manage.py test --pattern="tests_*.py" #正则表达式
 test --keepdb # 不销毁测试数据库
 test --noinput # 不使用残留数据库
 test --parallel # 并发测试

 ## 常用断言
 ```python
 self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )
self.assertContains(response, "No polls are available.")
self.assertEqual(response.status_code, 404)
```        