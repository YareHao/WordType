import flet as ft
import random

def main(page: ft.Page):
    page.title = "Simple Typing Test"
    page.window_width = 400
    page.window_height = 500
    
    word_list = [
        "cow", "cat", "dog", "duck", "mouse", 
        "pig", "panda", "cockroach", "crab", "owl", 
        "turtle", "koala", "kangaroo", "alligator", "shrimp"
    ]
    random.shuffle(word_list)
