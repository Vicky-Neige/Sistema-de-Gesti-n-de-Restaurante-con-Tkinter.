import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, master, servicio, usuario_actual, on_logout):
        super().__init__(master)
        self.master = master
        self.servicio = servicio
        self.usuario_actual = usuario_actual
        self.on_logout = on_logout

        self.master.title("Restaurante App - Menú Principal")
        self.master.geometry("620x450")

        self.crear_widgets()

    def crear_widgets(self):
        lbl_bienvenida = tk.Label(
            self, text=f"Panel Principal - Usuario: {self.usuario_actual.nombre} ({self.usuario_actual.rol})", 
            font=("Arial", 11, "bold")
        )
        lbl_bienvenida.pack(pady=10)

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        btn_prod = tk.Button(frame_botones, text="Productos", width=12, command=self.mostrar_productos)
        btn_prod.grid(row=0, column=0, padx=5)

        btn_usrs = tk.Button(frame_botones, text="Usuarios", width=12, command=self.mostrar_usuarios)
        btn_usrs.grid(row=0, column=1, padx=5)

        btn_ventas = tk.Button(frame_botones, text="Ventas", width=12, command=self.mostrar_ventas_pendiente)
        btn_ventas.grid(row=0, column=2, padx=5)

        btn_salir = tk.Button(frame_botones, text="Cerrar Sesión", width=12, bg="#dc3545", fg="white", command=self.cerrar_sesion)
        btn_salir.grid(row=0, column=3, padx=5)

        self.frame_contenido = tk.Frame(self)
        self.frame_contenido.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        self.pack(fill=tk.BOTH, expand=True)
        self.mostrar_productos()

    def limpiar_contenido(self):
        for widget in self.frame_contenido.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()
        lbl = tk.Label(self.frame_contenido, text="Productos Registrados", font=("Arial", 12, "bold"))
        lbl.pack(pady=5)

        columnas = ("id", "nombre", "precio", "categoria", "stock")
        tabla = ttk.Treeview(self.frame_contenido, columns=columnas, show="headings", height=8)
        
        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio ($)")
        tabla.heading("categoria", text="Categoría")
        tabla.heading("stock", text="Stock")

        tabla.column("id", width=40, anchor="center")
        tabla.column("nombre", width=180)
        tabla.column("precio", width=80, anchor="e")
        tabla.column("categoria", width=120)
        tabla.column("stock", width=60, anchor="center")

        productos = self.servicio.obtener_productos()
        for p in productos:
            tabla.insert("", tk.END, values=(p.id, p.nombre, f"{p.precio:.2f}", p.categoria, p.stock))

        tabla.pack(fill=tk.BOTH, expand=True)

    def mostrar_usuarios(self):
        self.limpiar_contenido()
        lbl = tk.Label(self.frame_contenido, text="Usuarios del Sistema", font=("Arial", 12, "bold"))
        lbl.pack(pady=5)

        columnas = ("id", "username", "nombre", "rol")
        tabla = ttk.Treeview(self.frame_contenido, columns=columnas, show="headings", height=8)
        
        tabla.heading("id", text="ID")
        tabla.heading("username", text="Usuario")
        tabla.heading("nombre", text="Nombre Completo")
        tabla.heading("rol", text="Rol")

        tabla.column("id", width=40, anchor="center")
        tabla.column("username", width=120)
        tabla.column("nombre", width=200)
        tabla.column("rol", width=100)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            tabla.insert("", tk.END, values=(u.id, u.username, u.nombre, u.rol))

        tabla.pack(fill=tk.BOTH, expand=True)

    def mostrar_ventas_pendiente(self):
        messagebox.showinfo("Módulo en Desarrollo", "El módulo de Ventas se incorporará en las próximas semanas.")

    def cerrar_sesion(self):
        self.destroy()
        self.on_logout()