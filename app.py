import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & CONFIGURATION
# -----------------------------------------------------------------------------

st.set_page_config(
    page_title="Credit Risk & Default Assessment",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Risk Assessment & Default Decision Engine")
st.markdown(
    "Assess loan applicant default risk using our optimized XGBoost ML pipeline."
)

# -----------------------------------------------------------------------------
# 2. LOAD SAVED MODEL ARTIFACTS
# -----------------------------------------------------------------------------

@st.cache_resource
def load_artifacts():
    model = joblib.load("xgboost_credit_model.joblib")
    preprocessor = joblib.load("preprocessor.joblib")
    threshold = joblib.load("optimal_threshold.joblib")

    return model, preprocessor, threshold


try:
    model, preprocessor, optimal_threshold = load_artifacts()

    st.sidebar.success("Model artifacts loaded successfully!")

except Exception as e:
    st.error(f"Error loading model artifacts: {e}")
    st.stop()


# -----------------------------------------------------------------------------
# 3. SIDEBAR: APPLICANT INPUT FORM
# -----------------------------------------------------------------------------

st.sidebar.header("📋 Applicant Profile")

person_age = st.sidebar.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=28
)

person_income = st.sidebar.number_input(
    "Annual Income ($)",
    min_value=1000,
    max_value=5000000,
    value=60000,
    step=5000
)

person_emp_length = st.sidebar.number_input(
    "Employment Length (Years)",
    min_value=0.0,
    max_value=60.0,
    value=3.0,
    step=0.5
)

person_home_ownership = st.sidebar.selectbox(
    "Home Ownership Status",
    ["RENT", "MORTGAGE", "OWN", "OTHER"]
)

cb_person_default_on_file = st.sidebar.selectbox(
    "Historical Default on File?",
    ["N", "Y"]
)

cb_person_cred_hist_length = st.sidebar.number_input(
    "Credit History Length (Years)",
    min_value=0,
    max_value=50,
    value=4
)


st.sidebar.header("💰 Loan Details")

loan_intent = st.sidebar.selectbox(
    "Loan Intent",
    [
        "PERSONAL",
        "EDUCATION",
        "MEDICAL",
        "VENTURE",
        "HOMEIMPROVEMENT",
        "DEBTCONSOLIDATION"
    ]
)

loan_grade = st.sidebar.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)

loan_amnt = st.sidebar.number_input(
    "Requested Loan Amount ($)",
    min_value=500,
    max_value=100000,
    value=10000,
    step=1000
)

loan_int_rate = st.sidebar.number_input(
    "Interest Rate (%)",
    min_value=1.0,
    max_value=40.0,
    value=11.0,
    step=0.5
)


# -----------------------------------------------------------------------------
# 4. FEATURE ENGINEERING
# -----------------------------------------------------------------------------
#
# IMPORTANT:
# These formulas exactly match STEP 2 of the training notebook.
#
# Training notebook:
#
# debt_to_income_ratio =
#     loan_amnt / person_income
#
# annual_interest_cost =
#     loan_amnt * (loan_int_rate / 100)
#
# interest_to_income_ratio =
#     annual_interest_cost / person_income
#
# credit_hist_ratio =
#     cb_person_cred_hist_length / max(person_age - 18, 1)
#
# -----------------------------------------------------------------------------

# Loan amount relative to annual income
debt_to_income_ratio = (
    loan_amnt / person_income
    if person_income > 0
    else 0
)

# Annual interest cost
annual_interest_cost = (
    loan_amnt * (loan_int_rate / 100)
)

# Interest burden relative to income
interest_to_income_ratio = (
    annual_interest_cost / person_income
    if person_income > 0
    else 0
)

# Adult age used for credit history calculation
adult_age = max(person_age - 18, 1)

# Credit history length relative to adult age
credit_hist_ratio = (
    cb_person_cred_hist_length / adult_age
)


# -----------------------------------------------------------------------------
# 5. CONSTRUCT INPUT DATAFRAME
# -----------------------------------------------------------------------------
#
# These columns must match the features used when fitting preprocessor.joblib.
#
# -----------------------------------------------------------------------------

