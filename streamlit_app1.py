from pathlib import Path
from urllib.parse import quote_plus

import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError


# =========================================================
# 1. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MediVision AI | Quantum Care AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "sample_images"


# =========================================================
# 2. CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #f5f8fc;
}
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #12345a;
}
.subtitle {
    font-size: 19px;
    color: #287c91;
    font-weight: 600;
}
.section-card {
    background-color: #eaf3fa;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 12px;
}
.small-text {
    color: #53677c;
    font-size: 14px;
}
div.stButton > button {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. MEDICAL MODULE DATABASE
# =========================================================

MODULES = {

    "Diabetic Retinopathy": {
        "folder": "diabetic_retinopathy",
        "icon": "👁️",
        "image_type": "Retinal Fundus Photograph",
        "upload_label": "Upload a retinal fundus image",

        "description": """
Diabetic retinopathy is an eye condition associated with
diabetes. It occurs when high blood sugar damages the
small blood vessels in the retina.

The retina is the light-sensitive tissue at the back
of the eye that helps us see.
""",

        "risk_factors": [
            "Long-term diabetes",
            "High blood sugar levels",
            "High blood pressure",
            "High cholesterol",
            "Pregnancy in people with diabetes"
        ],

        "symptoms": [
            "Blurred vision",
            "Floaters or dark spots",
            "Difficulty seeing clearly",
            "Changes in vision",
            "Difficulty seeing at night"
        ],

        "care": [
            "Attend regular retinal examinations.",
            "Follow your prescribed diabetes care plan.",
            "Maintain recommended blood sugar management.",
            "Seek prompt medical attention for sudden vision changes."
        ],

        "health_description": (
            "Diabetes can affect the tiny blood vessels "
            "in the retina. Early stages may not cause "
            "noticeable symptoms."
        ),

        "tips": [
            "Attend regular eye examinations.",
            "Follow your clinician's advice.",
            "Maintain recommended diabetes care.",
            "Do not rely on home remedies."
        ],

        "fact": (
            "Regular retinal examinations can help identify "
            "diabetic eye changes early."
        ),

        "specialist": "retina specialist ophthalmologist",

        "learn_url": (
            "https://www.cdc.gov/diabetes/diabetes-complications/"
            "diabetes-and-vision-loss.html"
        )
    },


    "Tuberculosis (TB)": {
        "folder": "tuberculosis",
        "icon": "🫁",
        "image_type": "Chest X-ray",
        "upload_label": "Upload a chest X-ray image",

        "description": """
Tuberculosis is an infectious disease caused by bacteria
called Mycobacterium tuberculosis.

It most commonly affects the lungs, although it can
also affect other parts of the body.
""",

        "risk_factors": [
            "Close contact with someone with active TB",
            "Weakened immune system",
            "Certain chronic health conditions",
            "Living or working in crowded environments"
        ],

        "symptoms": [
            "Persistent cough",
            "Fever",
            "Night sweats",
            "Unexplained weight loss",
            "Chest discomfort",
            "Coughing up blood"
        ],

        "care": [
            "Seek medical evaluation for persistent symptoms.",
            "Follow the complete treatment prescribed by a doctor.",
            "Follow public-health guidance.",
            "Do not stop prescribed treatment without medical advice."
        ],

        "health_description": (
            "Tuberculosis is an infectious disease that "
            "commonly affects the lungs. It can be treated "
            "with appropriate medical care."
        ),

        "tips": [
            "Seek medical evaluation for a persistent cough.",
            "Complete prescribed TB treatment.",
            "Follow advice about preventing transmission.",
            "Do not substitute home remedies for treatment."
        ],

        "fact": (
            "Tuberculosis is preventable and curable "
            "with appropriate medical treatment."
        ),

        "specialist": "pulmonologist tuberculosis specialist",

        "learn_url": (
            "https://www.who.int/news-room/fact-sheets/"
            "detail/tuberculosis"
        )
    },


    "Oral Cancer": {
        "folder": "oral_cancer",
        "icon": "🦷",
        "image_type": "Oral Clinical Photograph",
        "upload_label": "Upload an oral clinical photograph",

        "description": """
Oral cancer develops in tissues of the mouth.
It can affect the lips, tongue, gums, inner cheeks
and other parts of the oral cavity.

Early professional assessment of persistent
unusual changes is important.
""",

        "risk_factors": [
            "Tobacco use",
            "Alcohol consumption",
            "Certain HPV infections",
            "Other individual health and environmental factors"
        ],

        "symptoms": [
            "Persistent mouth ulcers",
            "Unusual red or white patches",
            "A persistent lump in the mouth",
            "Difficulty swallowing",
            "Persistent mouth discomfort",
            "Changes in the mouth that do not heal"
        ],

        "care": [
            "Arrange an examination with a dentist or doctor.",
            "Avoid tobacco.",
            "Follow professional medical advice.",
            "Get persistent mouth changes examined."
        ],

        "health_description": (
            "Oral cancer can affect the lips, tongue, gums "
            "and other tissues inside the mouth. Persistent "
            "unusual changes should be examined by a professional."
        ),

        "tips": [
            "Maintain regular dental check-ups.",
            "Avoid tobacco.",
            "Get persistent mouth ulcers or unusual patches examined.",
            "Do not use home remedies as a substitute for examination."
        ],

        "fact": (
            "A trained healthcare professional can examine "
            "the mouth as part of an oral health assessment."
        ),

        "specialist": "oral medicine specialist oral surgeon",

        "learn_url": "https://cancerindia.org.in/oral-cancer/"
    }
}


# =========================================================
# 4. APPLICATION HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🏥 MediVision AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Medical Image Screening</div>',
    unsafe_allow_html=True
)

