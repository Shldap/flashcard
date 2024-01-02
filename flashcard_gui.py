import tkinter as tk
from tkinter import messagebox, filedialog

class FlashcardGUI:
    def __init__(self, logic):
        self.logic = logic

        self.root = tk.Tk()
        self.root.title("Flashcard App")

        self.current_flashcard = self.logic.get_random_flashcard()

        self.question_label = tk.Label(self.root, text=self.current_flashcard["question"])
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_flashcard)
        self.next_button.pack(pady=5)

        self.import_button = tk.Button(self.root, text="Import", command=self.import_flashcards)
        self.import_button.pack(pady=5)

        self.custom_flashcard_button = tk.Button(self.root, text="Custom Flashcard", command=self.add_custom_flashcard)
        self.custom_flashcard_button.pack(pady=5)

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.current_flashcard["answer"]

        if user_answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}")

    def next_flashcard(self):
        self.answer_entry.delete(0, tk.END)
        self.current_flashcard = self.logic.get_random_flashcard()
        self.question_label.config(text=self.current_flashcard["question"])

    def import_flashcards(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            self.logic.load_flashcards(file_path)
            messagebox.showinfo("Success", "Flashcards imported successfully!")

        def add_custom_flashcard(self):
         question = messagebox.askstring("Question", "Enter the question for your custom flashcard:")
         if question:
             answer = messagebox.askstring("Answer", "Enter the answer for your custom flashcard:")
             if answer:
                 self.logic.add_custom_flashcard(question, answer)
                 messagebox.showinfo("Success", "Custom flashcard added successfully!")
             self.next_flashcard()
             
    def start(self):
        self.root.mainloop()
