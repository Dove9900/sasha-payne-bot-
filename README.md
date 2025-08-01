# sasha-payne-bot-
NLP-powered news classification and analysis tool built with Streamlit.




How to Run the Project

1.Install Dependencies
pip install -r requirements.txt

2.Download NLP resources and models required for your Sasha Payne NewsBot to perform tokenization, lemmatization, sentiment analysis, and entity recognition.
python -m nltk.downloader punkt stopwords wordnet
>> python -m textblob.download_corpora
>> python -m spacy download en_core_web_sm

3. Train the Model
python train_model.py

4. Run the App
python -m streamlit run app.py
