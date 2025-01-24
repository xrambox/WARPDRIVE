import streamlit as st

# Page configuration (MUST BE THE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="Alcubierre Warp Drive", page_icon="🚀", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    /* General styling */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTitle {
        font-size: 50px;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 20px;
    }
    .stSubheader {
        font-size: 30px;
        color: #2ca02c;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .stText {
        font-size: 20px;
        line-height: 1.6;
    }
    /* Navigation bar styling */
    .navbar {
        display: flex;
        justify-content: space-around;
        background-color: #1f1f1f;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .navbar a {
        color: white;
        text-decoration: none;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .navbar a:hover {
        background-color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Session state to manage page navigation
if "page" not in st.session_state:
    st.session_state.page = "Introduction"

# Navigation bar using Streamlit buttons
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("Introduction"):
        st.session_state.page = "Introduction"
with col2:
    if st.button("How It Works"):
        st.session_state.page = "How It Works"
with col3:
    if st.button("Revolutionizing Transport"):
        st.session_state.page = "Revolutionizing Transport"
with col4:
    if st.button("Challenges"):
        st.session_state.page = "Challenges"
with col5:
    if st.button("Future"):
        st.session_state.page = "Future"

# Function to handle page updates
def set_page():
    if st.session_state.page == "Introduction":
        introduction_page()
    elif st.session_state.page == "How It Works":
        how_it_works_page()
    elif st.session_state.page == "Revolutionizing Transport":
        revolutionizing_transport_page()
    elif st.session_state.page == "Challenges":
        challenges_page()
    elif st.session_state.page == "Future":
        future_page()

# Introduction Page
def introduction_page():
    st.markdown('<div class="stTitle">The Alcubierre Warp Drive</div>', unsafe_allow_html=True)
    st.markdown('<div class="stSubheader">A Future Beyond the Speed of Light</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stText">
        The Alcubierre Warp Drive is a theoretical concept in physics proposed by Mexican physicist Miguel Alcubierre in 1994. 
        It allows faster-than-light (FTL) travel by manipulating spacetime itself. Instead of moving through space at superluminal speeds, 
        the spacecraft moves space itself, creating a "warp bubble" that contracts spacetime in front of the ship and expands it behind, 
        enabling interstellar travel.
    </div>
    """, unsafe_allow_html=True)

    # Add the image of the Alcubierre Warp Drive concept
    st.image("image1.jpg", caption="Concept of the Alcubierre Warp Drive", use_container_width=True)


# How It Works Page
def how_it_works_page():
    st.markdown('<div class="stTitle">How It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stText">
        The Alcubierre Warp Drive allows faster-than-light (FTL) travel by manipulating spacetime. Instead of moving through space, 
        the spacecraft is enclosed in a "warp bubble" that contracts space in front of it and expands space behind it. 
        The ship itself doesn’t move within the bubble, but spacetime moves around it, enabling FTL travel without violating Einstein’s laws.
    </div>
    """, unsafe_allow_html=True)
    
    # Add the image of the Alcubierre Warp Drive concept
    st.image("image2.jpg", caption="Illustration of the Alcubierre Warp Bubble", use_container_width=True)


# Revolutionizing Transport Page
def revolutionizing_transport_page():
    st.markdown('<div class="stTitle">Revolutionizing Transportation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stText">
        - Travel to distant stars and galaxies in a matter of years instead of millennia.
        - No time dilation: Passengers age at the same rate as people on Earth.
        - Opens up the possibility of colonizing other planets and exploring the universe.
    </div>
    """, unsafe_allow_html=True)
    
    # Add the image of the Alcubierre Warp Drive concept
    st.image("image3.jpg", caption="Illustration of Alcubierre Warp Drive and Interstellar Travel", use_container_width=True)


# Challenges Page
# Challenges Page
def challenges_page():
    st.markdown('<div class="stTitle">Challenges and Risks</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stText">
        - Exotic Matter: Negative energy is needed to create the warp bubble.
        - Energy Requirements: The energy needed is currently beyond our capabilities.
        - Safety Concerns: High-energy particles could be dangerous for passengers and the destination.
    </div>
    """, unsafe_allow_html=True)
    
    # Add the image of the Alcubierre Warp Drive concept
    st.image("image4.jpg", caption="Challenges of the Alcubierre Warp Drive", use_container_width=True)


# Future Page
# Future Page
def future_page():
    st.markdown('<div class="stTitle">Future Prospects</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="stText">
        - Solving the exotic matter and energy requirements are the main obstacles.
        - Warp drive could be achievable in the next 100-200 years with technological advances.
        - It could unite humanity as a spacefaring civilization, enabling exploration and colonization of new worlds.
    </div>
    """, unsafe_allow_html=True)
    
    # Add the image related to the future prospects of Alcubierre Warp Drive
    st.image("image5.jpg", caption="Future Prospects of the Alcubierre Warp Drive", use_container_width=True)


# Render the current page
set_page()

# Footer
st.markdown("---")
st.markdown("BY Ankit Anand")
