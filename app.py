from urllib.parse import quote_plus

import streamlit as st
from PIL import Image
from preprocessing import check_retinal_image


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="MediVision AI",
    page_icon="🏥",
    layout="wide"
)


# --------------------------------------------------
# APPLICATION HEADER
# --------------------------------------------------

st.title("🏥 MediVision AI")
st.subheader("AI-Powered Medical Image Screening")

st.write(
    "Making medical image screening more accessible "
    "through responsible technology."
)

st.warning(
    "Research prototype only. This application "
    "does not provide a medical diagnosis."
)


# --------------------------------------------------
# DISEASE SELECTION
# --------------------------------------------------

disease = st.sidebar.selectbox(
    "Choose Screening Module",
    [
        "Diabetic Retinopathy",
        "Tuberculosis (TB)",
        "Oral Cancer"
    ]
)


# --------------------------------------------------
# MODULE INFORMATION
# --------------------------------------------------

if disease == "Diabetic Retinopathy":

    st.header("👁️ Diabetic Retinopathy Screening")
    st.write("Upload a retinal fundus photograph.")

    with st.expander(
        "📚 About Diabetic Retinopathy",
        expanded=True
    ):
        st.markdown("""
        **What is it?**

        Diabetic retinopathy is an eye condition caused by
        damage to retinal blood vessels due to diabetes.

        **Risk factors:**
        - Long-term diabetes
        - High blood sugar
        - High blood pressure
        - High cholesterol

        **Possible symptoms:**
        - Blurred vision
        - Floaters or dark spots
        - Difficulty seeing clearly

        **Prevention and care:**
        - Regular eye examinations
        - Blood sugar management
        - Following medical advice

        Regular retinal examinations can help detect
        changes early.
        """)

    symptoms = [
        "Blurred vision",
        "Floaters or dark spots",
        "Difficulty seeing clearly"
    ]

    care = [
        "Arrange an eye examination.",
        "Follow your clinician's advice.",
        "Maintain recommended diabetes care."
    ]

    specialist = "retina specialist ophthalmologist"

    learn_url = (
        "https://www.cdc.gov/diabetes/diabetes-complications/"
        "diabetes-and-vision-loss.html"
    )

    health_description = (
        "Diabetes can affect the tiny blood vessels in "
        "the retina. Early stages may not cause noticeable "
        "symptoms. Regular eye examinations are important."
    )

    health_tips = [
        "Follow your prescribed diabetes care plan.",
        "Attend regular eye examinations.",
        "Do not rely on home remedies to treat eye disease.",
        "Seek prompt medical care for sudden vision changes."
    ]

    health_fact = (
        "Regular eye examinations can help identify "
        "diabetic eye changes early."
    )

    learn_label = "📖 Click here to learn about Diabetic Retinopathy"


elif disease == "Tuberculosis (TB)":

    st.header("🫁 Tuberculosis Screening")
    st.write("Upload a chest X-ray image.")

    with st.expander("📚 About Tuberculosis", expanded=True):

        st.markdown("""
        **What is Tuberculosis?**

        Tuberculosis is an infectious disease caused by
        bacteria called Mycobacterium tuberculosis.
        It commonly affects the lungs.

        **Possible symptoms:**
        - Persistent cough
        - Fever
        - Night sweats
        - Weight loss
        - Chest discomfort

        **Risk factors:**
        - Close contact with someone who has active TB
        - Conditions that weaken the immune system

        **Prevention and care:**
        - Seek medical evaluation.
        - Follow prescribed treatment.
        - Follow public-health guidance.
        """)

    symptoms = [
        "Persistent cough",
        "Fever",
        "Night sweats",
        "Unexplained weight loss"
    ]

    care = [
        "Seek medical evaluation for persistent symptoms.",
        "Follow the complete treatment prescribed by a doctor.",
        "Follow public-health guidance to reduce transmission."
    ]

    specialist = "pulmonologist tuberculosis specialist"

    learn_url = (
        "https://www.who.int/news-room/fact-sheets/"
        "detail/tuberculosis"
    )

    health_description = (
        "Tuberculosis is an infectious disease caused by "
        "bacteria. It most commonly affects the lungs and "
        "can be treated with appropriate medical care."
    )

    health_tips = [
        "Seek medical evaluation for a persistent cough.",
        "Follow the complete treatment prescribed by a doctor.",
        "Do not use home remedies instead of TB treatment.",
        "Follow medical advice about preventing transmission."
    ]

    health_fact = (
        "Tuberculosis is preventable and curable with "
        "appropriate medical treatment."
    )

    learn_label = "📖 Click here to learn about Tuberculosis"


