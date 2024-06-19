import streamlit as st
import pyautogui as pg

st.set_page_config(
    page_title="Text Repeater",
    page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJDcGneOSP_w0wUrCo8jFb1utKhASkY7-hMQ&s",
    menu_items={
        "About":"""Welcome to the Text Repeater Tool, your go-to solution for repeating any text multiple times effortlessly. This tool is designed to save you time and effort by automating the process of text repetition. Whether you're a developer needing repeated text for testing, a writer looking to generate repetitive patterns, or just having fun, our tool is here to assist you."""
    }
)

st.markdown("# :orange[Instant Text Repeater]")

text=st.text_input(label="Text to repeat",help="Text you want to repeat")

times=st.number_input(label="Repetitions",help="Number of Repetitions",min_value=1)

btn=st.button("Repeat Text")

if btn:
    generated_text=st.text_area(":orange[Place Your Cursor In This Textbox]")
    pg.sleep(2)
    for i in range(0,times):
        pg.write(text+"\n")
