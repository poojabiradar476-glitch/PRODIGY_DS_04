import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate Social Media Sentiment Dataset
np.random.seed(42)
brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD']
sentiments = ['Positive', 'Neutral', 'Negative']

data = {
    'Brand': np.random.choice(brands, size=1200),
    'Sentiment': np.random.choice(sentiments, size=1200, p=[0.45, 0.35, 0.20]),
    'Platform': np.random.choice(['Twitter', 'Instagram', 'Facebook'], size=1200)
}
df = pd.DataFrame(data)

# Sentiment Distribution per Brand
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Brand', hue='Sentiment', palette='viridis')
plt.title('Sentiment Distribution Across Brands', fontsize=14)
plt.xlabel('Brand')
plt.ylabel('Post Count')
plt.legend(title='Sentiment')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()

print("Task 4 Completed successfully.")