else:

    st.header("🦷 Oral Cancer Screening")
    st.write("Upload an oral photograph.")

    with st.expander("📚 About Oral Cancer", expanded=True):

        st.markdown("""
        **What is Oral Cancer?**

        Oral cancer develops in tissues of the mouth,
        including the tongue, lips, gums and inner cheeks.

        **Risk factors:**
        - Tobacco use
        - Alcohol consumption
        - Certain HPV infections

        **Possible warning signs:**
        - Persistent mouth ulcers
        - Red or white patches
        - A lump in the mouth
        - Difficulty swallowing

        **Prevention and care:**
        - Avoid tobacco.
        - Maintain good oral hygiene.
        - Consult a dentist about persistent changes.
        """)

    symptoms = [
        "Persistent mouth ulcer",
        "Unusual red or white patch",
        "Persistent lump in the mouth"
    ]

    care = [
        "Arrange an examination with a dentist or doctor.",
        "Avoid tobacco.",
        "Follow professional medical advice."
    ]

    specialist = "oral cancer specialist oral surgeon"

    learn_url = (
        "https://cancerindia.org.in/oral-cancer/"
    )

    health_description = (
        "Oral cancer can affect the lips, tongue, gums "
        "and other tissues inside the mouth. Persistent "
        "unusual changes should be examined by a professional."
    )

    health_tips = [
        "Maintain regular dental check-ups.",
        "Avoid tobacco.",
        "Get persistent mouth ulcers or unusual patches examined.",
        "Do not use home remedies as a substitute for examination."
    ]

    health_fact = (
        "A trained healthcare professional can examine "
        "the mouth as part of an oral health assessment."
    )

    learn_label = "📖 Click here to learn about Oral Cancer"


# --------------------------------------------------
# MEDICAL GUIDELINES
# --------------------------------------------------

st.divider()

st.subheader("⚕️ Medical Screening Guidelines")

st.info("""
MediVision AI is an educational medical-image screening prototype.

- Uploaded images receive basic technical checks.
- The application does not currently provide AI-based disease predictions.
- Image review cannot confirm or exclude a disease.
- Consult a qualified healthcare professional for diagnosis.
""")


# --------------------------------------------------
# QUANTUM CARE AI BRANDING
# --------------------------------------------------

st.markdown("---")

st.markdown("""
### 🌐 About Quantum Care AI

Our mission is to explore responsible AI technology
for accessible healthcare innovation.

**Project:** MediVision AI

**Team:** Quantum Care AI

**Domain:** Healthcare and Artificial Intelligence
""")


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

st.divider()

st.subheader("📤 Upload Medical Image")

uploaded_file = st.file_uploader(
    "Choose your medical image",
    type=["jpg", "jpeg", "png"],
    help="Upload a JPG, JPEG or PNG image."
)


