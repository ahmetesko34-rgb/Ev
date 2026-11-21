import os
import tkinter as tk
from tkinter import messagebox
DOSYA = "kullanicilar.txt"
# renkler
BG, KART, VURGU, YESIL, BEYAZ = "#0f172a", "#1e293b", "#38bdf8", "#4ade80", "#f8fafc"
# veriler
kulupler = ["Matematik", "Türkçe", "Fizik"]
toplantilar = {"Matematik": ("Pazartesi", "15.00"), "Türkçe": ("Çarşamba", "15.30"), "Fizik": ("Cuma", "14.30")}
kayitlar = {"Matematik": set(), "Türkçe": set(), "Fizik": set()}
ogrenciler = {}
# kaydetme
def verileri_yukle():
    if not os.path.exists(DOSYA): return
    with open(DOSYA, "r", encoding="utf-8") as f:
        for satir in f:
            p = satir.strip().split(",")
            if len(p) == 4:
                ogrenciler[p[1]] = {"ad": p[0], "sifre": p[2], "kulup": p[3]}
                if p[3] in kayitlar: kayitlar[p[3]].add(p[1])
def verileri_kaydet():
    with open(DOSYA, "w", encoding="utf-8") as f:
        for no, b in ogrenciler.items(): f.write(f"{b['ad']},{no},{b['sifre']},{b['kulup']}\n")
# animasyon
aktif_kart = None
def ekran_gecisi(fonk, yon=1, param=None):
    global aktif_kart
    yeni = tk.Frame(pencere, bg=KART)
    if param: fonk(yeni, param)
    else: fonk(yeni)
    if aktif_kart is None:
        yeni.place(relx=0.5, rely=0.5, width=420, height=480, anchor="center")
        aktif_kart = yeni
        return
    eski = aktif_kart
    aktif_kart = yeni
    x_pos = 500 * yon
    yeni.place(relx=0.5, rely=0.5, x=x_pos, width=420, height=480, anchor="center")
    def kaydir():
        nonlocal x_pos
        if yon == 1 and x_pos > 0:
            x_pos -= 25
            yeni.place(relx=0.5, rely=0.5, x=x_pos, width=420, height=480, anchor="center")
            eski.place(relx=0.5, rely=0.5, x=x_pos - 500, width=420, height=480, anchor="center")
            pencere.after(15, kaydir)
        elif yon == -1 and x_pos < 0:
            x_pos += 25
            yeni.place(relx=0.5, rely=0.5, x=x_pos, width=420, height=480, anchor="center")
            eski.place(relx=0.5, rely=0.5, x=x_pos + 500, width=420, height=480, anchor="center")
            pencere.after(15, kaydir)
        else:
            yeni.place(relx=0.5, rely=0.5, x=0, width=420, height=480, anchor="center")
            eski.destroy()
    kaydir()
