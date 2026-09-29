# 🏭 Ternium – Détection de défauts sur bobines d'acier

Application Streamlit d'aide à la décision développée avec **Ternium** (sidérurgie) pendant mon semestre Data & IA au **Tec de Monterrey** (Mexique, 2024).

Elle exploite les données des capteurs du laminoir à chaud pour contrôler le procédé, repérer les capteurs au comportement anormal et prédire les bobines défectueuses.

## Fonctionnalités

| Page | Ce qu'elle fait |
|---|---|
| **Home** | Import d'un fichier CSV et prédiction « approuvée / défectueuse » pour chaque bobine avec deux modèles : SVC et Gradient Boosting |
| **Sensor Visualization** | Exploration interactive des mesures des capteurs, filtrées par matériau et par capteur |
| **Sensor Classification** | Détection des capteurs anormaux par distance de Mahalanobis, avec un seuil dynamique (95e percentile des matériaux approuvés) |
| **Cluster Specifications** | Segmentation des brames selon leur poids par K-Means (4 clusters) |
| **Dictionary** | Dictionnaire des capteurs et classification des aciers par dureté (soft, medium, hard) |

## Stack

Python · Streamlit · pandas · scikit-learn (SVC, Gradient Boosting, K-Means) · Matplotlib · joblib

## Lancer l'application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Structure

```
app.py                         # point d'entrée et menu de navigation
app_pages/                     # une page Streamlit par fonctionnalité
datasets/                      # données capteurs, défauts et dictionnaire
images/                        # visuels de l'application
svc_model.pkl                  # modèle SVC entraîné
gradient_boosting_model.pkl    # modèle Gradient Boosting entraîné
```

## Équipe

Projet de l'équipe 4 « Seiketsu », Tec de Monterrey × Ternium, 2024 : Andrea Espíndola, Daniela Alapizco, Clara Chalayer.
