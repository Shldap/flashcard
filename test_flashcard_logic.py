import unittest
from flashcard_logic import FlashcardLogic

class TestFlashcardLogic(unittest.TestCase):
    def test_extract_questions_from_pdf(self):
        logic = FlashcardLogic()
        questions = logic.extract_questions_from_pdf("sample.pdf")
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0]["question"], "What is the capital of France?")
        self.assertEqual(questions[0]["answer"], "")
        self.assertEqual(questions[1]["question"], "Who painted the Mona Lisa?")
        self.assertEqual(questions[1]["answer"], "")

if __name__ == "__main__":
    unittest.main()
