import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext, messagebox, Menu
import socket
import threading
import subprocess
import time
import math
import sys
import os
import re
import json
import webbrowser
import platform
import importlib.util
from concurrent.futures import ThreadPoolExecutor

# --- DEPENDANCES ---
try:
    import psutil
    PSUTIL_AVAIL = True
except ImportError:
    PSUTIL_AVAIL = False

# --- IMPORT MAC DB ---
try:
    file_path = os.path.join(os.path.dirname(__file__), "addressemac.py")
    spec = importlib.util.spec_from_file_location("mac_db", file_path)
    mac_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mac_mod)
    MAC_DB = mac_mod.vendors
    DB_STATUS = f"MAC DB: {len(MAC_DB)} ENTRIES"
except:
    MAC_DB = {}
    DB_STATUS = "MAC DB: DEFAULT"

# --- CONFIGURATION ---
APP_TITLE = "NET.ADMIN // OPTIMIZED UI"
VER_STR = "v20.0-SPACE-SAVER"

C = {
    "bg": "#0a0a0a",       
    "panel": "#141414",    
    "header": "#1a1a1a",   
    "text": "#dddddd",     
    "dim": "#666666",      
    "accent": "#007acc",   
    "success": "#4caf50",  
    "danger": "#f44336",   
    "warn": "#ff9800",     
    "border": "#2a2a2a",   
    "scroll": "#333333"    
}

# Base de données Ports
PORTS_DATA = {
    20: ("FTP-DATA", "📁"), 21: ("FTP", "📁"), 22: ("SSH", "🔒"), 23: ("TELNET", "📠"),
    25: ("SMTP", "📧"), 53: ("DNS", "🌍"), 67: ("DHCP", "📡"), 69: ("TFTP", "📁"),
    80: ("HTTP", "🌐"), 110: ("POP3", "📧"), 123: ("NTP", "⏱️"), 135: ("RPC", "⚙️"),
    139: ("NETBIOS", "🖥️"), 143: ("IMAP", "📧"), 161: ("SNMP", "📊"), 389: ("LDAP", "📇"),
    443: ("HTTPS", "🔒"), 445: ("SMB", "📁"), 514: ("SYSLOG", "📝"), 636: ("LDAPS", "🔒"),
    873: ("RSYNC", "🔄"), 993: ("IMAPS", "📧"), 995: ("POP3S", "📧"), 1194: ("OPENVPN", "🛡️"),
    1433: ("MSSQL", "🗄️"), 1521: ("ORACLE", "🗄️"), 1723: ("PPTP", "🛡️"), 1883: ("MQTT", "📡"),
    2049: ("NFS", "📁"), 3306: ("MYSQL", "🐬"), 3389: ("RDP", "💻"), 5060: ("SIP", "📞"),
    5432: ("POSTGRES", "🐘"), 5900: ("VNC", "👀"), 5938: ("TEAMVIEWER", "↔️"), 6379: ("REDIS", "📦"),
    8000: ("HTTP-DEV", "🌐"), 8080: ("HTTP-ALT", "🌐"), 8443: ("HTTPS-ALT", "🔒"), 8888: ("HTTP-PROXY", "🌐"),
    9200: ("ELASTIC", "🔍"), 25565: ("MINECRAFT", "🎮"), 27015: ("STEAM", "🎮"), 27017: ("MONGODB", "🍃")
}

