import streamlit as st
from modules.image_utils import load_and_preprocess_image
from modules.model_utils import generate_image_embeddings
from modules.caption_utils import match_captions

def image_captioning(image_path, candidate_captions):  
    inputs, processor = load_and_preprocess_image(image_path)
    image_features, clip_model = generate_image_embeddings(inputs)
    best_captions, similarities = match_captions(image_features, candidate_captions, clip_model, processor)
    return best_captions, similarities

st.title("AI Image Caption Recommender with CLIP")
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

candidate_captions = ["Trees, Travel and Tea!", "A refreshing beverage.", ...]  # Add all captions

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    best_captions, similarities = image_captioning(uploaded_image, candidate_captions)
    st.write("### Top Captions")
    for idx, (caption, similarity) in enumerate(zip(best_captions[:5], similarities[:5])):
        st.write(f"{idx+1}. {caption} (Similarity: {similarity:.4f})")