## Music Inspector

A machine learning app that analyzes any Spotify track and finds similar music based on sound characteristics.

## Live Demo
[https://musicinspector-kscj8nnukdsgodhq9xzrbz.streamlit.app/]

## How it works
1. Enter a track name and artist
2. The app finds the track in the database and shows its sound profile
3. The K-Means clustering algorithm groups the track into one of 10 music categories
4. Similar tracks from the same cluster are recommended

## Sound characteristics
- **Energy** — intensity and activity of the track
- **Valence** — musical positivity (high = happy, low = sad)
- **Danceability** — how suitable the track is for dancing
- **Acousticness** — whether the track is acoustic or electronic

## Music clusters
- Acoustic Pop, Upbeat Electronic, Melancholic Acoustic, Sad Ballad
- Indie, Dark EDM, Hip-Hop, Sad Instrumental, Techno, Heavy Electronic

## Dataset
Spotify Tracks Dataset by Yash
[https://www.kaggle.com/datasets/yashdev01/spotify-tracks-dataset]

## Technologies
- Python
- pandas
- scikit-learn (K-Means clustering)
- Streamlit
- joblib
- matplotlib
