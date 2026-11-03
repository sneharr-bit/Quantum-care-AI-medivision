from urllib.parse import quote_plus
import streamlit as st
from PIL import Image
from preprocessing import check_retinal_image

st.set_page_config(
    page_title="MediVision AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 MediVision AI")
st.subheader("AI-Powered Medical Image Screening")

st.write(
    "Making medical image screening more accessible."
)

st.warning(
    "Research prototype only. This application "
    "does not provide a medical diagnosis."
)

# Select disease
disease = st.sidebar.selectbox(
    "Choose Screening Module",
    [
        "Diabetic Retinopathy",
        "Tuberculosis (TB)",
        "Oral Cancer"
    ]
)

# Module information
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

        **Screening importance:**
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

elif disease == "Tuberculosis (TB)":
    st.header("🫁 Tuberculosis Screening")
    st.write("Upload a chest X-ray image.")

    st.subheader("📚 About Tuberculosis (TB)")

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
    - Seek medical evaluation for persistent symptoms.
    - Follow the complete treatment prescribed by a doctor.
    - Follow public-health guidance to reduce transmission.

    **Screening importance:**
    Medical evaluation and appropriate tests help
    identify tuberculosis.
    """)

    symptoms = [
        "Persistent cough",
        "Fever",
        "Night sweats",
        "Unexplained weight loss"
    ]

    care = [
        "Seek medical evaluation.",
        "Follow prescribed treatment if diagnosed.",
        "Follow public health guidance."
    ]

else:
    st.header("🦷 Oral Cancer Screening")
    st.write("Upload an oral photograph.")

    st.subheader("📚 About Oral Cancer")

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

# Medical screening disclaimer
st.divider()

st.subheader("⚕️ Medical Screening Guidelines")

st.info("""
MediVision AI is an educational medical-image screening prototype.

- Uploaded images receive basic technical checks.
- The application does not currently provide AI-based disease predictions.
- Image review cannot confirm or exclude a disease.
- Consult a qualified healthcare professional for diagnosis.
""")

st.markdown("---")

st.markdown("""
### 🌐 About Quantum Care AI

Our mission is to explore responsible AI technology
for accessible healthcare innovation.

**Project:** MediVision AI  
**Team:** Quantum Care AI  
**Domain:** Healthcare and Artificial Intelligence
""")

# Image upload
st.subheader("Upload Medical Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        image.load()

        is_valid, message = check_retinal_image(image)

        if is_valid:
            st.success(message)
        else:
            st.error(message)
            st.stop()

        st.success("Image uploaded successfully!")

        st.subheader("Your Image Preview")

        st.image(
            image,
            caption="Uploaded Medical Image",
            width=500
        )
        # SMART HEALTH INSIGHTS
st.divider()
st.header("💡 Smart Health Insights")

st.caption(
    "Educational information based on your selected "
    "screening module, not an interpretation of the image."
)

if disease == "Diabetic Retinopathy":

    st.subheader("👁️ Learn About Diabetic Retinopathy")

    st.info(
        "Diabetes can affect the tiny blood vessels in "
        "the retina. Early stages may have no noticeable symptoms."
    )

    st.markdown(
        "[📖 Click here to know more about this condition]"
        "(https://www.cdc.gov/diabetes/diabetes-complications/"
        "diabetes-and-vision-loss.html)"
    )

    st.subheader("🏡 Helpful Care Tips")
    st.write("- Follow your prescribed diabetes care plan.")
    st.write("- Attend regular eye examinations.")
    st.write("- Do not rely on home remedies to treat eye disease.")

    st.success(
        "Did you know? Regular eye examinations can help "
        "identify diabetic eye changes early."
    )

    specialist = "retina specialist ophthalmologist"

elif disease == "Tuberculosis (TB)":

    st.subheader("🫁 Learn About Tuberculosis")

    st.info(
        "TB is an infectious disease caused by bacteria. "
        "It most commonly affects the lungs and is treatable "
        "with appropriate medical care."
    )

    st.markdown(
        "[📖 Click here to know more about TB]"
        "(https://www.who.int/news-room/fact-sheets/detail/tuberculosis)"
    )

    st.subheader("🏡 Helpful Care Tips")
    st.write("- Seek medical evaluation for a persistent cough.")
    st.write("- Follow the complete treatment prescribed by a doctor.")
    st.write("- Do not try home remedies instead of TB treatment.")
    st.write("- Follow medical advice about preventing transmission.")

    st.success(
        "Did you know? TB is preventable and curable with "
        "appropriate medical treatment."
    )

    specialist = "pulmonologist tuberculosis specialist"

else:

    st.subheader("🦷 Learn About Oral Cancer")

    st.info(
        "Oral cancer can affect the lips, tongue, gums "
        "and other tissues inside the mouth."
    )

    st.markdown(
        "[📖 Click here to know more about oral cancer]"
        "(https://cancerindia.org.in/oral-cancer/)"
    )

    st.subheader("🏡 Helpful Care Tips")
    st.write("- Maintain regular dental check-ups.")
    st.write("- Avoid tobacco.")
    st.write("- Get persistent mouth ulcers or unusual patches examined.")
    st.write("- Do not use home remedies as a substitute for examination.")

    st.success(
        "Did you know? The mouth can be examined by a trained "
        "health professional as part of oral cancer screening."
    )

    specialist = "oral cancer specialist oral surgeon"

# HOSPITAL FINDER
st.divider()
st.subheader("🏥 Find a Relevant Hospital")

city = st.text_input(
    "Enter your city",
    value="Bengaluru",
    key="hospital_city"
)

if city.strip():
    search_query = f"{specialist} hospitals in {city.strip()}"

    hospital_url = (
        "https://www.google.com/maps/search/"
        + quote_plus(search_query)
    )

    st.link_button(
        "📍 Click here to find hospitals",
        hospital_url
    )

st.caption(
    "Hospital search results are not endorsements. "
    "Check the hospital's services and credentials before visiting."
)

        # Image review summary
        st.subheader("Image Review Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Selected Module:", disease)
            st.write(
                "Image Dimensions:",
                f"{image.width} x {image.height}"
            )

        with col2:
            st.write("Image Format:", image.format)
            st.write(
                "File Size:",
                f"{uploaded_file.size / 1024:.2f} KB"
            )

        st.warning(
            "AI model integration is pending. "
            "No medical diagnosis or disease prediction "
            "has been generated."
        )

        report = f"""
MEDIVISION AI - QUANTUM CARE AI

IMAGE REVIEW SUMMARY

Screening Module: {disease}
Image Name: {uploaded_file.name}
Image Format: {image.format}
Image Dimensions: {image.width} x {image.height}
File Size: {uploaded_file.size / 1024:.2f} KB

Status: Image uploaded and previewed successfully.

AI Analysis: Not yet connected.
This report is not a medical diagnosis.
"""

        st.download_button(
            label="Download Screening Report",
            data=report,
            file_name="MediVision_AI_Report.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Image preview error: {e}")
        st.info(
            "Image received. Disease-specific AI model "
            "integration is still pending. No disease "
            "prediction has been made."
        )

# Educational information
st.divider()

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