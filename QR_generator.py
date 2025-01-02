import segno
import streamlit as st
import io

st.set_page_config(page_title="Link to QR Code Converter", page_icon='😊')

st.title("QR Code Generator")
st.toast("👋 Welcome to my page")

# Input field for text/URL
a = st.text_input("Enter the text/URL you want to convert to a QR code")

# Customize QR code appearance
scale = st.slider("Select the blur scale of the QR code", min_value=1, max_value=20, value=10)
border = st.slider("Select the border size of the QR code", min_value=1, max_value=10, value=4)
color = st.color_picker("Pick a color for the QR code", "#000000")

if a:
    # Generate QR code
    qrcode = segno.make(a)

    # Save QR code to an in-memory file
    buffer = io.BytesIO()
    qrcode.save(buffer, kind='png', scale=scale, border=border, dark=color)
    buffer.seek(0)

    # Display the QR code
    st.image(buffer, caption='Generated QR Code', use_conatiner_width=True)

    # Provide download button
    st.download_button(
        label="Download QR Code",
        data=buffer,
        file_name="qrcode.png",
        mime="image/png"
    )

# Add a section with usage tips
st.sidebar.header("Usage Tips")
st.sidebar.info("""
- Enter a valid URL or any text you want to encode into a QR code.
- Use the sliders to adjust the scale and border size.
- Pick your favorite color for the QR code.
- Click the download button to save the QR code as an image.
""")

st.sidebar.markdown("Developed by [Vipul Singh](https://github.com/your-profile)")
