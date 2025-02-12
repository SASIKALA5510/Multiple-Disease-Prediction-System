import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image

# # Set Page Configurations
# st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")



# def set_bg_local(image_path):
#     with open(image_path, "rb") as img_file:
#         encoded = base64.b64encode(img_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{encoded}");
#             background-size: cover;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_bg_local("C:/Users/sasik/OneDrive/Desktop/pro3 images\heart.jpg")  # Change to your local image file

# Main Content
# st.title("🩺 MULTIPLE DISEASE PREDICTION SYSTEM")
# st.write("This web application helps users predict the likelihood of developing diseases using ML models.")
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom, #f0f8ff, #ffffff);
        }
    </style>
    """,
    unsafe_allow_html=True
)


kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
liver_model = pickle.load(open('liver_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Home','Kidney Prediction',
                            'Liver Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom right,rgb(15, 198, 214),rgb(59, 150, 114));
    }
    </style>
    """,
    unsafe_allow_html=True
)


    
if selected == "Home":
    #st.image("C:/Users/sasik/OneDrive/Desktop/pro3 images/kidney.webp", use_container_width=True)  # Add your banner image
    #st.image("C:/Users/sasik/OneDrive/Desktop/pro3 images/kidney2.png", use_column_width=True)
    import streamlit as st
    import base64

    # Function to convert image to Base64
    def get_base64_encoded_image(image_path):
        with open(image_path, "rb") as img_file:
            base64_str = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:image/jpeg;base64,{base64_str}"

    # Replace this with your local image path
    image_path = "C:/Users/sasik/OneDrive/Pictures/Screenshots/Screenshot 2025-02-12 191601.png" # Update this path

    # Get Base64 string
    base64_image = get_base64_encoded_image(image_path)

    # Inject custom CSS
    st.markdown(
        f"""
        <style>
        .custom-title {{
            font-size: 50px;
            color: white;
            text-align: center;
            text-shadow: 2px 2px 4px black;
            padding: 40px;
            border-radius: 10px;
            background-image: url('{base64_image}');
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title
    st.markdown("<h1 class='custom-title'>🩺 MULTIPLE DISEASE PREDICTION SYSTEM</h1>", unsafe_allow_html=True)

    st.write(
        """
        This Web Application is designed to help users predict the likelihood of developing certain diseases based on their input features.
        With the use of trained and tested machine learning models, we provide predictions for **Chronic Kidney Disease, Liver Disease, and Parkinsons Disease**.
        """
    )
    # Function to resize images to a consistent size
    def resize_image(image_path, size=(400, 400)):
        img = Image.open(image_path)
        img = img.resize(size)  # Resize to uniform dimensions
        return img

    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(resize_image("C:/Users/sasik/OneDrive/Desktop/pro3 images/kidney.webp"), width=200)
        st.markdown("<p style='text-align: center; font-size:16px; font-weight:normal; margin-left: -40px;'>Kidney Disease Prediction</p>",unsafe_allow_html=True)

    with col2:
        st.image(resize_image("C:/Users/sasik/Downloads/freepik__upload__86233.png"),width=200)
        st.markdown("<p style='text-align: center; font-size:16px; font-weight:normal; margin-left: -40px;'>Liver Disease Prediction</p>", unsafe_allow_html=True)

    with col3:
        
        st.image(resize_image("C:/Users/sasik/Downloads/freepik__upload__92510.png"), width=200)
        st.markdown("<p style='text-align: center; font-size:16px; font-weight:normal; margin-left: -40px;'>Parkinsons Prediction</p>", unsafe_allow_html=True)


    # Instructions
    st.markdown("### **How to Use:**")
    st.write("""
    - Navigate to the **Main Menu** located in the sidebar.
    - Click on the desired tab (**Kidney Prediction**, **Liver Prediction**, or **Parkinsons Prediction**) to access the prediction tools.
    - Enter your details and click the prediction button.
    """)
    
if selected == "Kidney Prediction":
  
# Create side-by-side tabs
   tab1, tab2 = st.tabs([ "🩸 Kidney Disease Diagnosis","📄 About Kidney Disease",])

   with tab2:
    
        st.title("Chronic Kidney Disease ")
        
        st.markdown("""
        
        Kidney disease, also known as renal disease, occurs when the kidneys are damaged and cannot filter blood effectively. 
        This can lead to waste buildup, fluid imbalance, and other health issues. Common causes include diabetes, high blood pressure, and infections.
        """)

         # Add an image for kidney disease symptoms
        st.image("C:/Users/sasik/OneDrive/Desktop/pro3 images/CKD-01.png", caption="Common Symptoms of Kidney Disease", use_container_width=True)
        
        st.header("Prevention & Management:")
        st.markdown("""
   
   - Maintain a healthy diet, reduce salt intake.
   - Control blood sugar levels and blood pressure.
   - Stay hydrated and engage in regular exercise.
   - Avoid excessive use of painkillers and smoking.
   """)
   


   with tab1:
        
        st.title("Kidney Disease Prediction")

       
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            age = st.text_input('Age')

        with col2:
            bp = st.text_input('Blood Pressure')

        with col3:
            al = st.text_input('Albumin')

        with col4:
            su = st.text_input('Sugar')

        with col5:
            rbc = st.text_input('Red Blood Cells')

        with col1:
            pc = st.text_input('Pus Cell')

        with col2:
            pcc = st.text_input('Pus Cell Clumps')

        with col3:
            ba = st.text_input('Bacteria')

        with col4:
                bgr = st.text_input('Blood Glucose ')

        with col5:
            bu = st.text_input('Blood Urea')

        with col1:
                sc = st.text_input('Serum Creatinine')
                
        with col2:
            pot = st.text_input('Potassium')  

        with col3:
            wc = st.text_input('WBC Count')

        with col4:
            htn = st.text_input('Hypertension')

        with col5:
            dm = st.text_input('Diabetes Mellitus')

        with col1:
            cad = st.text_input('CAD')

        with col2:
            pe = st.text_input('Pedal Edema')

        with col3:
            ane = st.text_input('Anemia')

        kidney_diagnosis = ''

        if st.button("Kidney Test Result"):
            user_input = [age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot,
                            wc, htn, dm, cad, pe, ane]
            
            user_input = [float(x) for x in user_input]

            Kidney_Prediction = kidney_model.predict([user_input])

            if Kidney_Prediction[0] == 1:
                    kidney_diagnosis = "The person has kidney disease. It is advised to seek medical consultation for further evaluation and treatment."
            else:
                    kidney_diagnosis = "The person does not have kidney disease. However, maintaining a healthy lifestyle is recommended."

        st.success(kidney_diagnosis)
   


if selected == "Liver Prediction":


    # Create side-by-side tabs
    tab1, tab2 = st.tabs([ "🩸 Liver Disease Diagnosis","📄 About Liver Disease",])

    with tab1:
 
            st.title('Liver Disease Prediction')

            col1,col2,col3 = st.columns(3)

            with col1:
                age = st.text_input('age')

            with col2:
                Total_Bilirubin = st.text_input('Total_Bilirubin')

            with col3:
                Direct_Bilirubin = st.text_input('Direct_Bilirubin')

            with col1:
                Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

            with col2:
                Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

            with col3:
                Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')

            with col1:
                Total_Protiens = st.text_input('Total_Protiens')

            with col2:
                Albumin = st.text_input('Albumin')

            with col3:
                Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')

            with col1:
                Gender_Male = st.text_input('Gender_Male')

            liver_diagnosis = ''

            if st.button("Liver Test Result"):

                user_input = [age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                                Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio,Gender_Male]
                
                user_input = [float(x) for x in user_input]

                liver_Prediction = liver_model.predict([user_input])

                if liver_Prediction[0] == 1:

                    liver_diagnosis = "The person has liver disease"
                else:
                    liver_diagnosis = "The person does not have liver disease"

            st.success(liver_diagnosis)

    with tab2:
            st.title('Liver Disease ')
            st.markdown("""
        
        Liver disease refers to any condition that affects liver function and structure. The liver is responsible for detoxification, metabolism, and digestion.  
        Common causes include alcohol consumption, viral infections (such as Hepatitis B and C), fatty liver disease, and genetic disorders.
        """)

            # Add an image for liver disease symptoms
            st.image("C:/Users/sasik/OneDrive/Desktop/pro3 images/Liver-disease-Symptoms-scaled.jpg", 
                    caption="Common Symptoms of Liver Disease",use_container_width=True)  # Adjust width as needed

            st.header("Prevention & Management:")
            st.markdown("""
            
            - Maintain a balanced diet and avoid excessive fat intake.
            - Reduce alcohol consumption and avoid smoking.
            - Get vaccinated against Hepatitis B.
            - Stay physically active and maintain a healthy weight.
            - Regularly monitor liver function and avoid excessive medication use.
            """)




    

    # Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # Create side-by-side tabs
    tab1, tab2 = st.tabs([ "🩸 Parkinsons Disease Diagnosis","📄 About Parkinsons Disease",])

    with tab1:
        
            # page title
            st.title("Parkinsons Prediction ")
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                fo = st.text_input('MDVP:Fo(Hz)')

            with col2:
                fhi = st.text_input('MDVP:Fhi(Hz)')

            with col3:
                flo = st.text_input('MDVP:Flo(Hz)')

            with col4:
                Jitter_percent = st.text_input('MDVP:Jitter(%)')

            with col5:
                Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

            with col1:
                RAP = st.text_input('MDVP:RAP')

            with col2:
                PPQ = st.text_input('MDVP:PPQ')

            with col3:
                DDP = st.text_input('Jitter:DDP')

            with col4:
                Shimmer = st.text_input('MDVP:Shimmer')

            with col5:
                Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

            with col1:
                APQ3 = st.text_input('Shimmer:APQ3')

            with col2:
                APQ5 = st.text_input('Shimmer:APQ5')

            with col3:
                APQ = st.text_input('MDVP:APQ')

            with col4:
                DDA = st.text_input('Shimmer:DDA')

            with col5:
                NHR = st.text_input('NHR')

            with col1:
                HNR = st.text_input('HNR')

            with col2:
                RPDE = st.text_input('RPDE')

            with col3:
                DFA = st.text_input('DFA')

            with col4:
                spread1 = st.text_input('spread1')

            with col5:
                spread2 = st.text_input('spread2')

            with col1:
                D2 = st.text_input('D2')

            with col2:
                PPE = st.text_input('PPE')

                

            # code for Prediction
            parkinsons_diagnosis = ''

            # creating a button for Prediction    
            if st.button("Parkinson's Test Result"):

                user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                            RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                            APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

                user_input = [float(x) for x in user_input]

                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)

    with tab2:
        st.title('Parkinsons Disease ')

        st.markdown("""
        
        
        Parkinson’s disease is a progressive neurological disorder that affects movement. It occurs when nerve cells in the brain produce less dopamine, leading to tremors, stiffness, and difficulty with balance and coordination.Common causes include genetic factors, environmental triggers, and aging.
        """)

        # Add an image for Parkinson’s disease symptoms
        st.image("C:/Users/sasik/OneDrive/Desktop/pro3 images/How to use Chatgpt (26).webp", 
                caption="Common Symptoms of Parkinson’s Disease",use_container_width=True)  # Adjust width as needed

        st.header("Prevention & Management:")
        st.markdown("""
        
        - Engage in regular physical activity to maintain mobility.
        - Follow a healthy diet rich in antioxidants (e.g., fruits, vegetables, whole grains).
        - Avoid exposure to pesticides and environmental toxins.
        - Participate in cognitive and motor exercises to support brain function.
        - Consult a neurologist for early diagnosis and treatment options.
        """)
