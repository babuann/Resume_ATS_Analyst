import streamlit as st 
import google.generativeai as genai 
import os
import PyPDF2 as pdf 
from dotenv import load_dotenv
load_dotenv()
# os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyDfMAgDSmgo39xLm7U5VYsUJMgHK8ipu0c")

def generate_text_from_gemini(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def image_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=" "
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

input_prompt_template = """

As an experienced Applicant Tracking System (ATS) analyst, your role is to analyze candidates' resumes against job descriptions and provide feedback for resume improvement. Given a resume and job description, please provide the following information in a single JSON string:

{{"Job Description Match":%, "Missing Keywords":[], "Candidate Summary":"", "Experience":""}}

"Job Description Match": Provide a percentage match score based on how well the resume aligns with the key requirements and responsibilities listed in the job description.
"Missing Keywords": List any important keywords or skills from the job description that are missing or not highlighted clearly in the resume.
"Candidate Summary": Provide a brief summary (2-3 sentences) highlighting the candidate's relevant qualifications, experience, and strengths based on the resume.
"Experience": List the candidate's relevant work experience, including job titles, companies, and duration (in years/months) based on the information provided in the resume.
Please ensure that your analysis is objective, accurate, and constructive, to help the candidate improve their resume and increase their chances of being selected for the role.

resume:{text}

description:{job_description}

"""

st.title("ATS Analyzer")
# st.text("Optimize Your Resume with AI-Powered Insights. 😃")
font_family = "Open Sans, sans-serif"

# Define the HTML with CSS styles
tagline_html = f"""
<div style="font-family: '{font_family}'; font-size: 18px; font-weight: bold; text-align: center;">
    Unlock Your Career Potential - Optimize Your Resume with AI-Powered Insights.😃
</div>
"""

# Display the tagline with custom font
st.markdown(tagline_html, unsafe_allow_html=True)
st.markdown('<style>h1{color: gray; text-align: center;}</style>', unsafe_allow_html=True)
jd=st.text_area("Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type=["pdf","docx"],help="Please uploadpdf or Docx format")

submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text=image_text(uploaded_file)
#         response=generate_text_from_gemini(input_prompt_template)
#         st.subheader(response)
if submit:
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = image_text(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = image_text(uploaded_file)
        response_text = generate_text_from_gemini(input_prompt_template.format(text=resume_text, job_description=jd))

        # Extract Job Description Match percentage from the response

        st.subheader("ATS Evaluation Result:")
        st.write(response_text)
