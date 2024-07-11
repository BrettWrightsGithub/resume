import streamlit as st
import io
import os
from PIL import Image, ImageOps, ImageDraw

def app():
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the path to the PDF file
    pdf_file_path = os.path.join(current_dir, '/Users/brettwright/WebApps/resume-1/assets/Brett-Wright-Resume-5-2024.pdf')
    # Main Header
    st.title("Brett Wright")
    col1, col2 = st.columns([1, 1.5])

    with col1:
        # Open the PDF file to attach to the download button
        try:
            with open(pdf_file_path, "rb") as file:
                btn = st.download_button(
                    label="⬇️ Download Resume as PDF",
                    data=file,
                    file_name="Brett-Wright-Resume-2024.pdf",
                    mime="application/octet-stream")
        except FileNotFoundError:
            st.error(f"File not found: {pdf_file_path}")

    st.subheader("Technical Product Manager | Eagle Mountain, UT | 801-540-7574 | brettwrightsemail@gmail.com")
    def crop_to_circle(image_path, max_width=300):
        img = Image.open(image_path)
        size = (min(img.size),)*2
        img = ImageOps.fit(img, size, centering=(0.5, 0.5))
        if img.width > max_width:
            scale = max_width / img.width
            new_size = (int(img.width * scale), int(img.height * scale))
            img = img.resize(new_size, Image.Resampling.LANCZOS) 
        mask = Image.new('L', img.size, 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.ellipse((0, 0) + img.size, fill=255)
        img.putalpha(mask)
        return img

    image_path = "assets/Profile.jpg"
    image = crop_to_circle(image_path)
    with col1: 
        st.image(image, caption="Brett Wright")

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

    # Skills & Applications Experience
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