# login
def giris_ekrani(f):
    tk.Label(f, text="Kulüp Giriş Sistemi", font=("Arial", 16, "bold"), bg=KART, fg=BEYAZ).pack(pady=30)
    tk.Label(f, text="Okul Numarası:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    e_no = tk.Entry(f, font=("Arial", 11), bg="#3e3e4f", fg=BEYAZ, relief="flat")
    e_no.pack(fill="x", padx=50, pady=5, ipady=4)

    tk.Label(f, text="Şifre:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    e_sifre = tk.Entry(f, font=("Arial", 11), bg="#3e3e4f", fg=BEYAZ, relief="flat", show="*")
    e_sifre.pack(fill="x", padx=50, pady=5, ipady=4)
    def giris_yap():
        no, sifre = e_no.get().strip(), e_sifre.get().strip()
        if no in ogrenciler and ogrenciler[no]["sifre"] == sifre:
            messagebox.showinfo("Başarılı", f"Hoş geldin {ogrenciler[no]['ad']}!")
            ekran_gecisi(panel_ekrani, yon=1, param=no)
        else: messagebox.showerror("Hata", "Okul numarası veya şifre hatalı!")
    tk.Button(f, text="GİRİŞ YAP", bg=VURGU, fg=BEYAZ, font=("Arial", 10, "bold"), relief="flat", command=giris_yap).pack(fill="x", padx=50, pady=20, ipady=5)
    tk.Button(f, text="Kayıt Olmak İçin Tıkla", bg=KART, fg=VURGU, relief="flat", command=lambda: ekran_gecisi(kayit_ekrani, yon=1)).pack()
# register
def kayit_ekrani(f):
    tk.Label(f, text="Öğrenci Kayıt Ol", font=("Arial", 16, "bold"), bg=KART, fg=BEYAZ).pack(pady=15)
    tk.Label(f, text="Ad Soyad:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    e_ad = tk.Entry(f, bg="#3e3e4f", fg=BEYAZ, relief="flat"); e_ad.pack(fill="x", padx=50, pady=2, ipady=3)
    tk.Label(f, text="Okul Numarası:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    e_no = tk.Entry(f, bg="#3e3e4f", fg=BEYAZ, relief="flat"); e_no.pack(fill="x", padx=50, pady=2, ipady=3)
    tk.Label(f, text="Şifre:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    e_sifre = tk.Entry(f, bg="#3e3e4f", fg=BEYAZ, relief="flat", show="*"); e_sifre.pack(fill="x", padx=50, pady=2, ipady=3)
    tk.Label(f, text="Kulüp Seç:", bg=KART, fg=BEYAZ).pack(anchor="w", padx=50)
    lb = tk.Listbox(f, height=3, bg="#3e3e4f", fg=BEYAZ, relief="flat"); lb.pack(fill="x", padx=50, pady=2)
    for k in kulupler: lb.insert(tk.END, k)
    def kaydet():
        ad, no, sifre, secim = e_ad.get().strip(), e_no.get().strip(), e_sifre.get().strip(), lb.curselection()
        if not ad or not no or not sifre or not secim: messagebox.showwarning("Uyarı", "Tüm alanları doldurun!"); return
        if no in ogrenciler: messagebox.showerror("Hata", "Bu numara zaten kayıtlı!"); return
        kulup = kulupler[secim[0]]
        kayitlar[kulup].add(no)
        ogrenciler[no] = {"ad": ad, "sifre": sifre, "kulup": kulup}
        verileri_kaydet()
        messagebox.showinfo("Başarılı", "Kayıt oldun! Giriş yapabilirsin.")
        ekran_gecisi(giris_ekrani, yon=-1)
    tk.Button(f, text="KAYDI TAMAMLA", bg=YESIL, fg=BEYAZ, font=("Arial", 10, "bold"), relief="flat", command=kaydet).pack(fill="x", padx=50, pady=10, ipady=4)
    tk.Button(f, text="Geri Dön", bg=KART, fg=BEYAZ, relief="flat", command=lambda: ekran_gecisi(giris_ekrani, yon=-1)).pack()
# uygulama içi
def panel_ekrani(f, no):
    ogr = ogrenciler[no]
    k, (gun, saat) = ogr["kulup"], toplantilar[ogr["kulup"]]
    tk.Label(f, text=f"Hoş geldin, {ogr['ad']}!", font=("Arial", 14, "bold"), bg=KART, fg=BEYAZ).pack(pady=20)
    tk.Label(f, text=f"Seçtiğin Kulüp: {k}\nToplantı: {gun} - {saat}", font=("Arial", 10), bg="#3e3e4f", fg=BEYAZ, padx=10, pady=8).pack(fill="x", padx=40, pady=5)
    tk.Label(f, text=f"Kulüpteki Toplam Üye Sayısı: {len(kayitlar[k])}", bg=KART, fg=YESIL, font=("Arial", 10, "bold")).pack(pady=5)
    def kaydi_sil():
        if messagebox.askyesno("Onay", "Kaydını silmek istiyor musun?"):
            kayitlar[k].remove(no)
            del ogrenciler[no]
            verileri_kaydet()
            messagebox.showinfo("Bilgi", "Kaydın silindi.")
            ekran_gecisi(giris_ekrani, yon=-1)
    tk.Button(f, text="Kulüp Kaydımı Sil", bg="#e74c3c", fg=BEYAZ, relief="flat", command=kaydi_sil).pack(fill="x", padx=40, pady=10, ipady=3)
    tk.Button(f, text="Çıkış Yap", bg=VURGU, fg=BEYAZ, relief="flat", command=lambda: ekran_gecisi(giris_ekrani, yon=-1)).pack(fill="x", padx=40, pady=5, ipady=3)
# çalıştır
pencere = tk.Tk()
pencere.title("Kulüp Kayıt Sistemi")
pencere.geometry("550x550")
pencere.config(bg=BG)
verileri_yukle()
if len(ogrenciler) == 0: ekran_gecisi(kayit_ekrani, yon=1)
else: ekran_gecisi(giris_ekrani, yon=1)
pencere.mainloop()