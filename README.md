# JEE SOCA Analysis System 🚀

## Overview
The *JEE SOCA Analysis System* is an AI-powered skill assessment tool for JEE aspirants. It collects responses through an interactive questionnaire and generates a *SOCA (Strengths, Opportunities, Challenges, and Action Plan) Analysis* using Google's Gemini AI.

## Features
- Interactive questionnaire for student assessment
- AI-generated personalized SOCA analysis
- Easy-to-use Streamlit interface
- Seamless integration with Google Gemini API

## Installation

### Prerequisites
Ensure you have *Python 3.8+* installed on your system.

### Steps
1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your *Google Gemini API Key*:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
4. **Run the application:**
   ```sh
   streamlit run app.py
   ```

## File Structure
```
📂 Project Directory
│── app.py                 # Main application script
│── requirements.txt       # List of dependencies
│── .env                   # Environment variables
│── soca-analysis-system/
│   └── assets/
│       └── questionnaire.json  # Questionnaire data
```

## How It Works
1. The user answers a series of questions through the Streamlit UI.
2. The responses are compiled and sent to the *Gemini AI Model*.
3. The AI processes the responses and generates a *SOCA Analysis Report*.
4. The results are displayed in a structured format.

## Use of Gemini AI
Google's *Gemini AI* is utilized for processing student responses and generating insights.

### AI Workflow
- The application collects user responses from the questionnaire.
- A structured prompt is created, providing context and specific instructions for Gemini.
- Gemini AI processes the data and returns a *SOCA Analysis* with:
  - *Strengths:* Key areas where the student excels.
  - *Opportunities:* Suggestions for improvement.
  - *Challenges:* Identified difficulties.
  - *Action Plan:* Steps to enhance performance.
- The response is displayed in the Streamlit UI in a well-structured format.

### Benefits of Using Gemini AI
- *Context-Aware Analysis:* Generates personalized insights based on user input.
- *Scalability:* Can analyze responses for multiple users efficiently.
- *AI-Driven Decision Making:* Helps students identify learning gaps and take actionable steps.
- Deep Natural Language Understanding for analyzing and processing text-based inputs.
- Generative Capabilities to create structured and insightful responses.
- Multi-Turn Conversations that maintain context over long interactions.
- Integration with Google Cloud AI Ecosystem for scalability and efficiency.

##Google Gemini Versions
Google Gemini AI has multiple versions, each improving upon previous iterations:
1. Gemini 1.0: Initial release with strong natural language processing capabilities.
2. Gemini 1.5: Enhanced multi-modal capabilities (text, images, and voice processing).
3. Gemini Ultra: Advanced version optimized for enterprise-level AI applications.

   
## Questionnaire Structure
The questionnaire is stored in `soca-analysis-system/assets/questionnaire.json` and consists of multiple sections, each containing relevant questions.

### Sections and Questions:
1. **Subject Knowledge**
   - Mathematics, Physics, and Chemistry proficiency (1-10 scale)
2. **Study Habits**
   - Daily study hours, time management rating, and primary study method
3. **Problem Solving**
   - Problem-solving approach, speed rating, and most challenging subject
4. **Stress Management**
   - Current stress level, stress management method, and sleep quality rating
5. **Study Resources**
   - Study resources used and satisfaction rating

## Dependencies
- `streamlit` - Web app framework
- `google-generativeai` - Google Gemini API for AI-generated responses
- `python-dotenv` - Load environment variables from `.env`

## Contribution
Feel free to submit *issues* or *pull requests* if you want to contribute!

## License
This project is licensed under the *MIT License*.

##Conclusion

The JEE SOCA Analysis System leverages Google Gemini AI to provide data-driven insights to students, helping them improve their JEE preparation through structured analysis. This AI-powered approach ensures that students receive personalized feedback to optimize their study plans effectively.

