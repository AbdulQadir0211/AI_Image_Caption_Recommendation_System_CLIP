import torch
from sklearn.metrics.pairwise import cosine_similarity

def match_captions(image_features, captions, clip_model, processor):
    text_inputs = processor(text=captions, return_tensors="pt", padding=True)
    with torch.no_grad():
        text_features = clip_model.get_text_features(**text_inputs)

    image_features = image_features.detach().cpu().numpy()
    text_features = text_features.detach().cpu().numpy()

    similarities = cosine_similarity(image_features, text_features)
    best_indices = similarities.argsort(axis=1)[0][::-1]  
    best_captions = [captions[i] for i in best_indices]

    return best_captions, similarities[0][best_indices].tolist()