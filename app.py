import streamlit as st
from audio_analysis import analyze_audio
from content_analysis import analyze_content
from shark_agents import generate_shark_feedback

st.title("🎤 Shark Tank Pitch Analyzer")
st.write("Upload your pitch audio and get investor-style feedback.")

audio_file = st.file_uploader("Upload Pitch Audio (.wav or .mp3)", type=["wav", "mp3"])

if audio_file:
    st.audio(audio_file)

    with st.spinner("Analyzing delivery..."):
        delivery_score, delivery_summary = analyze_audio(audio_file)

    with st.spinner("Transcribing & analyzing content..."):
        transcript, content_score, content_summary = analyze_content(audio_file)

    with st.spinner("Generating Virtual Shark Feedback..."):
        feedback, verdict = generate_shark_feedback(
            transcript, delivery_score, content_score
        )

    st.subheader("📌 Transcript")
    st.write(transcript)

    st.subheader("🎯 Delivery Score")
    st.write(delivery_score, delivery_summary)

    st.subheader("💼 Business Content Score")
    st.write(content_score, content_summary)

    st.subheader("🦈 Shark Panel Feedback")
    st.write(feedback)

    st.subheader("🏁 Final Verdict")
    st.write(f"**{verdict}**")
