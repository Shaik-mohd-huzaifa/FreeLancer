import google.generativeai as genai
from config import gemini_api_key

genai.configure(api_key=gemini_api_key)

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
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

system_instruction = "When a user put in the project data summarize it and list the skills needed for it. The only data you should respond with is \n\n- Project Title\n- Project Type\n- Project Description\n- Skills Needed\n- ProjectComplexity\n\nin json but not in code but generate it as normally text.\n\nThere would be two types of user prompts \n\n1. Which can include the skills needed\n2 With no skills mentioned.\n\nFor the once with skills mention all the skills and the type of skills. Ex: [ Frontend Development, HTML, CSS, JS ]\nFor the once without skills just mention Type. Ex: [Frontend Development, Backend Developer]. Without actually mentioning the skills\n\n\n- Things to remember\n- Do not include any examples or anything.\n- Put all the skills in one array. Where if its Version Control for example. Put Version Control. If client mentioned it specifically then include Git\n\nuse single quotes for key and values"

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings,
)

ProjectSummizationModel = model.start_chat(
    history=[
        {"role": "user", "parts": ["What roles do we need to develop this project"]},
        {
            "role": "model",
            "parts": [
                "## Project Roles: Building Your Dream Team\n\nTo effectively develop your project, you'll need a diverse team with specific roles to cover all aspects of development. The exact roles will depend on the nature and complexity of your project, but here's a general guide:\n\n**Core Team:**\n\n* **Project Manager:**  The leader who oversees the entire project, ensuring it stays on track, within budget, and meets deadlines. They manage resources, communicate with stakeholders, and mitigate risks.\n* **Product Owner/Business Analyst:**  Defines the project vision, goals, and requirements. They represent the stakeholders and ensure the final product aligns with their needs. \n* **Technical Lead/Architect:**  Designs the technical architecture of the project, choosing technologies and frameworks, and overseeing the development process.\n* **Developers:**  The coding wizards who build the project according to the specifications and architecture. Depending on the project, you might need front-end, back-end, full-stack, mobile, or embedded developers.\n* **QA Testers:**  Ensure the quality of the product by testing functionality, performance, and usability. They identify and report bugs, and work with developers to resolve them.\n\n**Additional Roles (depending on project needs):**\n\n* **UX/UI Designer:**  Focuses on the user experience and interface, ensuring the product is intuitive, user-friendly, and visually appealing.\n* **Data Scientist/Analyst:** If your project involves data processing or analysis, you'll need someone to collect, clean, and interpret data to derive insights and inform decision-making.\n* **DevOps Engineer:**  Bridges the gap between development and operations, automating deployment processes and ensuring smooth operation of the system.\n* **Content Creator/Copywriter:**  Develops engaging and informative content for the project, including website copy, marketing materials, and documentation.\n* **Marketing Specialist:**  Promotes the project and reaches the target audience through various marketing channels.\n\n**Considerations:**\n\n* **Team Size:**  The size of your team will depend on the project scope and complexity. \n* **Skills and Experience:** Ensure your team members possess the necessary skills and experience to fulfill their roles effectively.\n* **Collaboration and Communication:** Foster a collaborative environment with open communication channels to ensure everyone is aligned and working towards the same goals.\n\n**Remember, building the right team is crucial for project success.  Carefully evaluate your needs and assemble a team with the skills and expertise to bring your vision to life.**"
            ],
        },
        {"role": "user", "parts": ["I want a full stack web application"]},
        {
            "role": "model",
            "parts": [
                '{\n"Project Title": "Full Stack Web Application",\n"Project Type": "Web Application",\n"Project Description": "Developing a full stack web application involves creating both the front-end (user interface) and back-end (server-side logic and database) of the application.",\n"Skills Needed": ["Front-End Development (HTML, CSS, JavaScript, React, Angular, Vue.js)", "Back-End Development (Node.js, Python, Java, Ruby, PHP)", "Database Management (SQL, NoSQL)", "API Development (REST, GraphQL)", "Version Control (Git)", "Cloud Computing (AWS, Azure, GCP)", "Testing (Unit, Integration, End-to-End)"],\n"Project Complexity": "High" \n}'
            ],
        },
        {
            "role": "user",
            "parts": ["I want a static website with shows image and some content"],
        },
        {
            "role": "model",
            "parts": [
                '{\n"Project Title": "Static Website with Images and Content",\n"Project Type": "Website",\n"Project Description": "Creating a static website that displays images and written content.",\n"Skills Needed": [ "Front-End Development" ],\n"Project Complexity": "Low"\n}'
            ],
        },
        {"role": "user", "parts": ["I want a static website to be made with next.js"]},
        {
            "role": "model",
            "parts": [
                "{\n'Project Title': 'Static Website with Next.js',\n'Project Type': 'Website',\n'Project Description': 'Building a static website using the Next.js framework.',\n'Skills Needed': ['Front-End Development', 'Next.js', 'React'],\n'Project Complexity': 'Low-Medium'\n}"
            ],
        },
    ]
)
