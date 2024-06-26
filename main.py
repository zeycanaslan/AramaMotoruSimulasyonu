import tkinter
import webbrowser
from tkinter import messagebox


def giris_sifresi():
    def tamam():
        global girilen_sifre

        # Giriş şifresini girin
        girilen_sifre = entry.get()

        # Şifreyi doğrulayın
        if girilen_sifre=="zeycoo":
            messagebox.showinfo("Bilgi", f"Girdiğiniz sifre: {girilen_sifre}")
            giris_kutusu.destroy()

            def open_url():  # girilmiş url yi açar
                url = text_input.get("1.0", "end")
                if url:
                    webbrowser.open(url)

            def callback(url):  # hızlı giriş için
                if url:
                    webbrowser.open_new(url)

            def temizle():
                text_input.delete("1.0", "end")

            def readme():
                with open("readme","r",encoding="UTF-8") as file:
                    a=file.read()
                    print(a)


            label = tkinter.Label(text="Girmek istediğiniz siteyi giriniz.", font="Arial 20", background="pink")
            label.pack(ipadx=10, ipady=20)

            text_input = tkinter.Text(background="white", width=30, height=2)
            text_input.pack()

            ara = tkinter.Button(text="Ara", command=open_url, font="Arial 10", width=10, height=2)
            ara.pack(pady=30, padx=20)

            temizle=tkinter.Button(text="Temizle",command=temizle, font="Arial 10", width=10, height=2)
            temizle.pack(padx=10,pady=30)

            label = tkinter.Label(text="Hızlı Giriş", font="Arial 10")
            label.pack(anchor="w")

            youtube = tkinter.Button(text="youtube", font="Arial 10", width=8, height=2,
                                     command=lambda: callback("https://youtube.com"))
            youtube.pack(anchor="w", pady=10)

            instagram = tkinter.Button(text="instagram", font="Arial 10", width=8, height=2,
                                       command=lambda: callback("https://instagram.com"))
            instagram.pack(anchor="w", pady=10)

            twitter = tkinter.Button(text="twitter", font="Arial 10", width=8, height=2,
                                     command=lambda: callback("https://twitter.com"))
            twitter.pack(anchor="w", pady=10)


            readme=tkinter.Button(text="Sayfa Kodları",command=readme)
            readme.pack()




        else:
            messagebox.showwarning("Uyarı",f"Girdiğiniz sifre: {girilen_sifre}. Lütfen doğru şifreyi giriniz.")


    giris_kutusu = tkinter.Toplevel(ekran)
    giris_kutusu.geometry("200x200")
    giris_kutusu.title("Arama yapabilmek için giriş yap")

    # Giriş kutucuğunu oluşturun
    entry = tkinter.Entry(giris_kutusu,show="*")
    entry.pack(padx=30, pady=30)

    tamam_butonu = tkinter.Button(giris_kutusu, text="Tamam", command=tamam)
    tamam_butonu.pack(pady=5)

    giris_kutusu.transient(ekran)  # İletişim kutusunu ana pencereye bağla (isteğe bağlı)
    giris_kutusu.grab_set()  # İletişim kutusu açıkken diğer pencerelerdeki girişi engelle (isteğe bağlı)
    ekran.wait_window(giris_kutusu)  # İletişim kutusu kapatılana kadar ana pencereyi beklet



# Ana pencereyi oluşturun
ekran = tkinter.Tk()
ekran.geometry("600x600")
ekran.title("Arama Motoru")
ekran.configure(background="lightblue")



# Giriş şifresi düğmesini oluşturun
girisi_goster_butonu = tkinter.Button(ekran, text="Özel İletişim Kutusunu Göster", command=giris_sifresi())
girisi_goster_butonu.pack(pady=20)

ekran.mainloop()



"""
Entry (Giriş) Widget:
Entry (Giriş) widget'ı, tek satırlık metin girişi için kullanılır.
Bu widget, yalnızca bir satır metni işlemek üzere tasarlanmıştır 
ve bu nedenle get() metoduna herhangi bir pozisyonel argüman gerekmez.

get() metodu Text widget'ında iki pozisyonel argüman gerektirir: başlangıç dizini ve bitiş dizini.
Bu, Text widget'ının birden çok satır metni içerebilme özelliğinden kaynaklanır ve
metni almak için alınacak dizin aralığını belirtmeniz gerekmektedir. """