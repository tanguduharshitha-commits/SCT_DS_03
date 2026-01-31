import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# 1. Load the UCI Bank Marketing dataset
# The dataset has 45,211 instances and 16 features
df = pd.read_csv('bank.csv', sep=';')

# 2. Preprocessing
# We must convert categorical text into numbers for the model
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    df[col] = le.fit_transform(df[col])

X = df.drop('y', axis=1) # Features: age, job, duration, etc.
y = df['y'] # Target: will they subscribe?

# 3. Train the Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(max_depth=3) # Depth 3 matches your Excel tree
clf.fit(X_train, y_train)

# 4. Generate the Decision Tree Image
plt.figure(figsize=(15,8))
plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.title("Task 03: Bank Marketing Decision Tree Classifier")
plt.show()