import unittest
from app.controllers.quizzes_controller import QuizzesController
from datetime import datetime

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
    
    def test_expose_failure_01(self):
        self.ctrl.clear_data()

        self.ctrl.add_quiz("Quiz Title", "quiz text", "invalid start date", datetime(2023, 3, 18, 12, 30, 0))
        quizzes = self.ctrl.get_quizzes()

        self.assertEqual(len(quizzes), 0, "There should be no quizzes as it should have thrown an exception saying invalid date.")

    def test_expose_failure_02(self):
        with self.assertRaises(Exception):
            self.ctrl.add_quiz(None, None, None, None)

    def test_expose_failure_03(self):
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz Title", "quiz text", datetime(2023, 2, 15, 12, 30, 0), datetime(2023, 12, 15, 12, 30, 0))
        question_id = self.ctrl.add_question(quiz_id, "title", "question text")
        answer_id = self.ctrl.add_answer(question_id, "this is the answer", "Wrong type of Variable exposing the failure SHould have checked whether it is boolean or not")
        self.assertEqual(len(answer_id),0,  "There should be no quizzes.")


if __name__ == '__main__':
    unittest.main()
