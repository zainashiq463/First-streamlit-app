import streamlit as st
import pandas as pd

st.set_page_config(page_title="Daily Health & Productivity Tracker", layout="wide")
st.title("💪 Daily Health & Productivity Tracker")
st.write("Input your daily stats and track your productivity and health habits.")

# --- FORM SECTION ---
with st.form("daily_form"):

    st.subheader("📋 Enter Your Daily Stats")

    col1, col2 = st.columns(2)

    with col1:
        focus_hours = st.number_input("⏳ Hours of Focused Work", min_value=0, max_value=12, value=4)
        sleep_hours = st.number_input("😴 Sleep Hours", min_value=0, max_value=12, value=7)
        exercise_minutes = st.number_input("🏋 Exercise Minutes", min_value=0, max_value=180, value=30)

    with col2:
        water_glasses = st.number_input("💧 Glasses of Water", min_value=0, max_value=20, value=8)
        screen_hours = st.number_input("📱 Hours on Screen", min_value=0, max_value=12, value=5)
        stress_level = st.slider("😵 Stress Level", min_value=1, max_value=10, value=5)

    # Select multiple healthy habits
    healthy_habits = st.multiselect(
        "✅ Healthy Habits Practiced Today",
        ["Meditation", "Reading", "Balanced Diet", "Walking", "Journaling"]
    )

    submit = st.form_submit_button("Submit Daily Stats")

# --- PROCESS AND DISPLAY ---
if submit:

    st.success("✅ Data Submitted Successfully!")

    # --- Calculate a simple Productivity Score ---
    # Score formula is illustrative
    productivity_score = (
        focus_hours * 5 +
        sleep_hours * 3 +
        exercise_minutes * 0.5 +
        water_glasses * 2 -
        screen_hours * 2 -
        stress_level * 3
    )
    productivity_score = max(0, min(productivity_score, 100))  # keep between 0-100

    # --- Display Data ---
    st.subheader("📊 Today's Summary")
    summary_data = {
        "Focused Work Hours": focus_hours,
        "Sleep Hours": sleep_hours,
        "Exercise Minutes": exercise_minutes,
        "Water Intake (Glasses)": water_glasses,
        "Screen Time (Hours)": screen_hours,
        "Stress Level": stress_level,
        "Healthy Habits": ", ".join(healthy_habits) if healthy_habits else "None",
        "Productivity Score": productivity_score
    }

    summary_df = pd.DataFrame([summary_data])
    st.table(summary_df)

    # --- Simple Recommendations ---
    st.subheader("🧠 Recommendations")
    if focus_hours < 3:
        st.write("- Increase focused work sessions for better productivity.")
    if sleep_hours < 6:
        st.write("- Try to get adequate sleep for health.")
    if exercise_minutes < 30:
        st.write("- Aim for at least 30 minutes of exercise.")
    if water_glasses < 6:
        st.write("- Drink more water for hydration.")
    if screen_hours > 6:
        st.write("- Reduce screen time to decrease eye strain and fatigue.")
    if stress_level > 6:
        st.write("- Try meditation or relaxation techniques today.")
