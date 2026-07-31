# GET324 – PE9 Mini-Project: Tomato Blight Classifier

## Task
Binary image classification: **Tomato Early Blight vs Tomato Late Blight**
Course: GET324 – Laboratory Exercise 10 (Mini-Project)

## Group Members (PE9)

| Name | Registration Number | GitHub Username |
|---|---|---|
| Icho, Eti Cyril | 23/EG/PE/028 | Hairtea-fx |
| Hanson, Abasiakan Daniel | 23/EG/PE/018 | abashanson2006-cell |
| Inyang Israel Uko | 22/EG/PE/1478 | Da-iszy44 |
| Ubi Gladys Hycienth | 22/EG/PE/1498 | ubigladyso-tech |
| Godswill Ime Ubak | 23/EG/PE/008 | MRMONEYXIII |
| Bassey, Michael Ime | 22/EG/PE/1538 | dr784 |
| Favour Ofonmbuk Asuquo | 23/EG/PE/038 | genesisnode-alt
| Uko-Eninn, Anietie Augustine | 22/EG/PE/1548 | austine1710
| Udo, Ekemini Paul| 22/EG/PE/1468 | ekeminipaul068-gif

## Project Structure
- `train_model.py` – trains the CNN (MobileNetV2 transfer learning) on the dataset
- `app.py` – Streamlit web app for making predictions
- `tomato_blight_model.keras` – saved trained model
- `dataset/` – training images (Tomato___Early_blight, Tomato___Late_blight)
- `requirements.txt` – Python dependencies

## Model Performance
Final validation accuracy: **95.7%**

