import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, servicio, on_login_success):
        super().__init__(master)
        self.master = master
        self.servicio = servicio
        self.on_login_success = on_login_success
        
        self.master.title("Restaurante App - Autenticación")
        self.master.geometry("380x320")
        
        self.crear_widgets()

    def crear_widgets(self):
        lbl_titulo = tk.Label(self, text="RESTAURANTE APP", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=15)

        lbl_sub = tk.Label(self, text="Ingrese sus credenciales para acceder")
        lbl_sub.pack(pady=5)

        lbl_user = tk.Label(self, text="Usuario:")
        lbl_user.pack(pady=(10, 2))
        self.txt_usuario = tk.Entry(self, width=25)
        self.txt_usuario.pack(pady=2)

        lbl_pass = tk.Label(self, text="Contraseña:")
        lbl_pass.pack(pady=(10, 2))
        self.txt_password = tk.Entry(self, show="*", width=25)
        self.txt_password.pack(pady=2)

        btn_ingresar = tk.Button(
            self, text="INICIAR SESIÓN", bg="#124fc0", fg="white", 
            font=("Arial", 10, "bold"), command=self.ejecutar_login
        )
        btn_ingresar.pack(pady=20)

        self.pack(expand=True)

    def ejecutar_login(self):
        usuario_val = self.txt_usuario.get().strip()
        clave_val = self.txt_password.get().strip()

        if not usuario_val or not clave_val:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return

        usuario_autenticado = self.servicio.validar_acceso(usuario_val, clave_val)

        if usuario_autenticado:
            messagebox.showinfo("Éxito", f"¡Bienvenido, {usuario_autenticado.nombre}!")
            self.destroy()
            self.on_login_success(usuario_autenticado)
        else:
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")