st.write(
    "Making medical image screening more accessible "
    "through responsible healthcare technology."
)

st.markdown(
    "**A Healthcare Innovation Initiative by Quantum Care AI**"
)

st.info(
    "MediVision AI is a research and educational prototype. "
    "Its current version provides image upload, technical "
    "image checks and health education. Validated disease "
    "prediction models are not yet connected."
)

st.divider()


# =========================================================
# 5. SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("🏥 MediVision AI")

st.sidebar.caption("QUANTUM CARE AI")

page = st.sidebar.radio(
    "Application Navigation",
    [
        "Home",
        "Medical Screening",
        "Health Education",
        "About Our Project",
        "Future Scope"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("""
### 🔬 Screening Categories

- 👁️ Diabetic Retinopathy
- 🫁 Tuberculosis
- 🦷 Oral Cancer
""")

st.sidebar.caption(
    "Responsible AI | Healthcare Innovation | Accessibility"
)


# =========================================================
# 6. HOME PAGE
# =========================================================

if page == "Home":

    st.header("Welcome to MediVision AI")

    st.write("""
    MediVision AI is a healthcare technology prototype
    developed by Quantum Care AI.

    The project explores how digital image handling,
    artificial intelligence research and accessible
    health education can be brought together in one platform.
    """)

    st.subheader("Our Three Medical Screening Categories")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 👁️")
        st.markdown("**Diabetic Retinopathy**")
        st.write("Retinal fundus image screening research.")

    with col2:
        st.markdown("### 🫁")
        st.markdown("**Tuberculosis**")
        st.write("Chest X-ray image screening research.")

    with col3:
        st.markdown("### 🦷")
        st.markdown("**Oral Cancer**")
        st.write("Oral clinical image screening research.")

    st.divider()

    st.header("🎯 Our Main Objectives")

    objectives = [
        "Explore responsible medical-image technology.",
        "Provide separate image upload modules.",
        "Promote awareness of important medical conditions.",
        "Make educational health information accessible.",
        "Explore future integration of validated AI models.",
        "Encourage professional medical consultation."
    ]

    for item in objectives:
        st.write("✓", item)

    st.divider()

    st.header("✨ Key Features")

    features = [
        ("Multiple Screening Modules",
         "Three separate medical-image categories."),

        ("Image Upload and Preview",
         "Upload and view images with technical information."),

        ("Educational Image Galleries",
         "Separate sample-image galleries for each category."),

        ("Smart Health Insights",
         "Category-specific educational information."),

        ("Hospital Finder",
         "Search for relevant hospitals and specialists."),

        ("Downloadable Reports",
         "Download a basic image review summary.")
    ]

    for title, description in features:
        with st.expander(title):
            st.write(description)

    st.success(
        "MediVision AI — Innovation with responsibility."
    )


# =========================================================
# 7. MEDICAL SCREENING PAGE
# =========================================================

elif page == "Medical Screening":

    st.header("🔬 Medical Image Screening")

    disease = st.selectbox(
        "Select your Medical Screening Category",
        list(MODULES.keys())
    )

    module = MODULES[disease]

    st.divider()

    st.header(f"{module['icon']} {disease}")

    st.write(module["description"])

    # -----------------------------------------------------
    # DISEASE INFORMATION
    # -----------------------------------------------------

    with st.expander("📚 Detailed Medical Information", expanded=True):

        st.markdown("**Risk Factors**")

        for item in module["risk_factors"]:
            st.write("•", item)

        st.markdown("**Possible Symptoms**")

        for item in module["symptoms"]:
            st.write("•", item)

        st.markdown("**Care and Prevention Guidance**")

        for item in module["care"]:
            st.write("•", item)

    # -----------------------------------------------------
    # SAMPLE IMAGE GALLERY
    # -----------------------------------------------------

    st.divider()

    st.subheader("🖼️ Category-Specific Sample Image Gallery")

    st.write(
        f"Educational images for {disease}."
    )

    selected_folder = IMAGE_DIR / module["folder"]

    if selected_folder.exists():

        sample_images = sorted([
            p for p in selected_folder.iterdir()
            if p.is_file()
            and p.suffix.lower() in [
                ".jpg", ".jpeg", ".png", ".webp"
            ]
        ])

        if sample_images:

            columns = st.columns(2)

            for index, image_path in enumerate(sample_images):

                with columns[index % 2]:

                    try:
                        sample = Image.open(image_path)

                        st.image(
                            sample,
                            caption=image_path.name,
                            use_container_width=True
                        )

                    except (OSError, UnidentifiedImageError):
                        st.warning(
                            f"Unable to display {image_path.name}"
                        )

        else:

            st.info(
                "No sample images added yet. "
                "Place suitable educational images inside "
                f"sample_images/{module['folder']}."
            )

    else:

        st.info(
            "Create the category-specific sample image folder "
            "to display educational examples."
        )

    st.caption(
        "Sample images are educational examples, not "
        "diagnostic reference standards."
    )

    # -----------------------------------------------------
    # SEPARATE IMAGE UPLOAD
    # -----------------------------------------------------

    st.divider()

    st.subheader("📤 Upload Your Medical Image")

    st.write(
        f"Required image type: **{module['image_type']}**"
    )

    uploaded_file = st.file_uploader(
        module["upload_label"],
        type=["jpg", "jpeg", "png"],
        key=f"upload_{module['folder']}"
    )

    if uploaded_file is not None:

        try:

            if uploaded_file.size > 15 * 1024 * 1024:

                st.error("Maximum upload size is 15 MB.")

                st.stop()

            original = Image.open(uploaded_file)

            image_format = original.format or "Unknown"

            original.load()

            image = ImageOps.exif_transpose(original)

            width, height = image.size

            if width < 32 or height < 32:

                st.error(
                    "Image resolution is too small. "
                    "Please select another image."
                )

                st.stop()

            if width * height > 40000000:

                st.error("Image dimensions are too large.")

                st.stop()

            st.success("Image uploaded successfully!")

            st.subheader("🖼️ Image Preview")

            st.image(
                image,
                caption=f"Uploaded image: {disease}",
                use_container_width=True
            )

            st.divider()

            st.subheader("📋 Image Review Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Selected Category**")
                st.write(disease)

                st.write("**Image Dimensions**")
                st.write(f"{width} × {height}")

            with col2:
                st.write("**Image Format**")
                st.write(image_format)

                st.write("**File Size**")
                st.write(
                    f"{uploaded_file.size / 1024:.2f} KB"
                )

            st.warning(
                "AI model integration is pending. "
                "Only basic technical image checks have been "
                "performed. No disease prediction or medical "
                "interpretation has been generated."
            )

            # -------------------------------------------------
            # SMART HEALTH INSIGHTS
            # -------------------------------------------------

            st.divider()

            st.header("💡 Smart Health Insights")

            st.caption(
                "Educational information based on your selected "
                "category, not an analysis of your uploaded image."
            )

            st.info(module["health_description"])

            st.subheader("🏡 Helpful Health Tips")

            for tip in module["tips"]:
                st.write("✓", tip)

            st.subheader("🌟 Did You Know?")

            st.success(module["fact"])

            st.markdown(
                f"[📖 Learn more about {disease}]"
                f"({module['learn_url']})"
            )

            # -------------------------------------------------
            # HOSPITAL FINDER
            # -------------------------------------------------

            st.divider()

            st.subheader("🏥 Find a Relevant Hospital")

            st.write(
                "Search for hospitals and specialists "
                "related to your selected category."
            )

            city = st.text_input(
                "Enter your city",
                value="Bengaluru",
                key=f"city_{module['folder']}"
            )

            if city.strip():

                query = (
                    f"{module['specialist']} hospitals "
                    f"in {city.strip()}"
                )

                hospital_url = (
                    "https://www.google.com/maps/search/"
                    + quote_plus(query)
                )

                st.link_button(
                    "📍 Find Relevant Hospitals",
                    hospital_url
                )

            else:
                st.info("Please enter a city.")

            st.caption(
                "Search results are not endorsements. "
                "Check hospital services and specialist credentials."
            )

            # -------------------------------------------------
            # DOWNLOADABLE REPORT
            # -------------------------------------------------

            st.divider()

            st.subheader("📄 Download Screening Report")

            report = f"""
=================================================
              MEDIVISION AI
              QUANTUM CARE AI
=================================================

              IMAGE REVIEW REPORT

SCREENING INFORMATION
-------------------------------------------------

Screening Category: {disease}

Image Name: {uploaded_file.name}

Image Format: {image_format}

Image Dimensions: {width} x {height}

Image Size: {uploaded_file.size / 1024:.2f} KB

Upload Status: Successful

Technical Image Checks: Passed

AI Model Status: Not connected

EDUCATIONAL INFORMATION
-------------------------------------------------

{module['description']}

RISK FACTORS
-------------------------------------------------

{"".join("- " + x + chr(10) for x in module['risk_factors'])}

POSSIBLE SYMPTOMS
-------------------------------------------------

{"".join("- " + x + chr(10) for x in module['symptoms'])}

CARE GUIDANCE
-------------------------------------------------

{"".join("- " + x + chr(10) for x in module['care'])}

MEDICAL DISCLAIMER
-------------------------------------------------

This report is for educational purposes only.

No AI-based disease prediction or medical diagnosis
has been generated.

Technical image validation does not establish
medical image quality or disease status.

Please consult a qualified healthcare professional
for proper medical assessment.

=================================================
MediVision AI | Quantum Care AI
Innovation with Responsibility
=================================================
"""

            st.download_button(
                "⬇️ Download Screening Report",
                data=report,
                file_name="MediVision_AI_Report.txt",
                mime="text/plain",
                use_container_width=True
            )

        except (OSError, UnidentifiedImageError, ValueError):

            st.error(
                "Unable to process the uploaded image. "
                "Please select a valid JPG, JPEG or PNG file."
            )

        except Exception as error:

            st.error(f"Image processing error: {error}")


# =========================================================
# 8. HEALTH EDUCATION PAGE
# =========================================================

elif page == "Health Education":

    st.header("📚 General Health Education")

    st.write("""
    Health awareness and early professional assessment
    play important roles in managing medical conditions.

    Explore the following educational information.
    """)

    for disease_name, data in MODULES.items():

        with st.expander(
            f"{data['icon']} {disease_name}"
        ):

            st.markdown("**Overview**")

            st.write(data["description"])

            st.markdown("**Risk Factors**")

            for item in data["risk_factors"]:
                st.write("•", item)

            st.markdown("**Possible Symptoms**")

            for item in data["symptoms"]:
                st.write("•", item)

            st.markdown("**Care Guidance**")

            for item in data["care"]:
                st.write("•", item)

            st.markdown(
                f"[Learn more]({data['learn_url']})"
            )

    st.divider()

    st.info(
        "Educational health information cannot replace "
        "professional medical assessment."
    )


# =========================================================
# 9. ABOUT OUR PROJECT
# =========================================================

elif page == "About Our Project":

    st.header("🌐 About Quantum Care AI")

    st.subheader("Our Project: MediVision AI")

    st.write("""
    MediVision AI is a healthcare innovation prototype
    developed by Quantum Care AI.

    It explores the application of digital technology
    in medical-image education and responsible
    healthcare innovation.

    The platform brings three medical-image categories
    together through separate modules, image uploading,
    educational galleries and health information.
    """)

    st.divider()

    st.header("🎯 Project Objectives")

    objectives = [
        "Explore the role of technology in healthcare.",
        "Provide a unified platform for three screening categories.",
        "Organise medical image uploads by category.",
        "Improve accessibility to health education.",
        "Encourage awareness and professional consultation.",
        "Explore future integration of validated AI models."
    ]

    for item in objectives:
        st.write("✓", item)

    st.divider()

    st.header("💡 Our Innovation")

    st.markdown("""
    **1. Multi-Category Platform**

    Three separate medical-image modules within one application.

    **2. Category-Specific Image Handling**

    Separate galleries and upload sections for retinal,
    chest X-ray and oral clinical photographs.

    **3. Educational Health Insights**

    Health information is presented according to the
    selected medical category.

    **4. Accessible User Experience**

    A simple interface designed for convenient navigation.

    **5. Future AI Integration**

    The architecture can be extended with independently
    trained, evaluated and clinically validated models.
    """)

    st.divider()

    st.header("🛠️ Technology Stack")

    technologies = [
        ("Python", "Main programming language."),
        ("Streamlit", "Interactive web application framework."),
        ("Pillow", "Image loading and basic processing."),
        ("Pathlib", "File and folder management."),
        ("GitHub", "Source code management."),
        ("Streamlit Community Cloud", "Application deployment.")
    ]

    for technology, explanation in technologies:

        with st.expander(technology):
            st.write(explanation)

    st.caption(
        "Machine learning and deep learning are planned "
        "extensions; validated disease prediction is not "
        "currently implemented."
    )

    st.divider()

    st.header("👥 Team Identity")

    st.markdown("""
    **Team Name:** Quantum Care AI

    **Project Name:** MediVision AI

    **Domain:** Healthcare and Artificial Intelligence

    **Mission:** Exploring responsible technology
    for accessible healthcare innovation.
    """)

    st.success(
        "Quantum Care AI — Innovation with Responsibility."
    )


# =========================================================
# 10. FUTURE SCOPE
# =========================================================

elif page == "Future Scope":

    st.header("🚀 Future Scope and Development")

    st.write("""
    MediVision AI is designed as an expandable research
    prototype. Future development can introduce additional
    image-processing and machine-learning capabilities.
    """)

    future_features = [
        (
            "Validated AI Model Integration",
            "Integrate independently trained and evaluated "
            "models for the three medical-image categories."
        ),
        (
            "Advanced Image Processing",
            "Explore image quality assessment and preprocessing "
            "appropriate to each image type."
        ),
        (
            "Model Explainability",
            "Explore methods that help researchers understand "
            "which image regions influence model outputs."
        ),
        (
            "Expanded Medical Datasets",
            "Use appropriately licensed, representative datasets "
            "with reliable annotations."
        ),
        (
            "Professional Medical Validation",
            "Work with qualified healthcare professionals "
            "to evaluate safety and performance."
        ),
        (
            "Improved Accessibility",
            "Continue improving the interface for mobile "
            "and desktop users."
        ),
        (
            "Privacy and Security",
            "Develop secure image handling, appropriate "
            "consent and data protection practices."
        )
    ]

    for title, description in future_features:

        with st.expander(title):
            st.write(description)

    st.divider()

    st.header("⚕️ Limitations and Responsible AI")

    st.markdown("""
    - The current application does not diagnose diseases.
    - It does not contain validated disease classification models.
    - Basic image checks do not establish medical suitability.
    - Sample images are for education only.
    - Medical image interpretation requires appropriate
      clinical expertise.
    - Future models require independent testing and
      professional evaluation before clinical use.
    """)

    st.warning(
        "MediVision AI is not a substitute for a doctor, "
        "radiologist, ophthalmologist or dentist."
    )

    st.divider()

    st.header("🌟 Our Vision")

    st.write("""
    Our vision is to explore responsible, accessible
    and user-friendly healthcare technology.

    Through research, innovation and collaboration,
    Quantum Care AI aims to contribute to the exploration
    of technology-assisted health awareness.
    """)


# =========================================================
# 11. GLOBAL FOOTER
# =========================================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:15px;">

<h3 style="color:#12345a;">🏥 MediVision AI</h3>

<p><b>A Quantum Care AI Initiative</b></p>

<p>Innovation with Responsibility</p>

<p style="font-size:12px; color:#607080;">
Healthcare | Artificial Intelligence | Innovation
</p>

</div>
""", unsafe_allow_html=True)

st.caption(
    "Research and educational prototype only. "
    "Not intended for medical diagnosis or treatment decisions."
)