import pandas as pd
import ast
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# BACA & PRA-PROSES DATA
df = pd.read_csv("tourism_dataset_5000.csv")
df['Interests'] = df['Interests'].apply(lambda x: ast.literal_eval(x))

mlb = MultiLabelBinarizer()
interests_encoded = mlb.fit_transform(df['Interests'])
interests_df = pd.DataFrame(interests_encoded, columns=mlb.classes_)

le_site = LabelEncoder()
df['Site Name Encoded'] = le_site.fit_transform(df['Site Name'])

features = pd.concat([
    df[['Age', 'Preferred Tour Duration', 'Tourist Rating', 'VR Experience Quality']],
    interests_df
], axis=1)
labels = df['Site Name Encoded']

# LATIH MODEL
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# INTERAKTIF: INPUT PENGGUNA
print("\n===== SISTEM REKOMENDASI DESTINASI WISATA =====")
print("Masukkan data Anda untuk mendapatkan rekomendasi:\n")

age = int(input("Umur Anda: "))
duration = int(input("Durasi tur yang diinginkan (hari): "))
rating = float(input("Berapa rating rata-rata Anda berikan ke wisata? (1.0 - 5.0): "))
vr_quality = float(input("Seberapa penting pengalaman VR bagi Anda? (1.0 - 5.0): "))

print("\nPilih minat wisata Anda (pisahkan dengan koma, contoh: Art,History,Cultural)")
print("Pilihan tersedia:", list(mlb.classes_))
minat_input = input("Minat Anda: ").strip().split(',')

# Bersihkan input
minat_input = [i.strip().capitalize() for i in minat_input]

# Encode minat
interest_vector = [1 if interest in minat_input else 0 for interest in mlb.classes_]

# Buat data pengguna baru
user_data = pd.DataFrame([[age, duration, rating, vr_quality] + interest_vector],
                         columns=features.columns)

# PREDIKSI
prediction = knn.predict(user_data)
recommended_site = le_site.inverse_transform(prediction)

# 5. OUTPUT
print("\n🎯 Destinasi wisata yang direkomendasikan untuk Anda adalah:")
print(f">>> {recommended_site[0]}")