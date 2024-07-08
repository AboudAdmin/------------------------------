import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import requests
from bs4 import BeautifulSoup
import os

class SocialMediaSearchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("بحث عن حسابات وسائل التواصل الاجتماعي")
        self.geometry("800x600")
        self.configure(bg='#f0f0f0')

        # تحديد مسارات الصور
        image_paths = [
            r"C:\Users\abdallah\Downloads\request-social.png",
            r"C:\Users\abdallah\Downloads\clipart-hacker-hacker.png",
            r"C:\Users\abdallah\Downloads\hacker2.jpeg",
            r"C:\Users\abdallah\Downloads\hacker3.jpeg",
        ]
        
        self.images = []
        for path in image_paths:
            if os.path.exists(path):
                self.images.append(ImageTk.PhotoImage(Image.open(path).resize((100, 100))))
            else:
                messagebox.showerror("خطأ", f"لم يتم العثور على ملف الصورة: {path}")

        # إعداد التخطيط الرئيسي
        header_frame = tk.Frame(self, bg='#4caf50', bd=5)
        header_frame.pack(fill=tk.X)

        # إضافة الصور إلى واجهة المستخدم
        self.logo_label_left = tk.Label(header_frame, image=self.images[0], bg='#4caf50')
        self.logo_label_left.pack(side=tk.LEFT, padx=10)
        self.logo_label_right = tk.Label(header_frame, image=self.images[1], bg='#4caf50')
        self.logo_label_right.pack(side=tk.RIGHT, padx=10)

        self.title_label = tk.Label(header_frame, text="بحث عن حسابات وسائل التواصل الاجتماعي", font=("Arial", 18, "bold"), fg='white', bg='#4caf50')
        self.title_label.pack(side=tk.LEFT, padx=10, pady=10)

        # إضافة صور أخرى في الجانب السفلي من الإطار الرئيسي
        footer_frame = tk.Frame(self, bg='#f0f0f0')
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.logo_label_bottom_left = tk.Label(footer_frame, image=self.images[2], bg='#f0f0f0')
        self.logo_label_bottom_left.pack(side=tk.LEFT, padx=10)
        self.logo_label_bottom_right = tk.Label(footer_frame, image=self.images[3], bg='#f0f0f0')
        self.logo_label_bottom_right.pack(side=tk.RIGHT, padx=10)

        main_frame = tk.Frame(self, bg='#f0f0f0')
        main_frame.pack(pady=20)

        self.label_username = tk.Label(main_frame, text="اسم المستخدم:", font=("Arial", 14), bg='#f0f0f0')
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        
        self.entry_username = tk.Entry(main_frame, width=30, font=("Arial", 14))
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.search_button = tk.Button(main_frame, text="بحث", font=("Arial", 14, "bold"), bg='#4caf50', fg='white', command=self.search_accounts)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)

        self.result_label = tk.Label(main_frame, text="نتائج البحث:", font=("Arial", 14), bg='#f0f0f0')
        self.result_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.result_text = tk.Text(main_frame, height=10, width=50, wrap="word", font=("Arial", 12))
        self.result_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.result_text.yview)
        self.scrollbar.grid(row=2, column=3, sticky='ns')
        self.result_text.config(yscrollcommand=self.scrollbar.set)

    def find_social_media_accounts(self, username):
        social_media_accounts = []
        platforms = {
            "Facebook": f"https://www.facebook.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://www.instagram.com/{username}",
        }

        for platform, url in platforms.items():
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    if soup.title and username.lower() in soup.title.text.lower():
                        social_media_accounts.append((platform, url))
            except requests.RequestException as e:
                print(f"Error fetching {platform} data: {e}")

        return social_media_accounts

    def search_accounts(self):
        username = self.entry_username.get()
        accounts = self.find_social_media_accounts(username)
        self.result_text.delete('1.0', tk.END)
        if accounts:
            result = f"تم العثور على حسابات وسائل التواصل الاجتماعي للمستخدم '{username}':\n"
            for account in accounts:
                result += f"{account[0]}: {account[1]}\n"
            self.result_text.insert(tk.END, result)
        else:
            self.result_text.insert(tk.END, f"لا توجد حسابات وسائل التواصل الاجتماعي للمستخدم '{username}'.")

if __name__ == "__main__":
    app = SocialMediaSearchApp()
    app.mainloop()
