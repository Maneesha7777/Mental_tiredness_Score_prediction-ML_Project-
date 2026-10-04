import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Mental Tiredness Predictor",
    page_icon="🧠",
    layout="wide"
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

with open("model_pipe (1).pkl", "rb") as file:
    model = pickle.load(file)


# =========================================================
# TITLE
# =========================================================

st.title("🧠 Mental Tiredness Score Predictor")

st.write(
    "Predict your mental tiredness score using daily activity, "
    "work and lifestyle factors."
)

st.info(
    "💡 Enter your daily work, sleep, lifestyle and environmental "
    "details to estimate your mental tiredness score using the "
    "trained XGBoost model."
)


# =========================================================
# WORK & DAILY ACTIVITY
# =========================================================

st.header("💼 Work & Daily Activity")

col1, col2, col3 = st.columns(3)

with col1:
    number_of_decisions_made = st.number_input(
        "🧩 Number of Decisions Made Today",
        min_value=0,
        value=20,
        step=1
    )

with col2:
    context_switch_count = st.number_input(
        "🔄 Number of Task/Context Switches",
        min_value=0,
        value=10,
        step=1
    )

with col3:
    notifications_received = st.number_input(
        "🔔 Notifications Received",
        min_value=0,
        value=50,
        step=1
    )


col1, col2, col3 = st.columns(3)

with col1:
    screen_time_min = st.number_input(
        "💻 Screen Time (minutes)",
        min_value=0.0,
        value=300.0,
        step=10.0
    )

with col2:
    deep_work_min = st.number_input(
        "🎯 Deep Work Time (minutes)",
        min_value=0.0,
        value=120.0,
        step=10.0
    )

with col3:
    task_complexity_avg = st.slider(
        "📋 Average Task Complexity",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )


# =========================================================
# WORK ENVIRONMENT
# =========================================================

st.header("🏢 Work Environment")

col1, col2 = st.columns(2)

with col1:
    work_type_category = st.selectbox(
        "💼 Work Type",
        [
            "Office",
            "Remote",
            "Hybrid"
        ]
    )

with col2:
    environment_type = st.selectbox(
        "🌿 Environment Type",
        [
            "Quiet",
            "Moderate",
            "Noisy"
        ]
    )


# =========================================================
# WORK TYPE MAPPING
# =========================================================

work_type_mapping = {
    "Office": 0,
    "Remote": 1,
    "Hybrid": 2
}

work_type = work_type_mapping[work_type_category]


# =========================================================
# ENVIRONMENT → NOISE LEVEL
# =========================================================

environment_noise_mapping = {
    "Quiet": 30.0,
    "Moderate": 50.0,
    "Noisy": 70.0
}

noise_level_db = environment_noise_mapping[environment_type]


# =========================================================
# LIFESTYLE & WELLBEING
# =========================================================

st.header("🌿 Lifestyle & Wellbeing")

col1, col2, col3 = st.columns(3)

