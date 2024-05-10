import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap
import requests
from bs4 import BeautifulSoup

class SocialMediaSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("بحث عن حسابات وسائل التواصل الاجتماعي")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        header_layout = QHBoxLayout()
        layout.addLayout(header_layout)

        self.logo_label = QLabel()
        pixmap = QPixmap('social_media_logo.png')  # تحتاج لتغيير الاسم إلى اسم صورة وسائل التواصل الاجتماعي الخاصة بك
        self.logo_label.setPixmap(pixmap)
        self.logo_label.setScaledContents(True)
        header_layout.addWidget(self.logo_label)

        self.title_label = QLabel("بحث عن حسابات وسائل التواصل الاجتماعي")
        header_layout.addWidget(self.title_label)

        self.label_username = QLabel("اسم المستخدم:")
        layout.addWidget(self.label_username)
        
        self.entry_username = QLineEdit()
        layout.addWidget(self.entry_username)

        self.search_button = QPushButton("بحث")
        self.search_button.clicked.connect(self.search_accounts)
        layout.addWidget(self.search_button)

        self.result_label = QLabel("نتائج البحث:")
        layout.addWidget(self.result_label)

        self.result_text = QLabel()
        layout.addWidget(self.result_text)

    def find_social_media_accounts(self, username):
        social_media_accounts = []
        urls = {
            "Facebook": f"https://www.facebook.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://www.instagram.com/{username}",
            # يمكنك إضافة المزيد من الروابط هنا حسب الحاجة
        }

        for site, url in urls.items():
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                if soup.title and username.lower() in soup.title.text.lower():
                    social_media_accounts.append((site, url))

        return social_media_accounts

    def search_accounts(self):
        username = self.entry_username.text()
        accounts = self.find_social_media_accounts(username)
        if accounts:
            result = f"تم العثور على حسابات وسائل التواصل الاجتماعي للمستخدم '{username}':<br>"
            for account in accounts:
                result += f"<a href='{account[1]}'>{account[0]}</a><br>"
            self.result_text.setText(result)
        else:
            self.result_text.setText(f"لا توجد حسابات وسائل التواصل الاجتماعي للمستخدم '{username}'.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SocialMediaSearchApp()
    window.show()
    sys.exit(app.exec_())





