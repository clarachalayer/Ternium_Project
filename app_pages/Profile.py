import streamlit as st

def main():
    st.image("images/ternium_logo.png", width=140) 
    # Page header
    st.title("User Profile")
    st.write("Here you can view your basic profile information.")

    # Main container
    with st.container():
        col1, col2 = st.columns([1, 3])

        # Profile picture
        with col1:
            st.image("images/profile_image.png", width=150)  # Ensure the image is in the correct path

        # User information
        with col2:
            st.subheader("Team 4 Seiketsu")
            st.write("seiketsu@gmail.com")
            st.write("📍 Monterrey, NL")
            st.write("🔶 Data analysis and project management.")

    st.markdown("---")

    # Additional information section
    st.subheader("Personal Information")
    st.write("**Date of Birth:** May 12, 1990")
    st.write("**Phone:** +1 234 567 890")
    st.write("**Occupation:** Software Engineer")
    st.write("**Interests:** Data Science, Machine Learning, Project Management")
    
    st.markdown(
    """
    <style>
    /* Fixed footer at the bottom */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000000;
        color: white;
        text-align: right;
        padding: 10px;
        font-size: 14px;
    }
    /* Adjust bottom padding to prevent content overlap with the footer */
    .main > div {
        padding-bottom: 50px;
    }
    </style>
    <div class="footer">
        Seiketsu Consulting &copy; 2023
    </div>
    """,
    unsafe_allow_html=True
)
