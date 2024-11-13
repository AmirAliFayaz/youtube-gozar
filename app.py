import threading
import tkinter as tk
import customtkinter as ctk
import socket
import proxy
import smlwb
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

connected = False

def toggle_connection():
    global connected
    try:
        connected = not connected
        
        if connected:
            proxy_address = '127.0.0.1'
            proxy_port = '4525'
            is_ok = proxy.set_proxy(proxy_address, proxy_port)
            logging.info(f"Proxy set result: {is_ok}")
            
            if not is_ok:
                logging.error("Failed to set proxy.")
                return

            threading.Thread(target=run_app, daemon=True).start()
            update_button("Disconnect", "white", "green")
            
        else:
            is_ok = proxy.unset_proxy()
            logging.info(f"Proxy unset result: {is_ok}")
            
            if not is_ok:
                logging.error("Failed to unset proxy.")
                return

            update_button("Connect", "black", "SystemButtonFace")
            
    except Exception as e:
        logging.error(f"Error in toggle_connection: {e}")


def run_app():
    smlwb.runApp()


def close_app():
    smlwb.stop()


def update_button(text, text_color, fg_color):
    connect_button.configure(text=text, text_color=text_color, fg_color=fg_color)


def on_closing():
    if connected:
        proxy.unset_proxy()
        close_app()
    root.quit()
    root.destroy()


connected = False

root = ctk.CTk()
root.title("Youtube Gozar")
root.wm_title("Youtube Gozar v1.0")
root.geometry("300x200")
root.resizable(0, 0)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Escape>', lambda e: root.quit())

connect_button = ctk.CTkButton(root, text="Connect", command=toggle_connection)
connect_button.pack(pady=20)

root.mainloop()
