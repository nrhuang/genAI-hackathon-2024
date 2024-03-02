import streamlit as st

from bedrockClient import *

class BrainChipApp:
    """
    The BrainChipApp class.
    """

    # Class variable
    BEDROCK = BedrockClient()
    TONE = 0.5 # tone the AI will answer in
    MAX_TOKENS = 2048 # maximum number of characters to output

    def __init__(self):
        """
        Initialize the BrainChipApp class.
        """
        st.header("BrainChip")
        st.subheader("Learn Something new today!")
        self.form = st.form(key='my_form')
        self.topic = self.form.text_input(label='Topic')
        self.level = self.form.selectbox('Select a Level', ['Beginner', 'Intermediate', 'Advanced'])
        self.time = self.form.text_input(label='Time (hours)')
        self.submit_button = self.form.form_submit_button(label='Submit')

    def run(self):
        """
        Run the BrainChipApp.
        """
        if self.submit_button:
            notes_col, resources_col, slides_col, chatbot_col = st.columns([2, 3, 3, 3])

            with notes_col:
                self.show_notes()

            with resources_col:
                self.show_resources()

            with slides_col:
                self.show_slides()

            with chatbot_col:
                self.show_chatbot()

    def show_notes(self):
        """
        Show the notes for the given topic.
        """
        st.subheader("Notes")
        invoke_notes = f"I want to learn about {self.topic} and I have {self.time} hours. I am looking for {self.level} information. Give me short notes about it."
        notes = self.BEDROCK.invoke(invoke_notes, self.TONE, self.MAX_TOKENS)
        st.write(notes)

    def show_resources(self):
        """
        Show the resources for the given topic.
        """
        st.subheader("Resources")
        invoke_resources = f"Give a list of resources (books, videos, articles, links, etc.) for {self.topic} that are {self.level} and can be completed in {self.time} hours. For each resource, include the links (especially for websites, YouTube) if possible."
        resources = self.BEDROCK.invoke(invoke_resources, self.TONE, self.MAX_TOKENS)
        st.write(resources)

    def show_slides(self):
        """
        Show the slides for the given topic.
        """
        st.subheader("Slides")
        # Implement the logic for showing slides here

    def show_chatbot(self):
        """
        Show the chatbot for the given topic.
        """
        st.subheader("Chatbot")
        # Implement the logic for showing the chatbot here


def main():
    app = BrainChipApp()
    app.run()

if __name__ == "__main__":
    main()
