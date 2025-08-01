import streamlit as st
from utils.preprocessing import preprocess_text
from utils.features import get_tfidf_features, get_pos_tags, get_dependencies
from utils.sentiment import analyze_sentiment
from utils.classification import classify_news
from utils.ner import extract_named_entities

st.set_page_config(page_title="Sasha Payne NewsBot", layout="wide")

st.title("📰 Sasha Payne – News Intelligence Bot")

news_text = st.text_area("Paste a news article below:", height=300)

if st.button("Analyze Article") and news_text:
    with st.spinner("Processing..."):
        clean_text = preprocess_text(news_text)

        tfidf_features = get_tfidf_features(clean_text)
        classification = classify_news(tfidf_features)

        sentiment_score, sentiment_label = analyze_sentiment(clean_text)
        named_entities = extract_named_entities(clean_text)
        pos_tags = get_pos_tags(clean_text)
        dependencies = get_dependencies(clean_text)

    st.subheader("🧠 Prediction & Sentiment")
    st.markdown(f"**Category:** {classification}")
    st.markdown(f"**Sentiment:** {sentiment_label} (Score: {sentiment_score})")

    st.subheader("🧾 Named Entities")
    st.json(named_entities)

    st.subheader("🔍 POS Tags")
    st.code(pos_tags)

    st.subheader("🔗 Dependency Relations")
    st.code(dependencies)

    st.success("Insight generated by Sasha Payne ✅")
