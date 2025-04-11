import re
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Password Strength Checker By Mizna Moin", page_icon="🔑", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
        }
        .main {
            text-align: center;
        }
        .stTextInput > div > div > input {
            background-color: #ffffff;
            border: 2px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            font-size: 18px;
            margin-top: 20px;
            border-radius: 8px;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #45a049;
            transform: scale(1.02);
        }
        .stExpanderHeader {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🛡️ Password Strength Generator")
st.write("Enter your password below to check its security level 🔍")

# Function to check password strength
def check_password_strength(Password):
    score = 0
    feedback = []

    if len(Password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be **at least 8 characters long**.")

    if re.search(r"[A-Z]", Password) and re.search(r"[a-z]", Password):
        score += 1
    else:
        feedback.append("❌ Password must include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", Password):
        score += 1
    else:
        feedback.append("❌ Password must include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", Password):
        score += 1
    else:
        feedback.append("❌ Password must include **at least one special character (!@#$%^&*)**.")

    if score == 4:
        st.success("✔️ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("‼️ **Weak Password** - Follow the suggestions below to strengthen it.")

    if feedback:
        with st.expander("💹 **Improve your password**"):
            for item in feedback:
                st.write(item)

# Input and Button
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")

if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")

# Footer
st.markdown("---")
st.markdown('<div style="text-align: center; font-weight: bold;">🔧 Developed by Hiba Moin</div>', unsafe_allow_html=True)
