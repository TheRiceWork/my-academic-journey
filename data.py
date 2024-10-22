import streamlit as st
import base64

# Function to load image and convert to base64
def load_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Set different background images for each section
def set_section_background(image_file):
    st.markdown(
        f"""
        <style>
        .section {{
            background-image: url(data:image/jpeg;base64,{image_file});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            height: 100%;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar for navigation
st.sidebar.title("Navigation")
sections = [
    "Home",
    "About Me",
    "Educational Background",
    "Experience",
    "Paper/Patent Publications",
    "Awards and Achievements",
    "Projects",
    "Membership",
    "Research Thrust Area",
    "List of Events",
    "Poster/Paper Presentation",
    "Courses Completed",
    "Contact Address"
]

# Button for each section
selected_section = st.sidebar.radio("Select a section:", sections)

# Set background images
background_images = {
    "Home": "background_home.jpg",
    "About Me": "background_about.jpg",
    "Educational Background": "background_education.jpg",
    "Experience": "background_experience.jpg",
    "Paper/Patent Publications": "background_publications.jpg",
    "Awards and Achievements": "background_awards.jpg",
    "Projects": "background_projects.jpg",
    "Membership": "background_membership.jpg",
    "Research Thrust Area": "background_research.jpg",
    "List of Events": "background_events.jpg",
    "Poster/Paper Presentation": "background_presentation.jpg",
    "Courses Completed": "background_courses.jpg",
    "Contact Address": "background_contact.jpg",
}

# Set the background for the selected section
set_section_background(load_image(background_images[selected_section]))

# Eye-catching title
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082; font-size: 48px;'>
        Welcome to My Academic Journey!
    </h1>
    <hr style='border: 2px solid #4B0082;'>
    """,
    unsafe_allow_html=True
)

# Function to add spacing
def add_spacing():
    st.write("\n" * 8)

# Main content based on selected section
if selected_section == "Home":
    st.header("Home")
    st.write("""
    Welcome to my personal website! I'm thrilled to share my academic journey with you. 
    Here, you will find details about my education, projects, and achievements. 
    Feel free to explore the different sections to learn more about my interests and experiences. 
    I am passionate about technology and dedicated to expanding my knowledge. 
    Join me as I navigate through my academic path and make meaningful contributions to the field.
    Your feedback and connections are always welcome!
    """)
    add_spacing()

elif selected_section == "About Me":
    st.header("About Me")
    st.write(""" I am a dedicated student with a passion for technology and learning. 
    My journey in the academic world has been filled with challenges and exciting discoveries. 
    I thrive on collaborating with peers and mentors to develop innovative solutions. 
    In my free time, I enjoy coding, exploring new technologies, and participating in hackathons. 
    I believe in continuous learning and am always on the lookout for opportunities to enhance my skills. 
    My goal is to make a positive impact through my work and inspire others along the way. 
    Let's connect and create something amazing together!""")
    add_spacing()

elif selected_section == "Educational Background":
    st.header("Educational Background")
    st.write(""" I am currently pursuing a Bachelor of Science in Computer Science at IEM NEWTOWN University. 
    Throughout my academic career, I have been committed to excellence and have consistently been on the Dean's List. 
    My studies have included a variety of subjects such as data structures, algorithms, and web development. 
    I have also completed several online courses on platforms like Coursera and NPTEL, enhancing my understanding of key concepts. 
    Additionally, I am actively involved in university clubs and organizations that focus on technology and innovation. 
    I am excited to leverage my educational background to tackle real-world problems and contribute to advancements in the field.
    """)
    add_spacing()

elif selected_section == "Experience":
    st.header("Experience")
    st.write("""
      I have gained valuable experience through internships and freelance projects. 
    At Tech Solutions, I developed a web application that streamlined internal processes and improved efficiency. 
    I also worked as a freelance web developer, where I collaborated with local businesses to create user-friendly websites. 
    My experiences have taught me the importance of communication and teamwork in delivering successful projects. 
    I am always eager to learn from challenges and adapt to new environments. 
    These experiences have solidified my desire to pursue a career in technology, where I can continue to grow and innovate.
    """)
    add_spacing()