raw_data = pd.DataFrame([{

    # Original numerical features
    "person_age": person_age,
    "person_income": person_income,
    "person_emp_length": person_emp_length,
    "loan_amnt": loan_amnt,
    "loan_int_rate": loan_int_rate,
    "loan_percent_income": debt_to_income_ratio,
    "cb_person_cred_hist_length": cb_person_cred_hist_length,

    # Original categorical features
    "person_home_ownership": person_home_ownership,
    "loan_intent": loan_intent,
    "loan_grade": loan_grade,
    "cb_person_default_on_file": cb_person_default_on_file,

    # Engineered features used during training
    "debt_to_income_ratio": debt_to_income_ratio,
    "annual_interest_cost": annual_interest_cost,
    "interest_to_income_ratio": interest_to_income_ratio,
    "credit_hist_ratio": credit_hist_ratio
}])


# -----------------------------------------------------------------------------
# 6. PREDICTION & DISPLAY
# -----------------------------------------------------------------------------

col1, col2 = st.columns([1, 1])


# -----------------------------------------------------------------------------
# LEFT COLUMN: FINANCIAL RATIOS
# -----------------------------------------------------------------------------

with col1:

    st.subheader("📊 Key Financial Ratios")

    st.write(
        f"**Loan-to-Income Ratio:** "
        f"`{debt_to_income_ratio:.2%}`"
    )

    st.write(
        f"**Annual Interest Cost:** "
        f"${annual_interest_cost:,.2f}"
    )

    st.write(
        f"**Interest-to-Income Ratio:** "
        f"`{interest_to_income_ratio:.2%}`"
    )

    st.write(
        f"**Credit History / Adult Age Ratio:** "
        f"`{credit_hist_ratio:.3f}`"
    )


# -----------------------------------------------------------------------------
# RIGHT COLUMN: RISK ASSESSMENT
# -----------------------------------------------------------------------------

with col2:

    st.subheader("🎯 Risk Assessment Output")

    try:

        # ---------------------------------------------------------------------
        # PREPROCESS INPUT
        # ---------------------------------------------------------------------

        processed_input = preprocessor.transform(raw_data)

        # ---------------------------------------------------------------------
        # PREDICT DEFAULT PROBABILITY
        # ---------------------------------------------------------------------

        default_prob = model.predict_proba(processed_input)[0][1]

        # ---------------------------------------------------------------------
        # DISPLAY PROBABILITY
        # ---------------------------------------------------------------------

        st.metric(
            label="Predicted Default Probability",
            value=f"{default_prob:.1%}",
            delta=(
                f"{default_prob - optimal_threshold:.1%} "
                f"vs Threshold ({optimal_threshold:.2f})"
            ),
            delta_color="inverse"
        )

        # ---------------------------------------------------------------------
        # DECISION BASED ON OPTIMAL FINANCIAL THRESHOLD
        # ---------------------------------------------------------------------

        if default_prob >= optimal_threshold:

            st.error(
                "❌ **DECISION: LOAN REJECTED (High Risk)**"
            )

            st.warning(
                f"Applicant risk ({default_prob:.1%}) exceeds "
                f"the cost-optimal threshold of "
                f"{optimal_threshold:.1%}."
            )

        else:

            st.success(
                "✅ **DECISION: LOAN APPROVED (Low Risk)**"
            )

            st.info(
                f"Applicant risk ({default_prob:.1%}) is below "
                f"the cost-optimal threshold of "
                f"{optimal_threshold:.1%}."
            )

    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )


# -----------------------------------------------------------------------------
# 7. DEBUGGING INFORMATION
# -----------------------------------------------------------------------------
    #
# This section can help verify that the input columns match the trained
# preprocessor. You can remove it later if you don't want it displayed.
#
# -----------------------------------------------------------------------------

with st.expander("🔍 View Model Input Data"):

    st.dataframe(raw_data)

    st.write(
        "**Input columns:**"
    )

    st.write(
        raw_data.columns.tolist()
    )
