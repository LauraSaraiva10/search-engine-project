import txtai
import pandas as pd

df = pd.read_csv('data/seth-data.csv').dropna()

content = df.content_plain.values

embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/paraphrase-mpnet-base-v2'
})

embeddings.index(content)

embeddings.save('embeddings/embeddings_seth.tar.gz')