import flet as ft
import random

def main(page: ft.Page):
    page.title = "Simple Typing Test"
    page.window_width = 400
    page.window_height = 500
    
    word_list = [
        "cow", "cat", "dog", "duck", "mouse", 
        "pig", "panda", "cockroach", "crab", "owl", 
        "turtle", "koala", "kangaroo", "alligator", "shrimp"]
    
    random.shuffle(word_list)

    data = {"idx": 0, "correct": 0, "wrong": 0}

    word_text = ft.Text(value=word_list[0], size=40, weight="bold")
    user_input = ft.TextField(label="Type and press Enter", autofocus=True)
    status_msg = ft.Text(size=20)
    progress = ft.Text(value=f"Progress: 0 / {len(word_list)}")
    accuracy = ft.Text()

    def handle_submit(e):
        current_word = word_list[data["idx"]]
        user_text = user_input.value.strip().lower()

        if user_text == current_word:
            data["correct"] += 1
            status_msg.value = "Correct!"
            status_msg.color = "green"
        else:
            data["wrong"] += 1
            status_msg.value = "Incorrect!"
            status_msg.color = "red"

    data["idx"] += 1
        
    if data["idx"] < len(word_list):
            word_text.value = word_list[data["idx"]]
            user_input.value = ""
            progress.value = f"Progress: {data['idx']} / {len(word_list)}"
    else:
            total = len(word_list)
            acc_val = (data["correct"] / total) * 100
            word_text.value = "Done!"
            user_input.disabled = True
            progress.value = f"Final Score: {data['correct']} / {total}"
            accuracy.value = f"Accuracy: {acc_val:.1f}%"
            status_msg.value = "Game Finished!"
