import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Load questionnaire from JSON
def load_questionnaire():
    filepath = "assets/questionnaire.json"
    with open('assets/questionnaire.json', 'r') as f:
        return json.load(f)

# Render questions based on type
def render_question(question):
    question_type = question.get("type")
    if question_type == "slider":
        return st.slider(
            question["question"],
            min_value=question.get("min", 1),
            max_value=question.get("max", 10),
            value=question.get("default", 5)
        )
    elif question_type == "select_slider":
        return st.select_slider(
            question["question"],
            options=question["options"],
            value=question.get("default")
        )
    elif question_type == "radio":
        return st.radio(
            question["question"],
            options=question["options"]
        )
    elif question_type == "select":
        return st.selectbox(
            question["question"],
            options=question["options"]
        )
    elif question_type == "multiselect":
        return st.multiselect(
            question["question"],
            options=question["options"]
        )
    elif question_type == "number":
        return st.number_input(
            question["question"],
            min_value=question.get("min", 0),
            max_value=question.get("max", 24),
            value=question.get("default", 4)
        )
    else:
        st.warning(f"Unsupported question type: {question_type}")
        return None

# Main function
def main():
    st.title("JEE SOCA Analysis System 🚀")
    st.subheader("AI-Powered Skill Assessment for JEE Aspirants")

    # Load questionnaire
    questionnaire = load_questionnaire()

    # Collect responses
    responses = {}
    with st.form("student_form"):
        st.header("Student Questionnaire")
        
        # Render questions from JSON
        for section in questionnaire["questionnaire"]:
            st.subheader(f"📚 {section['section']}")
            for question in section["questions"]:
                response = render_question(question)
                if response is not None:
                    responses[question["question"]] = response
        
        # Submit button
        submitted = st.form_submit_button("Generate SOCA Analysis")
        
        if submitted:
            with st.spinner("Analyzing responses..."):
                # Prepare prompt for Gemini
                prompt = "Analyze this JEE student's profile and create a SOCA analysis:\n\n"
                for question, response in responses.items():
                    prompt += f"- {question}: {response}\n"
                
                prompt += """
                Provide the analysis in this format:
                **Strengths:** [Identify 3 key strengths]
                **Opportunities:** [Suggest 3 improvement areas]
                **Challenges:** [List 3 main challenges]
                **Action Plan:** [Create 4 actionable steps]
                """
                
                # Get Gemini response
                try:
                    response = model.generate_content(prompt)
                    st.subheader("SOCA Analysis Report")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"An error occurred while generating the analysis: {e}")

# Run the app
if __name__ == "__main__":
    main()
