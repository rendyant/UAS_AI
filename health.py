import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from PIL import Image

# =======================
# 1. BACA & PERSIAPAN DATA
# =======================
df = pd.read_csv("data-ori.csv")

# Encode data kategorik
le_sex = LabelEncoder()
le_source = LabelEncoder()
df['SEX'] = le_sex.fit_transform(df['SEX'])        # F=0, M=1
df['SOURCE'] = le_source.fit_transform(df['SOURCE'])  # out=0, in=1

# Pisahkan fitur dan label
X = df.drop('SOURCE', axis=1)
y = df['SOURCE']

# Normalisasi fitur numerik
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data untuk training
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Latih model k-NN
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# =======================
# 2. INPUT INTERAKTIF
# =======================
print("\n=== SISTEM PREDIKSI PERAWATAN PASIEN + VISUALISASI ===")
print("Silakan masukkan data pasien untuk melihat prediksi dan grafik analisis.\n")

haematocrit = float(input("HAEMATOCRIT: "))
haemoglobins = float(input("HAEMOGLOBINS: "))
erythrocyte = float(input("ERYTHROCYTE: "))
leucocyte = float(input("LEUCOCYTE: "))
thrombocyte = int(input("THROMBOCYTE: "))
mch = float(input("MCH: "))
mchc = float(input("MCHC: "))
mcv = float(input("MCV: "))
age = int(input("AGE: "))
sex = input("SEX (F/M): ").strip().upper()
sex_encoded = le_sex.transform([sex])[0]

# Gabungkan data input
user_data = pd.DataFrame([[haematocrit, haemoglobins, erythrocyte, leucocyte,
                           thrombocyte, mch, mchc, mcv, age, sex_encoded]],
                         columns=X.columns)

# Normalisasi
user_scaled = scaler.transform(user_data)

# Prediksi
prediction = model.predict(user_scaled)
result = le_source.inverse_transform(prediction)[0]

# =======================
# 3. TAMPILKAN PREDIKSI
# =======================
print(f"\n📋 Hasil prediksi: Pasien sebaiknya dirawat secara **{result.upper()}**")

# Gambar berdasarkan hasil
try:
    img_path = "rawat_inap.jpg" if result == 'in' else "rawat_jalan.jpg"
    img = Image.open(img_path)
    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Rekomendasi: {result.upper()}")
    plt.show()
except FileNotFoundError:
    print("(❗) Gambar tidak ditemukan.")

# =======================
# 4. VISUALISASI DATASET
# =======================
plt.figure(figsize=(10, 6))
sns.countplot(x=le_source.inverse_transform(df['SOURCE']), palette='Set2')
plt.title("Distribusi Jenis Perawatan (IN/OUT)")
plt.xlabel("Tipe Perawatan")
plt.ylabel("Jumlah Pasien")
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x=le_source.inverse_transform(df['SOURCE']), y='HAEMOGLOBINS', palette='Set3')
plt.title("Sebaran Nilai HAEMOGLOBINS Berdasarkan Jenis Perawatan")
plt.xlabel("Tipe Perawatan")
plt.ylabel("HAEMOGLOBINS")
plt.show()

# Heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Korelasi Antar Fitur")
plt.show()