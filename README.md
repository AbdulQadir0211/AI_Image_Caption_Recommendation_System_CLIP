---
title: AI Image Caption Recommendation Using CLIP
emoji: 🌍
colorFrom: pink
colorTo: blue
sdk: streamlit
sdk_version: 1.42.1
app_file: app.py
pinned: false
license: mit
short_description: This AI system recommends captions for the images
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference


# AI Image Caption Recommender System with CLIP

This project is an AI-powered image caption recommender system built using OpenAI's CLIP model. It recommends captions for social media posts (Instagram, Facebook, etc.) by finding the most relevant captions from a curated list based on the uploaded image.

---

## Problem Statement
Social media users often struggle to come up with engaging captions for their posts. This project solves that problem by automatically recommending captions that best match an uploaded image, helping users enhance their social media presence effortlessly.

---

## Features
- Upload images via a web interface.
- Generate image embeddings using CLIP.
- Match images to relevant captions from a predefined list.
- Display top 5 most relevant captions with similarity scores.
- Modular code structure for easy maintenance and scalability.

---

## Project Structure
```
clip_caption_recommender/
│
├── app.py              # Main Streamlit app
├── image_utils.py      # Image processing functions
├── model_utils.py      # CLIP model loading and embeddings
├── caption_utils.py    # Caption matching logic
├── captions.txt        # List of predefined captions
└── requirements.txt    # Project dependencies
```

---

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/clip-caption-recommender.git
cd clip-caption-recommender

# Install dependencies
pip install -r requirements.txt
```

---

## Usage
```bash
# Run the Streamlit app
streamlit run app.py
```
- Upload an image.
- View top 5 recommended captions with similarity scores.

---

## Adding More Captions
- Add more captions in `captions.txt` with one caption per line.

---

## Technologies Used
- Python
- OpenAI CLIP
- Streamlit
- Transformers
- scikit-learn
- Pillow

---

## Future Improvements
- Integrate with social media APIs for direct caption posting.
- Allow users to add personalized captions.
- Implement fine-tuning on domain-specific datasets.
- Deploy using Docker and AWS for scalability.

---

## Author
- **Your Name**  
  [LinkedIn](https://linkedin.com/in/abdul-qadir0) | [GitHub](https://github.com/AbdulQadir0211)

---

## License
This project is licensed under the MIT License.

---

Happy Posting! 🚀


