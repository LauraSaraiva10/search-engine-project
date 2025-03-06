import txtai
import numpy as np
import pandas as pd

np.random.seed(1)

df = pd.read_csv('data/amazon-data.csv')

titles = df.dropna().sample(5905, replace=False).TITLE.values

embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/all-MiniLM-L6-v2'
})

embeddings.index(titles)

embeddings.save('embeddings/embeddings_amazon.tar.gz')

results = embeddings.search('protector for cam', 5)

# Test
print(results)

actual_results = [titles[x[0]] for x in results]

print(actual_results)

