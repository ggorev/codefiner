import numpy as np
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = 'philomath-1209/programming-language-identification'
loaded_tokenizer = AutoTokenizer.from_pretrained(model_name)
loaded_model = AutoModelForSequenceClassification.from_pretrained(model_name)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
loaded_model.to(device)


class Prediction:
    def __init__(self, prediction):
        self.prediction = prediction
        self.probability = round(prediction["languages"][prediction["language"].lower()], 2)


def get_predict(text: str) -> Prediction:
    inputs = loaded_tokenizer(text, return_tensors="pt", truncation=True, padding=True)

    inputs = inputs.to(device)

    with torch.no_grad():
        outputs = loaded_model(**inputs)
        logits = outputs.logits

        probabilities = F.softmax(logits, dim=-1)

        probabilities = probabilities.cpu()
    probs = probabilities.detach().numpy()[0]

    labels = loaded_model.config.id2label

    top_three_indices = np.argsort(probs)[-3:][::-1]
    prediction = dict()
    predicted_class_id = top_three_indices[0]
    prediction["language"] = labels[predicted_class_id].lower()
    prediction["languages"] = dict()
    for index in top_three_indices:
        prediction["languages"][labels[index].lower()] = round(float(probs[index]), 2)
    return Prediction(prediction)
