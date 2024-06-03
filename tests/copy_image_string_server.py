import streamlit as st
import base64
from PIL import Image
from io import BytesIO
import pyperclip


def convert_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def convert_to_rdf(pil_image):
    img_str = convert_to_base64(pil_image)
    return \
        f"""PREFIX ajan-ns:<http://www.dfki.de/ajan-ns#>
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        
        ajan-ns:imageData {{
        ajan-ns:warehouseImage rdfs:type ajan-ns:Image .
        ajan-ns:base64String rdfs:Value "{img_str}"^^xsd:string ;
        }}"""


def main():
    st.title("Image to Base64 Converter")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Convert image to base64
        img_str = convert_to_rdf(image)

        st.text("Base64 String:")
        st.code(img_str)
        if st.button("Copy to Clipboard"):
            pyperclip.copy(img_str)
        # Copy to clipboard
        pyperclip.copy(img_str)
        st.success("Base64 string copied to clipboard!")


if __name__ == "__main__":
    main()
