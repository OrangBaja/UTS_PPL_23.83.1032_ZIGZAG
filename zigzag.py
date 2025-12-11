import time, sys

# --- FUNGSI BANTUAN MATEMATIKA ---
def is_prime(n):
    """Mengecek apakah n adalah bilangan prima"""
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

indent = 0
indentIncreasing = True

try:
    print("Menganalisis Struktur DNA... (Tekan Ctrl+C untuk berhenti)")
    time.sleep(1)
    
    while True:
        # --- FITUR 1: PARITY SHAPE-SHIFTER (Ganjil/Genap) ---
        # Tema DNA: Mengubah jenis 'Base Pair' (Pasangan Basa)
        # Genap = Pasangan Adenine-Thymine (A-T) dengan kurung bulat
        # Ganjil = Pasangan Guanine-Cytosine (G-C) dengan kurung siku
        if indent % 2 == 0:
            left_node = "(A"
            right_node = "T)"
        else:
            left_node = "[G"
            right_node = "C]"

        # --- FITUR 2: PRIME NUMBER DETECTOR (Matematika) ---
        # Tema DNA: Jika posisi adalah bilangan Prima, terjadi "Mutasi/Ikatan Kuat"
        # Konektor berubah dari "-" (tunggal) menjadi "=" (ganda)
        is_mutasi = is_prime(indent)
        
        if is_mutasi:
            connector_char = "=" # Ikatan ganda (Kuat/Prima)
            info_tambahan = " << MUTASI PRIMA!"
            # Highlight visual saat prima
            left_node = "*"+left_node[-1] # Ubah jadi bintang
            right_node = right_node[0]+"*"
        else:
            connector_char = "-" # Ikatan tunggal (Normal)
            info_tambahan = ""

        # --- LOGIKA VISUAL DNA (DOUBLE HELIX) ---
        # Agar terlihat seperti DNA, kita butuh dua sisi yang bergerak berlawanan.
        # indent = posisi sisi kiri.
        # (20 - indent) = posisi sisi kanan (cerminannya).
        
        spasi_kiri = ' ' * indent
        
        # Hitung jarak antara dua untaian DNA
        # Dikali 2 agar lebar DNA-nya proporsional
        lebar_tengah = (20 - indent) * 2 
        
        if lebar_tengah < 0: lebar_tengah = 0 # Mencegah error minus
        
        konektor = connector_char * lebar_tengah

        # --- FITUR 3: BINARY POSITION INDICATOR (Data) ---
        # Menampilkan data genetik (posisi) dalam biner
        kode_biner = format(indent, '05b') 

        # --- RENDER KE TERMINAL ---
        # Visual: [Spasi Kiri] [Node Kiri] [Konektor Tengah] [Node Kanan] [Info]
        if indent == 20:
             # Saat kedua untaian bertemu (Crossing point / Titik silang)
             print(f"{spasi_kiri}><  Bin:{kode_biner} {info_tambahan}")
        else:
             # Saat untaian terpisah
             print(f"{spasi_kiri}{left_node}{konektor}{right_node}  Bin:{kode_biner} {info_tambahan}")
        
        time.sleep(0.1)

        # --- LOGIKA ZIGZAG (Looping 0-20) ---
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()