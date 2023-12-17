import random
import PyPDF2

class FlashcardLogic:
    def __init__(self):
        self.flashcards = []

    def load_flashcards(self, file_path):
        self.flashcards.extend(self.extract_questions_from_pdf(file_path))

    def add_custom_flashcard(self, question, answer):
        self.flashcards.append({"question": question, "answer": answer})

    def get_random_flashcard(self):
        return random.choice(self.flashcards)

    def extract_questions_from_pdf(self, file_path):
        questions = []

        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            num_pages = pdf_reader.numPages

            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()

                # Extract questions using your own logic
                # Here's a simple example assuming questions start with "Q:"
                # and end with a question mark "?"
                start_index = text.find("Q:")
                end_index = text.find("?", start_index)

                while start_index != -1 and end_index != -1:
                    question = text[start_index + 2:end_index + 1].strip()
                    questions.append({"question": question, "answer": ""})
                    start_index = text.find("Q:", end_index)
                    end_index = text.find("?", start_index)

        return questions
