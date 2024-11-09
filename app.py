import threading
import customtkinter as ctk
import proxy
import smlwb

def toggle_connection():
    global connected
    connected = not connected
    if connected:
        proxy_address = '127.0.0.1'
        proxy_port = '4525'
        isOk = proxy.set_proxy(proxy_address, proxy_port)
        if not isOk:
            return
        threading.Thread(target=run_app).start()
        connect_button.configure(text="Disconnect", fg_color="blue")
    else:
        isOk = proxy.unset_proxy()
        if not isOk:
            return
        connect_button.configure(text="Connect", fg_color="SystemButtonFace")

def run_app():
    smlwb.runApp()

def close_app():
    smlwb.stop()

def on_closing():
    if connected:
        proxy.unset_proxy()
        close_app()
    root.destroy()
    root.quit()
    exit(0)

connected = False

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Youtube Gozar")
root.geometry("300x150")
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Escape>', lambda e: root.quit())

connect_button = ctk.CTkButton(root, text="Connect", command=toggle_connection, fg_color="blue", hover_color="darkblue")
connect_button.pack(pady=20)

root.mainloop()
