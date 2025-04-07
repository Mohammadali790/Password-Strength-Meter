import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one uppercase letter (A-Z).")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one lowercase letter (a-z).")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one number (0-9).")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("🔴 Include at least one special character (!@#$%^&* etc.).")

    # Strength classification
    if score >= 5:
        strength = "✅ Strong"
        color = "green"
    elif score >= 3:
        strength = "🟡 Medium"
        color = "orange"
    else:
        strength = "🔴 Weak"
        color = "red"

    return strength, color, feedback, score

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter a password to evaluate:", type="password")

if password:
    strength, color, feedback, score = check_password_strength(password)

    # Display strength result
    st.markdown(f"### Strength: <span style='color:{color}; font-weight:bold;'>{strength}</span>", unsafe_allow_html=True)
    
    # Visual bar
    st.progress(min(score / 6, 1.0))  # Score out of 6 max

    # Feedback
    if feedback:
        st.markdown("#### Suggestions:")
        for item in feedback:
            st.markdown(f"- {item}")

    # Tip Box
    st.info("Tip: Use 12+ characters, mix upper/lowercase, numbers, and symbols to boost your password security! 🔐")

else:
    st.info("👆 Start typing your password above to check its strength.")

