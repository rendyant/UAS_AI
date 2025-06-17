from experta import *

# Fakta: Preferensi wisata pengguna
class MinatWisatawan(Fact):
    pass

# Sistem Pakar Rekomendasi Wisata Indonesia
class WisataIndonesia(KnowledgeEngine):

    @Rule(OR(MinatWisatawan(sejarah='y'), MinatWisatawan(pemandangan='y')))
    def kunjungi_candi_borobudur(self):
        print("Kunjungi Candi Borobudur di Magelang")

    @Rule(AND(MinatWisatawan(petualangan='y'), MinatWisatawan(alam_terbuka='y')))
    def hiking_gunung_bromo(self):
        print("Lakukan pendakian ringan ke Gunung Bromo")

    @Rule(AND(MinatWisatawan(kuliner_tradisional='y')))
    def wisata_kuliner_jogja(self):
        print("Coba wisata kuliner tradisional di Yogyakarta")

    @Rule(AND(MinatWisatawan(seni_budaya='y'), MinatWisatawan(pertunjukan='y')))
    def nonton_sendratari(self):
        print("Saksikan pertunjukan Sendratari Ramayana di Prambanan")

    @Rule(AND(MinatWisatawan(relaksasi='y')))
    def santai_di_bali(self):
        print("Relaksasi di pantai-pantai Bali")

    @Rule(AND(MinatWisatawan(belanja='y'), MinatWisatawan(kota='y')))
    def belanja_di_bandung(self):
        print("Belanja di Factory Outlet Bandung")

    @Rule(AND(MinatWisatawan(musik='y'), MinatWisatawan(kota='y')))
    def konser_jakarta(self):
        print("Tonton konser musik di Jakarta")

    @Rule(AND(MinatWisatawan(pemandangan='y'), MinatWisatawan(laut='y')))
    def diving_raja_ampat(self):
        print("Diving atau snorkeling di Raja Ampat")

    @Rule(AND(MinatWisatawan(kuliner_modern='y'), MinatWisatawan(budget_tinggi='y')))
    def makan_di_restoran_mewah(self):
        print("Makan di restoran fine-dining Jakarta/Bali")

    # Jika tidak ada minat terdeteksi
    @Rule(AND(MinatWisatawan(sejarah='n'), MinatWisatawan(pemandangan='n'),
              MinatWisatawan(petualangan='n'), MinatWisatawan(alam_terbuka='n'),
              MinatWisatawan(kuliner_tradisional='n'), MinatWisatawan(seni_budaya='n'),
              MinatWisatawan(pertunjukan='n'), MinatWisatawan(relaksasi='n'),
              MinatWisatawan(belanja='n'), MinatWisatawan(kota='n'),
              MinatWisatawan(musik='n'), MinatWisatawan(laut='n'),
              MinatWisatawan(kuliner_modern='n'), MinatWisatawan(budget_tinggi='n')))
    def tidak_ada_rekomendasi(self):
        print("Maaf, kami tidak menemukan rekomendasi wisata yang cocok berdasarkan minat Anda.")

# Main Program
print("="*90)
print("Selamat Datang di Sistem Rekomendasi Wisata Indonesia")
print("Kami akan membantu merekomendasikan destinasi terbaik di Indonesia berdasarkan minat Anda.")
print("="*90)

mulai = input("Apakah Anda ingin memulai (y/n)? ")

if mulai == 'y':
    sistem = WisataIndonesia()
    sistem.reset()

    minat = {}
    # Input preferensi pengguna
    minat['sejarah'] = input("\n> Apakah Anda menyukai sejarah (y/n)? ").lower()
    minat['pemandangan'] = input("> Apakah Anda suka melihat pemandangan (y/n)? ").lower()
    minat['petualangan'] = input("> Apakah Anda menyukai petualangan (y/n)? ").lower()
    minat['alam_terbuka'] = input("> Apakah Anda senang kegiatan di alam terbuka (y/n)? ").lower()
    minat['kuliner_tradisional'] = input("> Apakah Anda tertarik mencoba kuliner tradisional (y/n)? ").lower()
    minat['seni_budaya'] = input("> Apakah Anda suka seni dan budaya (y/n)? ").lower()
    minat['pertunjukan'] = input("> Apakah Anda suka menonton pertunjukan (y/n)? ").lower()
    minat['relaksasi'] = input("> Apakah Anda ingin relaksasi (y/n)? ").lower()
    minat['belanja'] = input("> Apakah Anda suka belanja (y/n)? ").lower()
    minat['kota'] = input("> Apakah Anda lebih suka wisata di kota (y/n)? ").lower()
    minat['musik'] = input("> Apakah Anda suka musik (y/n)? ").lower()
    minat['laut'] = input("> Apakah Anda menyukai wisata laut (y/n)? ").lower()
    minat['kuliner_modern'] = input("> Apakah Anda suka kuliner modern (y/n)? ").lower()
    minat['budget_tinggi'] = input("> Apakah Anda memiliki anggaran tinggi (y/n)? ").lower()

    print("\nRekomendasi wisata untuk Anda berdasarkan preferensi:")
    print("-"*60)
    sistem.declare(MinatWisatawan(**minat))
    sistem.run()
else:
    print("Silakan coba nanti jika Anda berubah pikiran.")

print("="*90)
print("Terima kasih telah menggunakan Sistem Rekomendasi Wisata Indonesia!")
print("="*90)
