import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
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

system_instruction = 'Here the user will put in his details may be in object form along with or without resume. So you have to pull out the information from the both the prompt and resume or cv in uploaded and brief the profile and generate a object.\n\n- Try to also mention the technology type Ex: If there is a user with skills for like [Html, css, js, react] so in skills also add Frontend Developer. One more example if a user has skills like [React, Next.js, Node.js, Express.js, MongoDb] so along with Full Stack Developer also add both Frontend and Backend developer which together becomes full stack. I the skills of the user is matching any Popular Stack like "MERN stack" also include that in skills.\n\n- Try to Calculate the Skill level of the developer at Individual Skill type in percentage also considering his previous project and experience. Ex: Frontend : 70%, FullStack: 95%, Backend: 60%. So that if their is any individual project with specific skill type then he can go for that.\n\n- Try to include the revelant experience if individually mentioned or present on the resume \n\n- Remove unwanted information like interests, hobbies, certifications and other.\n\n- Depending of number of skills in what skill type generate the percentage of Skill Level and also the experience and projects done with skills can impact the skill level percentage. Mention individual skill level percentage. Ex: skills = [React, Next.js, Angular, React Native, python, flask] so the skill levels will be Frontend - Advance, Backend - Beginner or intermediate. Full stack - beginner\n\n- Include skills with skills type example [Frontend Development, React, Next.js, Backend, Node.js, Express.js, Full Stack Development] also include popular techstack abbreviations if  all skills of that tech stack are mentioned in skills. \n\n- As if resume video is uploaded  try to also fetch from it.'

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings,
)

userProfileSummarization = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                'Matthew Rodriguez,matthew.rodriguez.dev@email.com,"Full-Stack Development (Python, Django, JavaScript, React), API Development, Database Management",3+ years experience building web applications from scratch, handling both frontend and backend development. Strong understanding of databases and API integration.,$50/hour'
            ],
        },
        {
            "role": "model",
            "parts": [
                '```json\n{\n  "name": "Matthew Rodriguez",\n  "email": "matthew.rodriguez.dev@email.com",\n  "experience": "3+ years",\n  "hourlyRate": "$50/hour",\n  "skills": [\n    "Frontend Development",\n    "JavaScript",\n    "React",\n    "Backend Development",\n    "Python",\n    "Django",\n    "API Development",\n    "Database Management",\n    "Full Stack Development"\n  ],\n  "skillLevels": {\n    "Frontend Development": "70%",\n    "Backend Development": "70%",\n    "Full Stack Development": "80%"\n  }\n}\n```'
            ],
        },
    ]
)