with col1:
    caffeine_mg = st.number_input(
        "☕ Caffeine Intake (mg)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with col2:
    break_frequency = st.number_input(
        "☕ Number of Breaks Taken",
        min_value=0.0,
        value=3.0,
        step=1.0
    )

with col3:
    hydration_l = st.number_input(
        "💧 Water Intake (Litres)",
        min_value=0.0,
        value=2.0,
        step=0.1
    )


# =========================================================
# MOOD
# =========================================================

mood_category = st.select_slider(
    "😊 How would you describe your mood today?",
    options=[
        "Very Low",
        "Low",
        "Neutral",
        "Good",
        "Excellent"
    ],
    value="Neutral"
)


# =========================================================
# MOOD MAPPING
# =========================================================

mood_mapping = {
    "Very Low": 2.0,
    "Low": 4.0,
    "Neutral": 5.0,
    "Good": 7.0,
    "Excellent": 9.0
}

mood = mood_mapping[mood_category]


# =========================================================
# SLEEP
# =========================================================

st.header("😴 Sleep")

col1, col2 = st.columns(2)

with col1:
    sleep_hours = st.number_input(
        "🌙 Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

with col2:
    deep_sleep_pct = st.slider(
        "💤 Deep Sleep Percentage (%)",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=1.0
    )


# =========================================================
# WORKLOAD
# =========================================================

st.header("📊 Workload")

workload_score = st.slider(
    "🔥 Current Workload Level",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.5
)


# =========================================================
# FEATURE ENGINEERING
# =========================================================

deep_sleep_hours = (
    sleep_hours * deep_sleep_pct / 100
)

interruption_load = (
    context_switch_count + notifications_received
)


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🧠 Predict Mental Tiredness Score",
    use_container_width=True
)


# =========================================================
# MODEL PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------------
    # CREATE INPUT DATAFRAME
    # -----------------------------------------------------

    input_data = pd.DataFrame({

        "number_of_decisions_made": [
            number_of_decisions_made
        ],

        "context_switch_count": [
            context_switch_count
        ],

        "notifications_received": [
            notifications_received
        ],

        "screen_time_min": [
            screen_time_min
        ],

        "deep_work_min": [
            deep_work_min
        ],

        "task_complexity_avg": [
            task_complexity_avg
        ],

        "caffeine_mg": [
            caffeine_mg
        ],

        "break_frequency": [
            break_frequency
        ],

        "deep_sleep_pct": [
            deep_sleep_pct
        ],

        "hydration_l": [
            hydration_l
        ],

        "mood": [
            mood
        ],

        "work_type": [
            work_type
        ],

        "noise_level_db": [
            noise_level_db
        ],

        "workload_score": [
            workload_score
        ],

        "deep_sleep_hours": [
            deep_sleep_hours
        ],

        "interruption_load": [
            interruption_load
        ]
    })


    # -----------------------------------------------------
    # PREDICT
    # -----------------------------------------------------

    prediction = model.predict(input_data)

    predicted_score = float(prediction[0])


    # =====================================================
    # RESULT
    # =====================================================

    st.divider()

    st.subheader("🎯 Prediction Result")

    st.metric(
        label="Predicted Mental Tiredness Score",
        value=f"{predicted_score:.2f}"
    )


    # =====================================================
    # INTERPRETATION
    # =====================================================

    if predicted_score < 20:

        st.success(
            "🌱 The predicted mental tiredness level is relatively low."
        )

    elif predicted_score < 40:

        st.info(
            "🙂 The predicted mental tiredness level is moderate."
        )

    else:

        st.warning(
            "😴 The predicted mental tiredness level is relatively high."
        )


    # =====================================================
    # PREDICTION DETAILS
    # =====================================================

    with st.expander("🔍 View Prediction Details"):

        st.subheader("Your Input Summary")

        detail_col1, detail_col2, detail_col3 = st.columns(3)

        with detail_col1:

            st.write(
                f"**💼 Work Type:** {work_type_category}"
            )

            st.write(
                f"**🌿 Environment:** {environment_type}"
            )

            st.write(
                f"**😊 Mood:** {mood_category}"
            )

        with detail_col2:

            st.write(
                f"**😴 Sleep Hours:** {sleep_hours:.1f}"
            )

            st.write(
                f"**💤 Deep Sleep:** {deep_sleep_pct:.1f}%"
            )

            st.write(
                f"**💧 Hydration:** {hydration_l:.1f} L"
            )

        with detail_col3:

            st.write(
                f"**💻 Screen Time:** {screen_time_min:.0f} min"
            )

            st.write(
                f"**🎯 Deep Work:** {deep_work_min:.0f} min"
            )

            st.write(
                f"**🔥 Workload:** {workload_score:.1f}/10"
            )


        st.divider()

        st.subheader("Calculated Features")

        calc_col1, calc_col2 = st.columns(2)

        with calc_col1:

            st.write(
                f"**💤 Deep Sleep Hours:** "
                f"{deep_sleep_hours:.2f}"
            )

        with calc_col2:

            st.write(
                f"**🔔 Interruption Load:** "
                f"{interruption_load:.0f}"
            )