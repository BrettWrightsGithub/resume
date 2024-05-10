import streamlit as st
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageOps, ImageDraw
from openai import OpenAI


# Page configuration
st.set_page_config(page_title="Brett Wright's Resume", page_icon=":briefcase:", layout="wide") 


st.markdown("""
<style>
body {
    color: #004d40;
    background-color: #b2dfdb;
}
</style>
""", unsafe_allow_html=True)

# Main Header
st.title("Brett Wright")
col1, col2 = st.columns([1,1.5])
with col1:
    with open("assets/Brett-Wright-Resume-5-2024.pdf", "rb") as file:
        btn = st.download_button(
            label="⬇️ Download Resume as PDF",
            data=file,
            file_name="Brett-Wright-Resume-5-2024.pdf",
            mime="application/octet-stream")
st.subheader("Technical Product Manager | Eagle Mountain, UT | 801-540-7574 | brettwrightsemail@gmail.com")
image_path = "assets/Profile.jpg"

def crop_to_circle(image_path, max_width=300):
    img = Image.open(image_path)
    # Convert image to square
    size = (min(img.size),)*2
    img = ImageOps.fit(img, size, centering=(0.5, 0.5))
        # Resize image if it's larger than max_width
    if img.width > max_width:
        scale = max_width / img.width
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size, Image.Resampling.LANCZOS) 
    # Create mask
    mask = Image.new('L', img.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0) + img.size, fill=255)
    # Apply mask
    img.putalpha(mask)
    return img


# Load and crop the image
image_path = "assets/Profile.jpg"
image = crop_to_circle(image_path)
col1, col2 =st.columns(2)   
with col1: 
    st.image(image,caption="Brett Wright")  # Adjust 'width' as needed


# Professional Summary
st.header("Profile Summary")
st.write("""
I'm a Product Manager focusing on practical generative AI to solve real-world problems. I've successfully developed 
and deployed AI solutions in financial compliance software used by Fortune 100 companies using Azure AI. I am excited 
about the possibilities it opens up for our future projects. My work involves integrating various platforms like 
Salesforce, Pershing, Docupace, and Hexure, improving workflows, and enhancing user experiences. I work closely with 
senior management, clients, and team leaders in my discovery and development of products and solutions for internal 
and external stakeholders. I believe in thorough documentation to ensure transparency and understanding across teams.
""")

# st.header("Work Experience Timeline")
# timeline = {
#     "July 2022 - Present": {
#         "role": "Technical Product Manager at CapitalROCK",
#         "details": [
#             "Architected and managed the development of our generative AI product.",
#             "Migrated AI framework from Langchain to Azure's Prompt Flow for better performance."
#         ]
#     },
#     "March 2020 - July 2022": {
#         "role": "Business Product Manager at Inertial Sense",
#         "details": [
#             "Led a complete internal systems overhaul of inventory management.",
#             "Scoped and built an internal data warehouse."
#         ]
#     },
#     "March 2018 - March 2020": {
#         "role": "Marketing Manager at Navigator Business Solutions",
#         "details": [
#             "Integrated marketing services with our internal CRM.",
#             "Created and distributed training and marketing videos."
#         ]
#     }
# }

# for date, info in timeline.items():
#     with st.expander(f"{date} - {info['role']}"):
#         for detail in info["details"]:
#             st.text(detail)



# Work Experience
st.header("Work Experience")
with st.expander("Technical Product Manager, CapitalROCK - July 2022 to Present"):
    st.write("""
    - Architected and managed the development of our generative AI product used by large institutions in our financial 
    compliance software. Migrated AI framework from Langchain to Azure's Prompt Flow for better performance, 
    evaluation, groundedness, and monitoring.
    - Oversaw the development, configuration, and maintenance of client APIs and SAML SSO applications, improving user 
    workflow and providing a seamless client experience.
    - Designed and implemented multiple large-scale integrations between disparate platforms.
    - Successfully managed complex projects, delivering results on time and in line with project specifications.
    - Collaborated with multiple stakeholders, including Chief Compliance Officers, CTOs, and Lead Development Engineers.
    - Played a key role in advising Statement of Work (SOW) contracts and providing instructions on integrations with 
    legal and compliance teams.
    - Organized and executed projects according to modern scrum Agile methodologies using Azure DevOps.
    """)

with st.expander("Business Product Manager, Inertial Sense - Mar 2020 to July 2022"):
    st.write("""
    - Identified the need for and led a complete internal systems overhaul of inventory management, tracking, and 
    accounting, enhancing visibility into the financial operations and improving the accuracy of inventory levels.
    - Scoped and built an internal data warehouse to consolidate data entry and reporting to one source.
    - Identified and corrected key processes that lead to errors from data entry.
    - Integrated key data sources from accounting (QuickBooks), manufacturing, sales, and marketing together for cohesive data flow.
    """)


# Skills
st.header("Skills & Applications Experience")
st.write("""
- **AI Frameworks:** Azure AI, Azure Prompt Flow, Langchain
- **API Interfaces:** Postman, Swagger, LlamaFile, Visual Studio
- **Data Management:** QuickBooks, Hubspot, WooCommerce, Excel, SQL, WordPress, JSON
- **Automation & Integration Tools:** Integromat (Make), Zapier, Airtable Automations
- **Web Technologies:** HTML, CSS, XML
- **Design & Development Tools:** Illustrator, Photoshop, Python, Google Data Studio, OpenAI, FlutterFlow
""")

# Education & Certifications
st.header("Education & Certifications")
st.write("""
- **MBA**, Utah Valley University (UVU)
- **Bachelor's Degree**, Brigham Young University (BYU)
- **Certification:** CompTIA Data+
""")

# Footer
st.write("---")
st.subheader("Contact Information")
st.write("""
Email: [brettwrightsemail@gmail.com](mailto:brettwrightsemail@gmail.com)
LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/bretttwright)
""")

# Add API Key Input in Sidebar for security and ease of access
with st.sidebar:
    openai_api_key = st.text_input("Enter OpenAI API Key", type="password", help="Paste your OpenAI API key here.")
    st.write("""If you do not have an OpenAI API Key, reach out to me and I'll send you one so you can try this out.""")

# Setup the chatbot interface
st.subheader("💬 Chat with Brett's Resume Bot - COMING SOON 05/24")
# st.caption("Feel free to ask me anything about my experience or projects!")

# Initialize or retrieve the chat history from session state
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# Display the chat history
# for message in st.session_state.chat_history:
#     role, content = message['role'], message['content']
#     if role == 'user':
#         st.text_area("You said:", value=content, height=50, disabled=True)
#     else:
#         st.text_area("Bot replied:", value=content, height=50, disabled=True)

# User input for new messages
# user_input = st.text_input("Type your question here...", key="new_message")

#  if st.button("Send"):
    # if not openai_api_key:
    #     st.error("Please add your OpenAI API key to continue.")
    # else:
    #     # Append user message to the history
    #     st.session_state.chat_history.append({"role": "user", "content": user_input})

    #     # Create an OpenAI client
    #     client = OpenAI(api_key=openai_api_key)

    #     # Generate a response using the OpenAI API
    #     try:
    #         response = client.chat.completions.create(
    #             model="gpt-3.5-turbo",
    #             messages=[{"role": "user", "content": user_input}]
    #         )
    #         bot_message = response['choices'][0]['message']['content']
    #         st.session_state.chat_history.append({"role": "assistant", "content": bot_message})
    #     except Exception as e:
    #         st.error(f"Failed to generate response: {e}")