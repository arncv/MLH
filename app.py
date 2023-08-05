import taipy as ti

# Load the dataset
news = ti.load_dataset('news')

# Preprocess the text data
news['text'] = news['text'].apply(ti.preprocess_text)

# Build the topic model
model = ti.build_topic_model(news['text'], num_topics=5)

# Classify the news articles into different topics
news['topic'] = model.predict(news['text'])

# Print the top 10 words for each topic
for i in range(5):
    print(f"Topic {i}:")
    print(model.top_words(i, 10))
    print()
