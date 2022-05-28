from tkinter import *
import time
from threading import Thread


def game():
    root = Tk()
    root.title("Disappearing Text")
    root.geometry("800x600")

    count_label = Label(text="0 words", font=("Arial"))
    count_label.grid(row=2, column=1, pady=20)

    def check(event):
        word_list = []

        def count():
            for n in range(1, 6):
                time.sleep(1)
                print(n)
                if n == 5:
                    print("yes")
                    count_label.destroy()
                    header_label.destroy()
                    text_input.destroy()
                    label = Label(text="You spent too much time without writing a word", font=("Arial", 18, "bold"))
                    label.pack(pady=250)

        thread = Thread(target=count)
        if event.char == " ":
            thread.start()
            words = text_input.get(1.0, "end-1c")
            for i in words.split():
                word_list.append(i)
            if len(word_list) > 1 or len(word_list) < 1:
                i = f"{len(word_list)} words"
            else:
                i = f"{len(word_list)} word"
            count_label.config(text=i)
            print(word_list)

    header_label = Label(text="Disappearing Text", font=("Arial", 18, "bold"))
    header_label.grid(row=0, column=0, padx=10, pady=20)

    text_input = Text(root, height=20, width=50)
    text_input.grid(row=1, column=1)
    text_input.bind("<Key>", check)

    root.mainloop()


game()

