import google.generativeai as genai


genai.configure(api_key="AIzaSyDqk_BXrxQPMMZp0V2YjxaQi8kQfWloPvQ")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}


safetySettings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# FreeLancer Generator Model Configuration and history Chats

# Model Instructions
freelancerGenerationInstruction = 'This is the kind of data you will get from the user : {\n"Project Title": "Static Website with Next.js",\n"Project Type": "Website",\n"Project Description": "Building a static website using the Next.js framework.",\n"Skills Needed": [ "Front-End Development", "Next.js" ],\n"Project Complexity": "Low-Medium"\n}\n\nWhat you got to do is generate more minor skills needed for this project with these fields\n\nIndividual: [Skills needed for as individual freelancer to complete the project]\nTeam: {member1 : skills of each member with their Designation, member2...}\n\nPut this data in this form\n\n{\nIndividual: ...,\nTeam: ....,\nEfficiency: [As a Individual to complete the task, as a team]\nQuality:  [As a Individual delivering quality of the task, as a team]\n\n Only generate the json data in a text form no code'

freelancerGenerationModel = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=freelancerGenerationInstruction,
    safety_settings=safetySettings,
)

FreelancersSkillsModel = freelancerGenerationModel.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                '{"Project Title": "Static Website with Next.js","Project Type": "Website","Project Description": "Building a static website using the Next.js framework.","Skills Needed": [ "Front-End Development", "Next.js" ],"Project Complexity": "Low-Medium"}'
            ],
        },
        {
            "role": "model",
            "parts": [
                '{\n"Individual": ["HTML", "CSS", "Javascript", "React", "Next.js", "Responsive Design", "Version Control (Git)", "Deployment"],\n"Team": {\n"Member 1": {"Designation": "Front-End Developer", "Skills": ["HTML", "CSS", "Javascript", "React", "Next.js", "Responsive Design"]},\n"Member 2": {"Designation": "Designer", "Skills": ["UI/UX Design", "Figma/Adobe XD", "Branding", "Visual Communication"]}\n},\n"Efficiency": ["Moderate", "High"], \n"Quality": ["Good", "Excellent"]\n}'
            ],
        },
    ]
)