if uploaded_file is not None:

    try:

        # Open uploaded image
        image = Image.open(uploaded_file)

        image.load()

        # Store original image information
        image_format = image.format or "Unknown"
        image_width = image.width
        image_height = image.height
        image_size = uploaded_file.size

        # Basic image checks
        is_valid, message = check_retinal_image(image)

        if not is_valid:
            st.error(message)
            st.stop()

        st.success("Image uploaded successfully!")

        # Image preview
        st.subheader("🖼️ Your Image Preview")

        st.image(
            image,
            caption="Uploaded Medical Image",
            width=500
        )

        # Image review summary
        st.divider()

        st.subheader("📋 Image Review Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Selected Module:**", disease)

            st.write(
                "**Image Dimensions:**",
                f"{image_width} x {image_height}"
            )

        with col2:

            st.write("**Image Format:**", image_format)

            st.write(
                "**File Size:**",
                f"{image_size / 1024:.2f} KB"
            )

        st.warning(
            "AI model integration is pending. "
            "No medical diagnosis or disease prediction "
            "has been generated."
        )

        # --------------------------------------------------
        # SMART HEALTH INSIGHTS
        # --------------------------------------------------

        st.divider()

        st.header("💡 Smart Health Insights")

        st.caption(
            "Educational information based on your selected "
            "screening module. This is not an interpretation "
            "of the uploaded image."
        )

        st.subheader("🔍 Learn About Your Selected Module")

        st.info(health_description)

        st.markdown(
            f"[{learn_label}]({learn_url})"
        )

        # Care tips
        st.subheader("🏡 Helpful Care and Safety Tips")

        for tip in health_tips:
            st.write("•", tip)

        # Interesting fact
        st.subheader("🌟 Did You Know?")

        st.success(health_fact)

        # Hospital finder
        st.divider()

        st.subheader("🏥 Find a Relevant Hospital")

        st.write(
            "Search for hospitals and specialists "
            "related to your selected screening module."
        )

        city = st.text_input(
            "Enter your city",
            value="Bengaluru",
            key="hospital_city"
        )

        if city.strip():

            search_query = (
                f"{specialist} hospitals in {city.strip()}"
            )

            hospital_url = (
                "https://www.google.com/maps/search/"
                + quote_plus(search_query)
            )

            st.markdown(
                f"[📍 Click here to find relevant hospitals]({hospital_url})"
            )

        else:

            st.info("Please enter a city to search for hospitals.")

        st.caption(
            "Search results are not endorsements. "
            "Check hospital services and specialist credentials "
            "before choosing a provider."
        )

        # --------------------------------------------------
        # DOWNLOAD REPORT
        # --------------------------------------------------

        st.divider()

        st.subheader("📄 Download Screening Report")

        report = f"""
MEDIVISION AI - QUANTUM CARE AI

IMAGE REVIEW SUMMARY

Screening Module: {disease}

Image Name: {uploaded_file.name}

Image Format: {image_format}

Image Dimensions: {image_width} x {image_height}

File Size: {image_size / 1024:.2f} KB

Image Status: Uploaded successfully.

AI Analysis: Not yet connected.

Educational Information:
{health_description}

Important:
This report is not a medical diagnosis.
The uploaded image has not received AI-based
disease classification.
Please consult a qualified healthcare professional.
"""

        st.download_button(
            label="⬇️ Download Screening Report",
            data=report,
            file_name="MediVision_AI_Report.txt",
            mime="text/plain"
        )

    except Exception as e:

        st.error(f"Image processing error: {e}")

        st.info(
            "Please check the uploaded image format "
            "and try another image."
        )


# --------------------------------------------------
# EDUCATIONAL INFORMATION
# --------------------------------------------------

st.divider()

st.header("📚 General Health Education")

st.subheader("Common Symptoms")

for symptom in symptoms:
    st.write("•", symptom)

st.subheader("General Care Guidance")

for advice in care:
    st.write("•", advice)

st.caption(
    "Symptoms and care information are educational. "
    "An image alone cannot establish a diagnosis."
)


# --------------------------------------------------
# WHY OUR APP IS USEFUL
# --------------------------------------------------

st.divider()

st.header("🚀 Why Is MediVision AI Useful?")

st.markdown("""
MediVision AI is a healthcare technology prototype
developed by Quantum Care AI to explore how digital
tools can make medical-image education more accessible.

### Our Key Benefits

**1. Multiple Screening Modules**

The application brings educational information about
Diabetic Retinopathy, Tuberculosis and Oral Cancer
together in one platform.

**2. Easy Image Upload**

Users can upload medical images and view their
previews and basic image information.

**3. Health Awareness**

Each module provides educational descriptions,
possible symptoms, risk factors and care guidance.

**4. Reliable Learning Resources**

Clickable educational links help users explore
more information from established health organisations.

**5. Hospital Discovery**

The hospital finder helps users search for relevant
hospitals and specialists in their city.

**6. Downloadable Reports**

Users can download a simple report containing
their uploaded image details and selected module.

### Our Vision

We aim to explore responsible, accessible and
user-friendly healthcare technology.

Our goal is to support health awareness and
encourage people to seek appropriate professional care.
""")

st.success(
    "MediVision AI — Innovation with responsibility. "
    "A Quantum Care AI initiative."
)

st.caption(
    "This is an educational prototype, not a medical "
    "diagnostic system or a substitute for professional care."
)