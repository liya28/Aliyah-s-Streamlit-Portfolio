# app.py
import streamlit as st
from PIL import Image
import os
import csv
from datetime import datetime

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Aliyah Khaet Regacho — Portfolio",
    page_icon="✨",
    layout="wide"
)

LINKEDIN_URL = "https://www.linkedin.com/in/aliyahregacho0528/"
RESUME_FILENAME = "resume.pdf"
CONTACTS_FILENAME = "contacts.csv"
PORTFOLIO_URL = "https://www.canva.com/design/DAGSnLhy04U/19rPO8edboYw9jYQ1wz9FQ/view?utm_content=DAGSnLhy04U&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=had92145dc4"


def load_css(file_name):
    """Loads and injects custom CSS."""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file '{file_name}' not found.")

def render_portfolio_link():
    st.markdown(
        f"""
        <a href='{PORTFOLIO_URL}' target='_blank' style='text-decoration: none;'>
            <button style='
                background-color: #6d5cff; 
                color: white; 
                padding: 10px 14px; 
                border: none; 
                border-radius: 10px; 
                font-size: 14px;
                cursor: pointer;
                width: 100%;
                margin: 0;
            '>
                View Online Portfolio
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

def save_contact(email: str, subject: str, message: str):
    """Append contact submission to contacts.csv with timestamp."""
    try:
        is_new_file = not os.path.exists(CONTACTS_FILENAME)
        
        with open(CONTACTS_FILENAME, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if is_new_file:
                writer.writerow(["timestamp", "email", "subject", "message"])
                
            writer.writerow([datetime.now().isoformat(), email, subject, message])
        return True
    except Exception as e:
        st.error(f"Error saving contact: {e}")
        return False

def render_contact_buttons():
    """Renders the reusable Download Resume and LinkedIn buttons."""
    if os.path.exists(RESUME_FILENAME):
        with open(RESUME_FILENAME, "rb") as f:
            st.download_button(
                "Download Resume", 
                f, 
                file_name="Aliyah-Regacho-Resume.pdf", 
                key=f"download_resume_{st.session_state.page_selection}",
                use_container_width=True 
            )
    else:
        st.info(f"Add {RESUME_FILENAME} to enable download button.")
        
    st.markdown(
        f"<div style='height:8px;'></div><a href='{LINKEDIN_URL}' target='_blank'><button class='cvbtn' style='width:100%;'>Visit LinkedIn</button></a>", 
        unsafe_allow_html=True
    )

load_css("style.css")


# ------------------ HEADER / NAV ------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='glass hero'>", unsafe_allow_html=True)
    st.markdown("<h1 style='margin:0;'>Aliyah Khaet Regacho, CePL</h1>", unsafe_allow_html=True)
    st.markdown("<div class='muted'>Cebu, Philippines • +63 966 223 1048 • liyahregacho@gmail.com</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True) 
    st.markdown("<div class='typing'>Computer Science Student • Freelancer • Virtual Assistant</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if os.path.exists("images/me.png"):
        img = Image.open("images/me.png")
        st.image(img, width=220)

# ------------------ MULTI-PAGE NAV (Sidebar) ------------------
st.sidebar.markdown("<div class='glass' style='padding:16px;'>", unsafe_allow_html=True)
st.sidebar.title("Navigation")
pages = ["Home", "Experience", "Technical Projects", "Education", "Certifications & Activities", "Leadership Roles", "Skills", "Contact"]

page = st.sidebar.radio(
    "", 
    pages, 
    key="page_selection" # Direct key binding ensures state is updated efficiently
)
st.sidebar.markdown("</div>", unsafe_allow_html=True)


page = st.session_state.page_selection

if page == "Home":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>About</div>", unsafe_allow_html=True)
    st.write("""
    I'm Aliyah, a Computer Science student at Cebu Institute of Technology - University.
    I work remotely on automation, documentation, and design projects while pursuing a career in law and tech policy.
    """)

    # contact and resume
    rcol1, rcol2 = st.columns([2,1])
    with rcol1:
        st.markdown("<div class='glass'>", unsafe_allow_html=True)
        st.markdown("**Professional Summary**")
        st.write("""
        A detail-oriented automation specialist and documentation lead with experience creating
        workflows, processing large datasets, and delivering client-facing content. Skilled in
        design (Canva), basic web stacks (HTML/CSS/PHP), and programming fundamentals (C/C++/Java).
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    with rcol2:
        st.markdown("<div class='glass' style='text-align:center;'>", unsafe_allow_html=True)
        render_contact_buttons()
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ EXPERIENCE PAGE ------------------
elif page == "Experience":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Professional Experience</div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 20px;'>", unsafe_allow_html=True)
    render_portfolio_link() # Call the new URL link function
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("---") 
    
    st.subheader("Executive General Manager & Documentation Officer — VERGE Inc. (Remote)")
    st.caption("July - September 2024")
    
    st.write("• Created system manuals, team leader protocols, and community outreach guidelines, forming a cohesive resource framework for ongoing initiatives.") 
    st.write("• Improved documentation efficiency with a systematic database, enhancing cross-team access and communication.")
    st.write("• Established standardized process, driving efficient project completion and stronger interdepartmental collaboration.")

    st.markdown("---")

    st.subheader("Automation Specialist — VERGE Inc. (Remote)")
    st.caption("July - August 2024")
    
    st.write("• Developed and executed automated workflows for the HR Department, enhancing application responsiveness and fostering improved internal cooperation.")
    st.write("• Created a comprehensive SaaS-focused website with organized product listings to enhance customer navigation and interaction.")
    st.write("• Successfully incorporated more than a hundred CSV files of leads into a software tool, improving data accessibility and functionality for team use.")
    st.write("• Created focused content for marketing campaigns, boosting brand awareness and interaction.")

    st.markdown("---")

    st.subheader("Freelance Graphics Designer — Self-Employed")
    
    st.write("• Create customized visual designs using Canva for diverse client requirements.") 
    st.write("• Generate engaging content to complement design deliverables.") 
    st.write("• Optimize existing designs for enhanced professional appeal and project alignment.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ TECHNICAL PROJECTS PAGE ------------------
elif page == "Technical Projects":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Technical Projects</div>", unsafe_allow_html=True)

    st.subheader("Finish Line — (OOP2 Capstone)")
    st.caption("Java, JavaFX, MySQL (JDBC), CSS, Git, XAMPP")
    st.write("""
    Finish Line is a typing game developed as a capstone project to sharpen typing skills while reinforcing core concepts from the CIT-U Computer Science curriculum. Built using Java, JavaFX, MySQL (via JDBC), and CSS, with GitHub for version control and XAMPP for local server deployment.
    """)
    if os.path.exists("images/project_finishline.png"):
        st.image("images/project_finishline.png", use_column_width=True)

    st.markdown("---")

    st.subheader("QuickCart — (Mobile Development)")
    st.caption("Kotlin / Android")
    st.write("""
    QuickCart is a Kotlin-based Android app that streamlines grocery list creation and management. Designed for convenience and speed, it features an intuitive UI that helps users plan, organize, and shop efficiently.
    """)
    if os.path.exists("images/project_quickcart.png"):
        st.image("images/project_quickcart.png", use_column_width=True)

    st.markdown("---")

    st.subheader("AIO StuBu — (OOP1 Capstone)")
    st.caption("Java, JavaFX")
    st.write("""
    All-In-One Study Buddy (StuBu) is an offline-first Windows desktop app designed to equip students with essential academic tools on one platform. Developed using Java and JavaFX, it focuses on productivity, accessibility, and modular utility for learners.
    """)
    if os.path.exists("images/project_aiostubu.png"):
        st.image("images/project_aiostubu.png", use_column_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ EDUCATION PAGE ------------------
elif page == "Education":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Education</div>", unsafe_allow_html=True)
    
    st.subheader("Cebu Institute of Technology - University")
    st.caption("Bachelor of Science in Computer Science | 2023 - Present")
    
    st.write("**Awards & Recognition**")
    st.write("• Overall Rank 9 in Computer Science Department of A.Y 23-24, FlexhibIT Awards (2024)") 
    st.write("• Academic Achiever, Parangal Awards (2025)")
    st.write("• College Scholar, Parangal Awards (2024)")
    st.write("• Recent GPA: 4.6/5.0")
    
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ CERTIFICATIONS & ACTIVITIES PAGE ------------------
elif page == "Certifications & Activities":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Certifications, Projects & Seminars</div>", unsafe_allow_html=True)

    # 2. Certifications
    st.write("**Certifications**")
    st.write("- Certified Paralegal, Certified Paralegal and Legal Researchers, Inc. (September 2025)")
    st.write("- Passer, Civil Service Examination Professional Level (August 2025)")
    st.write("- Certification of Completion, Canva Education: Graphics Design Essential (October 2024)")
    st.write("- Part of the Top 1%, CodeChum C Language Certification Examination (May 2024)")

    st.markdown("---")
    st.write("**Projects & Events**")
    st.write("- Volunteer - CIT-U College of Computer Studies Infographics Using Canva Seminar for ALS (June 2025)")
    st.write("- Technical Working Committee Head - CIT-U SSG Elections (May 2025)")
    st.write("- Technical Working Committee Head - CIT-U EDS – TINGOG (March 2025)")
    st.write("- Working Committee Member - CIT-U Intramurals (March 2025)")
    st.write("- Working Committee Member - CIT-U CCS Days: The Pixelated Playground (May 2024)")
    st.write("- Working Committee Member - CIT-U CSS Tutorials 2.0 (October 2023)")

    st.markdown("---")
    st.write("**Seminars & Conferences**")
    st.write("- Best Delegate - CIT-U Model United Nations ECOSOC (July 2025)")
    st.write("- Participant - U-Konek: Youth Initiatives for Collaborative Civic Education (June 2025)")
    st.write("- Participant - MIX 4.0: SDG Champions Ideas Sharing Session (March 2025)")
    st.write("- Participant - Cebu City SSC-G Tertiary Federation – Voter Education Forum (April 2025)")
    st.write("- Semifinalist Adjudicator – Visayas Novice Debate Cup (December 2024)")
    st.write("- Delegate - ASEAN: Digital Literacy Programme Orientation (March 2023)")
    st.write("- Delegate - Ka-Dasig Youth Organization: Team Building (March 2023)")
    st.write("- Participant - JCI Philippines AREA 5 NSDM Celebration (Dec 2022)")
    st.write("- Participant - Kilos Ko Youth Fellowship Program (Dec 2021)")
    st.write("- Delegate - Youth Ally for Safe Space Movers (Nov 2021)")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ LEADERSHIP PAGE ------------------
elif page == "Leadership Roles":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Leadership Roles</div>", unsafe_allow_html=True)
    
    if os.path.exists("images/leadership.jpg"):
        st.image("images/leadership.jpg", caption="My organizations through the years", use_container_width=True)
    
    st.write("**Organizations & Roles**")
    st.write("- Director for Partnership - Google Developer Groups on Campus - CIT-U (2025-2026)")
    st.write("- Officer - CIT-U Computer Students’ Society Committee on Networks and Linkages (2025-2026)")
    st.write("- Secretary - CIT-U Elite Debate Society (2025-2026)")
    st.write("- Commissioner (Media and Archives) - CIT-U Supreme Student Government Committee on Public Relations (2025-2026)")
    st.write("- Head - CIT-U SSG Commission on Elections Technical Committee (2024-2025)")
    st.write("- Member - CIT-U Google Developer Students Club (2023-2024)")
    st.write("- Assistant Head - CIT-U Computer Students’ Society Committee on Logistics (2023-2024)")
    st.write("- President - Talisay City National High School Supreme Secondary Learner’s Government (2022-2023)")
    st.write("- Secretary, Supreme Student Government (2020-2021)")
    st.write("- Public Information Officer, Supreme Student Government (2019-2020)")
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ SKILLS PAGE ------------------
elif page == "Skills":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Technical & Soft Skills</div>", unsafe_allow_html=True)

    tech_skills = [
        "GoHighLevel", "Canva", "Figma", "HTML", "CSS", "PHP (Beginner)",
        "Trello", "Slack", "Zoho", "SurveySparrow", "MS Office", "Google Workspace",
        "C", "C++", "Java", "VS Code", "IntelliJ", "Scene Builder - Gluon"
    ]
    st.write("**Technical:**")
    st.markdown(" ".join([f"<span class='badge'>{s}</span>" for s in tech_skills]), unsafe_allow_html=True)

    st.write("")
    st.write("**Soft Skills:**")
    soft = [
        "Remote team collaboration", "Strategic planning", "Documentation", "Leadership and team management",
        "Time management", "Client relations", "Public speaking", "Event organization"
    ]
    st.markdown(" ".join([f"<span class='badge'>{s}</span>" for s in soft]), unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ CONTACT PAGE ------------------
elif page == "Contact":
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)

    colL, colR = st.columns([2,1])
    with colL:
        st.write("If you want to connect, drop your email and a short message — I’ll respond as soon as I can.")
        with st.form("contact_form"):
            sender_email = st.text_input("Your email", value="")
            subject = st.text_input("Subject (optional)", value="")
            message = st.text_area("Message", height=150)
            submit = st.form_submit_button("Send message")
            
            if submit:
                # Basic email format check
                is_valid_email = "@" in sender_email and "." in sender_email
                if not sender_email or not message or not is_valid_email:
                    st.error("Please enter a **valid email address** and a **short message**.")
                elif save_contact(sender_email, subject, message):
                    st.success("Thanks. Your message was saved. I will reply as soon as possible!")
                else:
                    st.error("There was an error saving your message.")
                    
    with colR:
        st.markdown("<div class='glass' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<b>Aliyah Khaet Regacho, CePL</b><br>BS Computer Science<br>Cebu Institute of Technology - University<br>N. Bacalso Avenue, Cebu City", unsafe_allow_html=True)
        st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)
        
        render_contact_buttons()
        
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------ FOOTER ------------------
st.markdown("<div style='text-align:center; margin-top:22px; color:#6b6f82;'>BSCS - 3 F1 • Data Analytics and Visualization • Streamlit Project</div>", unsafe_allow_html=True)