# --- GUI PRINCIPALE ---
class NetAdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1500x950")
        self.root.configure(bg=C["bg"])
        
        self.hosts = []
        self.host_details = {} 
        self.selected_ip = None
        self.local_ip = self.get_local_ip()
        self.anim_step = 0
        
        self.last_net = 0
        self.bars = {}
        if PSUTIL_AVAIL:
            try:
                io = psutil.net_io_counters()
                self.last_net = io.bytes_recv + io.bytes_sent
            except: pass

        self.setup_styles()
        self.setup_ui()
        
        self.log(f"[*] SYSTEM READY. {DB_STATUS}")
        self.log(f"[*] INTERFACE: {self.local_ip}")
        
        self.root.after(50, self.animate_visuals)
        self.root.after(1000, self.update_monitor)

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80)); i = s.getsockname()[0]; s.close()
            return i
        except: return "127.0.0.1"

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("Treeview", 
                        background=C["panel"], foreground=C["text"], 
                        fieldbackground=C["panel"], borderwidth=0, 
                        font=("Consolas", 10), rowheight=28)
        
        style.configure("Treeview.Heading", 
                        background=C["header"], foreground=C["accent"], 
                        relief="flat", font=("Segoe UI", 9, "bold"))
        
        style.map("Treeview", background=[('selected', "#222")], foreground=[('selected', C["accent"])])
        
        style.configure("Dark.Vertical.TScrollbar", gripcount=0,
                        background="#333", darkcolor=C["bg"], lightcolor=C["bg"], 
                        troughcolor=C["bg"], bordercolor=C["bg"], arrowcolor="white")
        
        style.configure("Thin.Horizontal.TProgressbar", 
                        troughcolor=C["bg"], background=C["accent"], 
                        thickness=6, borderwidth=0)

    def setup_ui(self):
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)

        # --- 1. HEADER ---
        header = tk.Frame(self.root, bg=C["header"], height=45)
        header.grid(row=0, column=0, columnspan=3, sticky="ew")
        header.pack_propagate(False)
        tk.Label(header, text="NET.ADMIN", bg=C["header"], fg="white", font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT, padx=15)
        tk.Label(header, text="// BLACKOPS", bg=C["header"], fg=C["dim"], font=("Segoe UI", 10, "bold")).pack(side=tk.LEFT)
        tk.Label(header, text=f"HOST: {self.local_ip}", bg=C["header"], fg=C["dim"], font=("Consolas", 10)).pack(side=tk.RIGHT, padx=15)

        # --- 2. SIDEBAR ---
        left_p = tk.Frame(self.root, bg=C["panel"], width=280)
        left_p.grid(row=1, column=0, rowspan=2, sticky="ns", padx=(0, 1))
        left_p.pack_propagate(False)
        
        btn_frame = tk.Frame(left_p, bg=C["panel"], pady=15)
        btn_frame.pack(fill=tk.X)
        tk.Button(btn_frame, text="SCAN NETWORK", bg=C["accent"], fg="white", font=("Segoe UI", 9, "bold"), 
                  relief="flat", pady=8, command=self.start_scan).pack(fill=tk.X, padx=15)
        
        tk.Label(left_p, text="TARGET LIST", bg=C["panel"], fg=C["dim"], font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=15, pady=5)
        list_frame = tk.Frame(left_p, bg=C["panel"])
        list_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)
        
        sb = ttk.Scrollbar(list_frame, orient="vertical", style="Dark.Vertical.TScrollbar")
        self.listbox = tk.Listbox(list_frame, bg="#111", fg="#ccc", font=("Consolas", 10), 
                                  borderwidth=0, selectbackground="#333", selectforeground="white",
                                  activestyle="none", yscrollcommand=sb.set)
        sb.config(command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.select_ip)

        # --- 3. CENTER PANEL (Main) ---
        center = tk.Frame(self.root, bg=C["bg"])
        center.grid(row=1, column=1, sticky="nsew")
        center.columnconfigure(0, weight=1)
        # La ligne 1 (Tableau) prend l'espace dispo, la ligne 3 (Map) a une taille fixe ou extensible
        center.rowconfigure(1, weight=1) 

        # ROW 0: Info Header (Compact)
        info_f = tk.Frame(center, bg=C["bg"], height=60)
        info_f.grid(row=0, column=0, sticky="ew")
        info_f.pack_propagate(False)
        
        # Titre IP
        self.lbl_targ = tk.Label(info_f, text="AWAITING ORDERS", bg=C["bg"], fg="white", font=("Segoe UI", 20, "bold"))
        self.lbl_targ.pack(side=tk.LEFT, padx=20, pady=10)
        # Infos Mac/Vendor
        self.lbl_vend = tk.Label(info_f, text="", bg=C["bg"], fg=C["dim"], font=("Consolas", 10))
        self.lbl_vend.pack(side=tk.LEFT, padx=10, pady=10)

        # ROW 1: Tableau des Ports (Plus haut, prend l'espace)
        table_f = tk.Frame(center, bg=C["bg"])
        table_f.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 5))
        
        cols = ("port", "icon", "service", "banner")
        self.tree = ttk.Treeview(table_f, columns=cols, show="headings")
        self.tree.heading("port", text="PORT", anchor="w"); self.tree.column("port", width=70)
        self.tree.heading("icon", text="", anchor="center"); self.tree.column("icon", width=30)
        self.tree.heading("service", text="SERVICE", anchor="w"); self.tree.column("service", width=150)
        self.tree.heading("banner", text="VERSION / INFO", anchor="w"); self.tree.column("banner", width=400)
        self.tree.tag_configure('open', foreground=C["success"])
        
        tsb = ttk.Scrollbar(table_f, orient="vertical", command=self.tree.yview, style="Dark.Vertical.TScrollbar")
        self.tree.configure(yscrollcommand=tsb.set)
        tsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.context_menu = Menu(self.root, tearoff=0, bg=C["panel"], fg="white", activebackground=C["accent"])
        self.context_menu.add_command(label="Open HTTP/HTTPS", command=self.open_browser)
        self.tree.bind("<Button-3>", self.show_context_menu)

        # ROW 2: Barre de progression (Entre Table et Map)
        self.progress = ttk.Progressbar(center, mode='determinate', style="Thin.Horizontal.TProgressbar")
        self.progress.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

        # ROW 3: Map (Agrandie)
        map_f = tk.Frame(center, bg=C["bg"], height=400)
        map_f.grid(row=3, column=0, sticky="ew", padx=20, pady=(5, 10))
        # Important: ne pas mettre propagate(False) si on veut qu'elle s'adapte, 
        # mais ici on veut forcer la hauteur
        map_f.pack_propagate(False) 
        
        tk.Label(map_f, text="TOPOLOGY RADAR", bg=C["bg"], fg=C["dim"], font=("Consolas", 8)).pack(anchor="nw")
        self.map = tk.Canvas(map_f, bg=C["panel"], highlightthickness=0, height=380)
        self.map.pack(fill=tk.BOTH, expand=True)
        self.map.bind("<Configure>", lambda e: self.draw_map())

        # --- 4. RIGHT PANEL ---
        right = tk.Frame(self.root, bg=C["panel"], width=320)
        right.grid(row=1, column=2, rowspan=2, sticky="ns", padx=(1, 0))
        right.pack_propagate(False)

        tk.Label(right, text="SYSTEM LOGS", bg=C["panel"], fg=C["dim"], font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=15, pady=(20, 5))
        log_f = tk.Frame(right, bg=C["panel"])
        log_f.pack(fill=tk.X, padx=15)
        lsb = ttk.Scrollbar(log_f, orient="vertical", style="Dark.Vertical.TScrollbar")
        self.term = scrolledtext.ScrolledText(log_f, bg="#111", fg=C["success"], font=("Consolas", 8), 
                                              relief="flat", height=25, state='disabled', yscrollcommand=lsb.set)
        lsb.config(command=self.term.yview)
        lsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.term.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        mon_f = tk.Frame(right, bg=C["panel"])
        mon_f.pack(side=tk.BOTTOM, fill=tk.X, padx=15, pady=30)
        tk.Label(mon_f, text="RESOURCES", bg=C["panel"], fg=C["danger"], font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 10))
        self.create_stat_bar(mon_f, "CPU LOAD", C["accent"])
        self.create_stat_bar(mon_f, "MEMORY", C["warn"])
        self.create_stat_bar(mon_f, "NET I/O", C["success"])

    def create_stat_bar(self, parent, title, color):
        f = tk.Frame(parent, bg=C["panel"]); f.pack(fill=tk.X, pady=5)
        h = tk.Frame(f, bg=C["panel"]); h.pack(fill=tk.X)
        tk.Label(h, text=title, bg=C["panel"], fg="#ccc", font=("Consolas", 8)).pack(side=tk.LEFT)
        l = tk.Label(h, text="0%", bg=C["panel"], fg=color, font=("Consolas", 8, "bold")); l.pack(side=tk.RIGHT)
        c = tk.Canvas(f, height=6, bg="#222", highlightthickness=0); c.pack(fill=tk.X, pady=2)
        b = c.create_rectangle(0, 0, 0, 6, fill=color, width=0)
        self.bars[title] = (c, b, l)

    def log(self, t):
        self.term.config(state='normal')
        self.term.insert(tk.END, f"> {t}\n"); self.term.see(tk.END)
        self.term.config(state='disabled')

    # --- LOGIQUE ---
    def open_browser(self):
        sel = self.tree.selection()
        if sel:
            vals = self.tree.item(sel[0])['values']
            if str(vals[0]) in ['80', '8080', '8000']: webbrowser.open(f"http://{self.selected_ip}:{vals[0]}")
            elif str(vals[0]) in ['443', '8443']: webbrowser.open(f"https://{self.selected_ip}:{vals[0]}")

    def show_context_menu(self, event):
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.post(event.x_root, event.y_root)

    def start_scan(self):
        self.hosts = [self.local_ip]
        self.host_details = {self.local_ip: {"mac": "HOST", "ven": "Localhost"}}
        self.listbox.delete(0, tk.END)
        self.log("Initializing ARP Sweep...")
        threading.Thread(target=self.run_discovery, daemon=True).start()

    def run_discovery(self):
        base = ".".join(self.local_ip.split(".")[:3]) + "."
        def ping(i):
            try:
                si = subprocess.STARTUPINFO(); si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                subprocess.call(['ping', '-n', '1', '-w', '50', f"{base}{i}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=si)
            except: pass
        with ThreadPoolExecutor(max_workers=50) as ex: ex.map(ping, range(1, 255))
        try:
            out = subprocess.check_output(['arp', '-a']).decode(errors='ignore')
            for line in out.splitlines():
                m = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+([0-9a-fA-F:-]{17})', line)
                if m:
                    ip, mac = m.groups(); mac = mac.replace(":", "-").upper()
                    if ip not in self.hosts and not ip.startswith("224."):
                        self.hosts.append(ip)
                        ven = MAC_DB.get(mac[:8], "Unknown")
                        self.host_details[ip] = {"mac": mac, "ven": ven}
        except: pass
        self.root.after(0, self.update_host_list)

    def update_host_list(self):
        for h in self.hosts: self.listbox.insert(tk.END, h)
        self.log(f"Scan Finished: {len(self.hosts)} devices.")

    def select_ip(self, e):
        s = self.listbox.curselection()
        if not s: return
        ip = self.listbox.get(s[0]); self.selected_ip = ip
        info = self.host_details.get(ip, {"mac":"?", "ven":"?"})
        self.lbl_targ.config(text=f"{ip}")
        self.lbl_vend.config(text=f"MAC: {info['mac']}  |  VENDOR: {info['ven']}")
        for i in self.tree.get_children(): self.tree.delete(i)
        threading.Thread(target=self.scan_ports_auto, args=(ip,), daemon=True).start()

    def scan_ports_auto(self, ip):
        self.log(f"Scanning ports on {ip}...")
        self.root.after(0, lambda: self.progress.config(value=0))
        completed = 0; total = len(PORTS_DATA)
        def check(port):
            nonlocal completed
            res = None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.4)
                if s.connect_ex((ip, port)) == 0:
                    banner = "Open"
                    try:
                        if port in [80, 8080]: s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                        else: s.send(b"\r\n")
                        b = s.recv(1024).decode(errors='ignore').strip()
                        if b: banner = b[:50]
                    except: pass
                    res = (port, banner)
                s.close()
            except: pass
            completed += 1
            self.root.after(0, lambda: self.progress.config(value=(completed/total)*100))
            return res
        with ThreadPoolExecutor(max_workers=30) as ex: results = list(ex.map(check, PORTS_DATA.keys()))
        valid = [r for r in results if r]
        self.root.after(0, lambda: self.update_table(ip, valid))

    def update_table(self, ip, results):
        if self.selected_ip != ip: return
        results.sort(key=lambda x: x[0])
        if not results: self.tree.insert("", "end", values=("N/A", "", "No open ports", ""))
        else:
            for p, ban in results:
                info = PORTS_DATA.get(p, ("UNK", "❓"))
                self.tree.insert("", "end", values=(p, info[1], info[0], ban), tags=('open',))
        self.log(f"Found {len(results)} open ports.")

    # --- ANIMATIONS ---
    def animate_visuals(self):
        self.draw_map(); self.anim_step += 0.05
        self.root.after(100, self.animate_visuals)

    def update_monitor(self):
        if PSUTIL_AVAIL and self.bars:
            try:
                self.update_bar("CPU LOAD", psutil.cpu_percent())
                self.update_bar("MEMORY", psutil.virtual_memory().percent)
                io = psutil.net_io_counters(); curr = io.bytes_recv + io.bytes_sent
                delta = curr - self.last_net; self.last_net = curr
                spd = delta / 1.5; pct = min((spd/1000000)*100, 100)
                self.update_bar("NET I/O", pct)
            except: pass
        self.root.after(1500, self.update_monitor)

    def update_bar(self, t, v):
        if t in self.bars:
            c, b, l = self.bars[t]; l.config(text=f"{int(v)}%")
            w = c.winfo_width()
            if w > 1: c.coords(b, 0, 0, (v/100)*w, 6)

    def draw_map(self):
        self.map.delete("all")
        w, h = self.map.winfo_width(), self.map.winfo_height()
        if w < 10: return
        cx, cy = w/2, h/2
        for r in range(40, int(min(w,h)/2), 50): self.map.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#222")
        lx = cx + (min(w,h)/2) * math.cos(self.anim_step); ly = cy + (min(w,h)/2) * math.sin(self.anim_step)
        self.map.create_line(cx, cy, lx, ly, fill="#333", width=2)
        self.map.create_oval(cx-5, cy-5, cx+5, cy+5, fill=C["accent"], outline="white")
        nodes = [h for h in self.hosts if h != self.local_ip]
        if not nodes: return
        rad = min(w, h)/2.5
        for i, node in enumerate(nodes):
            ang = (2*math.pi/len(nodes))*i; x = cx + rad * math.cos(ang); y = cy + rad * math.sin(ang)
            col = "white" if node==self.selected_ip else "#444"
            self.map.create_line(cx, cy, x, y, fill=col)
            fill = C["success"] if node==self.selected_ip else C["danger"]
            self.map.create_oval(x-4, y-4, x+4, y+4, fill=fill, outline="black")
            self.map.create_text(x, y+15, text=node, fill="gray", font=("Arial", 8))

if __name__ == "__main__":
    root = tk.Tk()
    app = NetAdminGUI(root)
    root.mainloop()