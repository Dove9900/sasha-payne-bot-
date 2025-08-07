Sasha payne

Applied Artificial Intelligence & Robotics

Overview of Skills and Technologies

Over the course of the program, I developed strong technical and analytical skills in the following areas:

Programming Languages:Python, SQL, HTML/CSS/JavaScript (basic)

Libraries & Frameworks: scikit-learn, spaCy, NLTK, Pandas, NumPy, Flask, Streamlit, Matplotlib

Machine Learning: Supervised Learning, Model Evaluation, Classification, Clustering

Natural Language Processing: Tokenization, TF-IDF, Sentiment Analysis, POS Tagging, Named Entity Recognition, Dependency Parsing

Deployment: REST APIs, Streamlit Apps, Docker, Git/GitHub
-Soft Skills: Problem Solving, Collaboration, Communication, Agile Development



Course Descriptions – Applied AI & Robotics Program
Course	Description

AI Programming with Python: Foundations of Python programming, data structures, and object-oriented programming.

Machine Learning Fundamentals:Covered supervised and unsupervised learning models, evaluation metrics, and data preprocessing techniques.

Natural Language Processing (NLP):Explored text analysis, tokenization, POS tagging, NER, parsing, and language modeling using Python NLP libraries.

Applied AI Projects:Designed and implemented real-world AI systems, focusing on media and business applications.

AI System Deployment:Learned to package, deploy, and maintain machine learning models using Flask, Streamlit, and Docker.

Capstone Project:Built the Sasha Payne NewsBot: a real-time NLP-powered news classification and analysis system with a user-friendly UI.




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
