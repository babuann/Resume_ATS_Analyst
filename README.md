Sure, here's a README file for the prompt you mentioned earlier:

# ATS Analyzer Prompt

This is a prompt for an Applicant Tracking System (ATS) analyst to analyze candidates' resumes against job descriptions and provide feedback for resume improvement.

## Prompt Template

```
As an experienced Applicant Tracking System (ATS) analyst, your role is to analyze candidates' resumes against job descriptions and provide feedback for resume improvement. Given a resume and job description, please provide the following information in a single JSON string:

{
    "Job Description Match": %,
    "Missing Keywords": [],
    "Candidate Summary": "",
    "Experience": ""
}

- "Job Description Match": Provide a percentage match score based on how well the resume aligns with the key requirements and responsibilities listed in the job description.

- "Missing Keywords": List any important keywords or skills from the job description that are missing or not highlighted clearly in the resume.

- "Candidate Summary": Provide a brief summary (2-3 sentences) highlighting the candidate's relevant qualifications, experience, and strengths based on the resume.

- "Experience": List the candidate's relevant work experience, including job titles, companies, and duration (in years/months) based on the information provided in the resume.

Please ensure that your analysis is objective, accurate, and constructive, to help the candidate improve their resume and increase their chances of being selected for the role.

resume: {text}

description: {job_description}
```

## Usage

To use this prompt, replace `{text}` with the candidate's resume text and `{job_description}` with the job description text that the resume should be analyzed against.

The expected output is a JSON string with the following keys:

- `"Job Description Match"`: A percentage value indicating how well the resume matches the job description.
- `"Missing Keywords"`: A list of important keywords or skills from the job description that are missing or not highlighted clearly in the resume.
- `"Candidate Summary"`: A brief summary (2-3 sentences) of the candidate's relevant qualifications, experience, and strengths.
- `"Experience"`: A list of the candidate's relevant work experience, including job titles, companies, and duration.

## Example

Input:
```
resume: {John Doe's resume text}

description: {Software Engineer Job Description}
```

Output:
```json
{
    "Job Description Match": 80,
    "Missing Keywords": ["Python", "AWS"],
    "Candidate Summary": "John Doe is an experienced software engineer with expertise in Java, React, and SQL. He has worked on various web applications and has a strong background in agile development methodologies.",
    "Experience": "Software Engineer at ACME Corp (2019 - Present), Software Developer at XYZ Inc. (2016 - 2019)"
}
```

This output indicates that John Doe's resume has an 80% match with the Software Engineer job description, but is missing keywords like "Python" and "AWS". It also provides a summary of his qualifications and relevant work experience.

Feel free to modify the prompt template or the expected output format as needed for your specific use case.
