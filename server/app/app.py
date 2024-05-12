import os
from flask import Flask, request, Response, g, render_template, jsonify
import marko
import google.generativeai as genai
from flask_cors import CORS
from flask import session
from flask_session import Session
import json

# Generative AI model
from FreelancerModel import FreelancersSkillsModel as FSGM
from ProjectSummizationModel import ProjectSummizationModel as PSGM
from userdataGenerationModel import userDataGeneration as UDGM

# Supabase
from supabase import create_client, Client

url = "https://gubymwuuroyagpdpgdif.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd1Ynltd3V1cm95YWdwZHBnZGlmIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NDI2MTkyNSwiZXhwIjoyMDA5ODM3OTI1fQ.qCGoYbeB8kXYtGdpqi26eVPYDyQUEvPaco6GGYD4Lq0"
supabase = create_client(url, key)

from IPython.display import display
from IPython.display import Markdown

app = Flask(__name__)
app.debug = True

app.config["SECRET_KEY"] = "2ADHW446GHJJPED78@%^$#"  # Replace with a strong secret key
CORS(app)


# Pulls out freelancer data from the frontend
@app.route("/freelancerInfo", methods=["POST"])
def createUser():
    if request.method == "POST":
        response = UDGM.send_message(request.data)
        print(response)

    return {"status": "delivered"}


# Pulls out Client Requirement from the frontend

# Generates a summarized version of the project
PSGM.send_message(
    "Want a website for my business preety my like a ecommerce. I prefer using technology like react, python, django, mysql"
)

response = PSGM.last.text


# Generates the Freelancer Requirement for this project
FSGM.send_message(response)

text = json.loads(FSGM.last.text)
# print(type(text), text)


response = supabase.table("user_data").select("project_id").execute()
# print(response)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
