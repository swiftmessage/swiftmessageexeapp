import webview

# URL
url = "https://your_url"

# create web app
window = webview.create_window("Messenger", url, width=800, height=600)

# Запускаем окно
webview.start()
