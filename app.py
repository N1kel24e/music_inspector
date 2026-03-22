import streamlit as st
import joblib
import pandas as pd

df = pd.read_csv('tracks_with_clusters.csv')

model = joblib.load('kmeans.pkl')
scaler = joblib.load('scaler.pkl')

def song_search(song, artists):
    result = df[df['track_name'].str.contains(song, na=False, case=False) & df['artists'].str.contains(artists, na=False, case=False)]
    result = result.drop_duplicates(subset=['track_name', 'artists'])
    result = result [['track_name', 'artists', 'cluster_name', 'energy', 'tempo', 'valence', 'danceability', 'acousticness',]]
    return result

def get_similar (cluster):
    similar = df[df['cluster_name'] == cluster]
    similar = similar.sample(n=5)
    similar = similar[['track_name', 'artists',]]
    return similar

def song_analyze (song, artists):
    search = song_search(song, artists)
    if search.empty:
        return search, None
    cluster = search['cluster_name'].iloc[0]
    similar = get_similar(cluster)
    return search, similar

st.title('Music Inspector')
st.write('Analyze any track and find music that sounds just like it')

artist = st.text_input('Enter artist')
song = st.text_input('Enter song')

if st.button('Analyze'):
    track_info, similar = song_analyze(song, artist)
    if track_info.empty:
        st.warning("Track not found. Try different spelling!")
        st.stop()
    st.write('Song name: ')
    st.write(track_info['track_name'].iloc[0])
    st.write('Artist: ')
    st.write(track_info['artists'].iloc[0])
    st.write("Track info:")
    st.write("Genre cluster: " + track_info['cluster_name'].iloc[0])
    st.write("Energy")
    st.progress(track_info['energy'].iloc[0])
    st.write("Valence")
    st.progress(track_info['valence'].iloc[0])
    st.write("Danceability")
    st.progress(track_info['danceability'].iloc[0])
    st.write("Acousticness")
    st.progress(track_info['acousticness'].iloc[0])
    st.write("Similar tracks:")
    st.write(similar)