elif selected_section == "Paper/Patent Publications":
    st.header("Paper/Patent Publications")
    st.write("""
    I have been fortunate to publish research papers and file patents during my academic journey. 
    One of my notable papers, "Exploring Machine Learning Techniques for Data Analysis," was published in the Science Journal in 2023. 
    This work involved extensive research on data processing and algorithm optimization. 
    Additionally, I filed a patent for an innovative algorithm that enhances data processing efficiency in real-time applications. 
    These experiences have deepened my interest in research and the potential of technology to solve complex problems. 
    I look forward to contributing further to the field with more impactful research in the future.
    """)
    add_spacing()

elif selected_section == "Awards and Achievements":
    st.header("Awards and Achievements")
    st.write("""
  I am proud to have received several accolades throughout my academic career. 
    Being on the Dean's List for two consecutive years is a testament to my hard work and dedication. 
    I also achieved first place in the National Coding Competition in 2023, where I showcased my programming skills against the best. 
    These accomplishments inspire me to strive for excellence and continue pushing my boundaries. 
    I believe that recognition is not just about the awards but also about the journey and the lessons learned along the way. 
    I am excited to take on new challenges that will lead to even more achievements.
    """)
    add_spacing()

elif selected_section == "Projects":
    st.header("Projects")
    project = st.selectbox("Choose a project to learn more about:", ["Personal Portfolio Website", "Data Visualization Dashboard"])
    if project == "Personal Portfolio Website":
        st.write("A website showcasing my skills and projects.")
    elif project == "Data Visualization Dashboard":
        st.write("A data visualization dashboard is an interactive tool that displays data from various sources in a visual format to help users understand it")
    add_spacing()

elif selected_section == "Membership":
    st.header("Membership")
    st.write("""
     I am an active member of several organizations that focus on technology and innovation. 
    Being a part of the Computer Science Club has allowed me to network with peers and engage in collaborative projects. 
    I also participate in various hackathons, where I can apply my skills in a competitive environment and learn from others. 
    These experiences have enriched my academic journey and provided me with opportunities to grow as a professional. 
    I believe that being involved in such organizations is crucial for personal and professional development. 
    I look forward to contributing to more initiatives that inspire and educate others.
    """)
    add_spacing()

elif selected_section == "Research Thrust Area":
    st.header("Research Thrust Area")
    thrust_area = st.selectbox("Select a research area:", ["Artificial Intelligence", "Machine Learning", "Data Science"])
    st.write(f"You selected: **{thrust_area}**")
    add_spacing()

elif selected_section == "List of Events":
    st.header("List of Events (Organized/Attended)")
    st.write("""
Throughout my academic career, I have organized and attended numerous events. 
    I was the organizer for the Annual Tech Fest in 2023, which brought together industry professionals and students. 
    This experience taught me valuable skills in event management and networking. 
    Additionally, I attended the AI Conference in 2022, where I gained insights from leading experts in the field. 
    Participating in such events has broadened my perspective and fueled my passion for technology. 
    I look forward to being involved in
    """)
    add_spacing()

elif selected_section == "Poster/Paper Presentation":
    st.header("Poster/Paper Presentation")
    st.write("""
    - Presented research on data analysis at the University Symposium, 2023.
    """)
    add_spacing()

elif selected_section == "Courses Completed":
    st.header("Courses Completed")
    courses = st.multiselect("Select courses you've completed:",
                              ["NPTEL: Data Structures and Algorithms",
                               "Coursera: Machine Learning by Andrew Ng",
                               "LinkedIn Learning: Web Development Foundations"])
    st.write("You selected:", courses)
    add_spacing()

elif selected_section == "Contact Address":
    st.header("Contact Address")
    st.write("You can reach me at: legendh151@gmail.com")
    add_spacing()

# Footer
st.write("Thank you for visiting my academic journey!")
