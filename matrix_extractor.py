import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup
import csv
import json
import threading
import time
import os
import random

# --- MATRIX COLOR PALETTE ---
COLORS = {
    "bg": "#000000",        
    "panel": "#0a0a0a",     
    "input_bg": "#1a1a1a",  
    "input_fg": "#00ff41",  
    "accent": "#00ff41",    
    "dim_text": "#008f11",  
    "text": "#e0ffe0",      
    "danger": "#ff0000",
    "warning": "#ffaa00"
}

FONT_MAIN = "Consolas"
FONT_UI = "Segoe UI"

# --- MATRIX RAIN ANIMATION ---
class DigitalRain(tk.Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, highlightthickness=0, bg="black", **kwargs)
        self.active = True
        self.drops = []
        self.chars = ["0", "1", "ア", "イ", "ウ", "エ", "オ", "カ", "キ", "ク", "ケ", "コ"]
        self.bind("<Configure>", self.on_resize)
        self.after(100, self.animate)

    def on_resize(self, event):
        self.delete("all")
        self.drops = []
        columns = max(1, int(event.width / 15))
        for i in range(columns):
            self.drops.append({
                'x': i * 15, 
                'y': random.randint(-500, 0), 
                'speed': random.randint(4, 10),
                'trail': []
            })

    def animate(self):
        if not self.active:
            return
            
        self.delete("rain")
        width = self.winfo_width()
        height = self.winfo_height()
        
        if width <= 1 or height <= 1:
            self.after(50, self.animate)
            return
            
        for d in self.drops:
            d['y'] += d['speed']
            if d['y'] > height + 20:
                d['y'] = random.randint(-50, -20)
                d['x'] = random.randint(0, width // 15) * 15
            
            # Parlak baş karakter
            self.create_text(d['x'], d['y'], text=random.choice(self.chars), 
                           fill=COLORS["accent"], font=(FONT_MAIN, 12, "bold"), tags="rain")
            
            # İz efekti
            for i in range(1, 8):
                y_pos = d['y'] - i * 15
                if y_pos > 0:
                    opacity = hex(int(255 * (1 - i/8)))[2:].zfill(2)
                    color = f"#00{opacity}00"
                    self.create_text(d['x'], y_pos, text=random.choice(self.chars),
                                   fill=color, font=(FONT_MAIN, 10), tags="rain")
        
        self.after(40, self.animate)

# --- GLITCH TEXT EFFECT ---
class GlitchLabel(tk.Label):
    def __init__(self, parent, original_text="", **kwargs):
        super().__init__(parent, **kwargs)
        self.original_text = original_text
        self.config(text=original_text)
        self.glitching = False
        
    def start_glitch(self):
        if not self.glitching:
            self.glitching = True
            self.glitch_animation()
    
    def glitch_animation(self, count=0):
        if not self.glitching or count > 8:
            self.config(text=self.original_text)
            self.glitching = False
            return
        
        if count % 2 == 0:
            glitch_chars = ['█', '▓', '▒', '░', '▀', '▄']
            glitched = ''.join(random.choice([c, random.choice(glitch_chars)]) 
                              for c in self.original_text)
            self.config(text=glitched)
        else:
            self.config(text=self.original_text)
        
        self.after(50, lambda: self.glitch_animation(count + 1))

# --- MAIN APPLICATION ---
class MatrixScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.geometry("900x600")
        self.root.configure(bg="black")
        
        # Center window
        self.center_window()
        
        # Background Layer - Matrix Rain
        self.bg_canvas = DigitalRain(root)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.setup_title_bar()
        self.setup_ui()
        
        # Typing effect for initial log
        self.type_initial_message()

    def center_window(self):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - 900) // 2
        y = (sh - 600) // 2
        self.root.geometry(f"900x600+{x}+{y}")

    def setup_title_bar(self):
        bar = tk.Frame(self.root, bg="#000000", height=40, bd=0)
        bar.pack(fill="x", side="top")
        bar.bind("<Button-1>", self.start_move)
        bar.bind("<B1-Motion>", self.do_move)
        
        # Animated title
        self.title_label = GlitchLabel(bar, original_text="▌ MATRIX_BACKLOGGD_EXTRACTOR // V2.0", 
                                       font=(FONT_MAIN, 11, "bold"),
                                       bg="#000000", fg=COLORS["accent"])
        self.title_label.pack(side="left", padx=20, pady=8)
        
        # Close button with hover effect
        self.close_btn = tk.Button(bar, text="[ X ]", command=self.close_app,
                                   bg="#000000", fg=COLORS["dim_text"], bd=0, 
                                   font=(FONT_MAIN, 12, "bold"),
                                   activebackground=COLORS["danger"], 
                                   activeforeground="white",
                                   cursor="hand2")
        self.close_btn.pack(side="right", padx=15)
        self.close_btn.bind("<Enter>", lambda e: self.close_btn.config(fg=COLORS["danger"], text="[ ✕ ]"))
        self.close_btn.bind("<Leave>", lambda e: self.close_btn.config(fg=COLORS["dim_text"], text="[ X ]"))

    def setup_ui(self):
        # Main container with semi-transparency effect
        main_container = tk.Frame(self.root, bg="#000000")
        main_container.pack(fill="both", expand=True, padx=15, pady=10)

        # === LEFT PANEL ===
        left_panel = tk.Frame(main_container, bg="#050505", bd=1, relief="solid")
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 8))
        
        # Header with animation trigger
        header = tk.Frame(left_panel, bg="#050505")
        header.pack(fill="x", padx=20, pady=(15, 10))
        
        self.panel_title = GlitchLabel(header, original_text=">> CONTROL_PANEL", 
                                       font=(FONT_MAIN, 12, "bold"),
                                       bg="#050505", fg=COLORS["accent"])
        self.panel_title.pack(anchor="w")
        
        # Input section
        input_frame = tk.Frame(left_panel, bg="#050505")
        input_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.create_input(input_frame, "TARGET_USER", "hayatim_yok")
        self.create_input(input_frame, "OUTPUT_FILE", "matrix_dump")
        
        # Format selector
        tk.Label(input_frame, text="EXPORT_FORMAT", font=(FONT_MAIN, 9), 
                bg="#050505", fg=COLORS["dim_text"]).pack(anchor="w", pady=(15, 5))
        
        fmt_frame = tk.Frame(input_frame, bg="#050505")
        fmt_frame.pack(fill="x", pady=5)
        
        self.format_var = tk.StringVar(value="CSV")
        for fmt in ["CSV", "JSON", "TXT"]:
            btn = tk.Radiobutton(fmt_frame, text=f"[ {fmt} ]", 
                               variable=self.format_var, value=fmt,
                               bg="#050505", fg=COLORS["accent"], 
                               selectcolor="#000000",
                               activebackground="#050505", 
                               activeforeground=COLORS["text"],
                               font=(FONT_MAIN, 10, "bold"), 
                               indicatoron=0, bd=1, relief="solid",
                               padx=15, pady=6, cursor="hand2")
            btn.pack(side="left", padx=(0, 8))
            btn.bind("<Enter>", lambda e, b=btn: b.config(fg=COLORS["text"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(fg=COLORS["accent"]))
        
        # Destination
        tk.Label(input_frame, text="DESTINATION_PATH", font=(FONT_MAIN, 9),
                bg="#050505", fg=COLORS["dim_text"]).pack(anchor="w", pady=(15, 5))
        
        path_frame = tk.Frame(input_frame, bg="#050505")
        path_frame.pack(fill="x")
        
        self.path_var = tk.StringVar(value=os.path.join(os.path.expanduser("~"), "Desktop"))
        
        path_btn = tk.Button(path_frame, textvariable=self.path_var, 
                            command=self.select_folder,
                            bg=COLORS["input_bg"], fg=COLORS["accent"], 
                            relief="flat", anchor="w", padx=12, font=(FONT_MAIN, 9),
                            cursor="hand2")
        path_btn.pack(fill="x", ipady=10)
        path_btn.bind("<Enter>", lambda e: path_btn.config(bg="#252525"))
        path_btn.bind("<Leave>", lambda e: path_btn.config(bg=COLORS["input_bg"]))
        
        # Execute button
        self.btn_start = tk.Button(left_panel, text="[ ▶ EXECUTE_SEQUENCE ]", 
                                   font=(FONT_MAIN, 13, "bold"),
                                   bg="#000000", fg=COLORS["accent"], 
                                   relief="solid", bd=2,
                                   command=self.start_process,
                                   cursor="hand2",
                                   activebackground=COLORS["accent"],
                                   activeforeground="#000000")
        self.btn_start.pack(side="bottom", fill="x", ipady=14, padx=20, pady=20)
        self.btn_start.bind("<Enter>", lambda e: self.btn_start.config(bg=COLORS["accent"], fg="#000000"))
        self.btn_start.bind("<Leave>", lambda e: self.btn_start.config(bg="#000000", fg=COLORS["accent"]))

        # === RIGHT PANEL ===
        right_panel = tk.Frame(main_container, bg="#050505", bd=1, relief="solid")
        right_panel.pack(side="right", fill="both", expand=True)
        
        # Monitor header
        tk.Label(right_panel, text=">> LIVE_MONITOR", font=(FONT_MAIN, 12, "bold"),
                bg="#050505", fg=COLORS["accent"]).pack(anchor="w", padx=20, pady=(15, 10))
        
        # Status display
        monitor_frame = tk.Frame(right_panel, bg="#0a0a0a", bd=1, relief="solid")
        monitor_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        status_inner = tk.Frame(monitor_frame, bg="#000000")
        status_inner.pack(fill="both", expand=True, padx=2, pady=2)
        
        self.lbl_game = tk.Label(status_inner, text="SYSTEM_READY", 
                                font=(FONT_MAIN, 10), bg="#000000", 
                                fg=COLORS["text"], anchor="w", padx=15, pady=8)
        self.lbl_game.pack(fill="x")
        
        self.lbl_stat = tk.Label(status_inner, text="--:--", 
                               font=(FONT_MAIN, 22, "bold"), bg="#000000",
                               fg=COLORS["accent"], anchor="center", pady=5)
        self.lbl_stat.pack(fill="x")
        
        # Log terminal
        tk.Label(right_panel, text=">> CONSOLE_LOG", font=(FONT_MAIN, 10, "bold"),
                bg="#050505", fg=COLORS["dim_text"]).pack(anchor="w", padx=20, pady=(5, 5))
        
        log_container = tk.Frame(right_panel, bg=COLORS["accent"], bd=1)
        log_container.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        self.log_area = scrolledtext.ScrolledText(log_container, bg="#000000", 
                                                 fg=COLORS["accent"],
                                                 font=(FONT_MAIN, 9), relief="flat",
                                                 insertbackground=COLORS["accent"],
                                                 wrap="word")
        self.log_area.pack(fill="both", expand=True, padx=1, pady=1)
        self.log_area.config(state="disabled")
        
        # Footer
        tk.Label(right_panel, text="[ CRAFTED_BY:_hayatim_yok ]", 
                font=(FONT_MAIN, 8), bg="#050505", fg="#1a1a1a").pack(side="bottom", pady=10)

    def create_input(self, parent, label, default=""):
        tk.Label(parent, text=label, font=(FONT_MAIN, 9), 
                bg="#050505", fg=COLORS["dim_text"]).pack(anchor="w", pady=(10, 5))
        
        entry = tk.Entry(parent, font=(FONT_MAIN, 11), bg=COLORS["input_bg"], 
                        fg=COLORS["text"], relief="flat", 
                        insertbackground=COLORS["accent"], bd=0)
        entry.pack(fill="x", ipady=10)
        entry.insert(0, default)
        
        # Focus effects
        entry.bind("<FocusIn>", lambda e: entry.config(bg="#252525"))
        entry.bind("<FocusOut>", lambda e: entry.config(bg=COLORS["input_bg"]))
        
        setattr(self, f"entry_{label.lower()}", entry)

    def type_initial_message(self):
        """Types initial message character by character"""
        messages = [
            "> INITIALIZING_SYSTEM...",
            "> LOADING_MATRIX_PROTOCOLS...",
            "> CONNECTION_ESTABLISHED",
            "> READY_FOR_DATA_EXTRACTION",
            ""
        ]
        self.type_messages(messages, 0)
    
    def type_messages(self, messages, index):
        if index >= len(messages):
            return
        
        message = messages[index]
        self.type_message(message, 0, lambda: self.type_messages(messages, index + 1))
    
    def type_message(self, message, char_index, callback):
        if char_index <= len(message):
            self.log_area.config(state="normal")
            self.log_area.insert(tk.END, message[char_index-1:char_index])
            if char_index == len(message):
                self.log_area.insert(tk.END, "\n")
            self.log_area.see(tk.END)
            self.log_area.config(state="disabled")
            self.root.after(30, lambda: self.type_message(message, char_index + 1, callback))
        else:
            callback()

    def log(self, msg, msg_type="info"):
        """Enhanced logging with color coding"""
        self.log_area.config(state="normal")
        
        color = COLORS["accent"]
        if msg_type == "error":
            color = COLORS["danger"]
        elif msg_type == "warning":
            color = COLORS["warning"]
        elif msg_type == "success":
            color = "#00ff00"
        
        tag = f"tag_{msg_type}"
        self.log_area.tag_config(tag, foreground=color)
        
        timestamp = time.strftime("%H:%M:%S")
        self.log_area.insert(tk.END, f"[{timestamp}] > {msg}\n", tag)
        self.log_area.see(tk.END)
        self.log_area.config(state="disabled")

    # Window dragging
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def close_app(self):
        self.bg_canvas.active = False
        self.root.destroy()

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.path_var.set(folder)
            self.log(f"DESTINATION_UPDATED: {folder}", "info")

    def start_process(self):
        user = self.entry_target_user.get().strip()
        if not user:
            self.log("ERROR: TARGET_USER_REQUIRED", "error")
            messagebox.showerror("ERROR", "Target user cannot be empty!")
            return
        
        self.panel_title.start_glitch()
        self.title_label.start_glitch()
        
        self.btn_start.config(state="disabled", text="[ ⏳ PROCESSING... ]")
        threading.Thread(target=self.scrape, args=(user,), daemon=True).start()

    def scrape(self, username):
        fname = self.entry_output_file.get().strip()
        fmt = self.format_var.get().lower()
        path = self.path_var.get()
        
        if not fname:
            fname = f"matrix_dump_{int(time.time())}"
        
        if not fname.endswith(f".{fmt}"):
            fname += f".{fmt}"
        
        full_path = os.path.join(path, fname)
        
        self.log(f"INITIATING_EXTRACTION: {username}", "info")
        self.log(f"TARGET_FORMAT: {fmt.upper()}", "info")
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        games = []
        prev_page = []
        page = 1
        
        while True:
            self.lbl_stat.config(text=f"PAGE:{page}")
            
            try:
                url = f"https://www.backloggd.com/u/{username}/games?page={page}"
                response = requests.get(url, headers=headers, timeout=10)
                
                if response.status_code != 200:
                    self.log(f"CONNECTION_FAILED: STATUS_{response.status_code}", "error")
                    break
                
                soup = BeautifulSoup(response.text, "html.parser")
                cards = soup.find_all("div", class_="card")
                
                if not cards:
                    self.log("NO_MORE_DATA_FOUND", "warning")
                    break
                
                current_page = []
                page_data = []
                
                for card in cards:
                    img = card.find("img")
                    if not img:
                        continue
                    
                    name = img.get("alt", "UNKNOWN")
                    rating_raw = card.get("data-rating")
                    rating = "N/A"
                    
                    if rating_raw:
                        try:
                            val = int(rating_raw) / 2
                            rating = f"{int(val)}/5" if val.is_integer() else f"{val}/5"
                        except:
                            pass
                    
                    # Update live monitor
                    display_name = name[:35] + "..." if len(name) > 35 else name
                    self.lbl_game.config(text=f"EXTRACTING: {display_name}")
                    self.lbl_stat.config(text=rating)
                    
                    current_page.append(name)
                    page_data.append({"name": name, "rating": rating})
                
                if current_page == prev_page:
                    self.log("DUPLICATE_PAGE_DETECTED", "warning")
                    break
                
                games.extend(page_data)
                prev_page = current_page
                
                self.log(f"PACKET_{page}_SECURED: +{len(page_data)}_ENTRIES", "success")
                page += 1
                time.sleep(0.4)
                
            except Exception as e:
                self.log(f"EXCEPTION: {str(e)}", "error")
                break
        
        # Save data
        self.lbl_game.config(text="WRITING_TO_DISK...")
        self.lbl_stat.config(text="⌛")
        
        try:
            with open(full_path, "w", newline="", encoding="utf-8-sig") as file:
                if fmt == "csv":
                    writer = csv.writer(file)
                    writer.writerow(["Game", "Rating"])
                    for game in games:
                        writer.writerow([game["name"], game["rating"]])
                elif fmt == "json":
                    json.dump(games, file, indent=4, ensure_ascii=False)
                else:  # TXT
                    for game in games:
                        file.write(f"{game['name']} - {game['rating']}\n")
            
            self.log(f"OPERATION_COMPLETE: {len(games)}_ENTRIES_SAVED", "success")
            self.lbl_game.config(text="EXTRACTION_COMPLETE")
            self.lbl_stat.config(text=f"✓ {len(games)}")
            
            messagebox.showinfo("SUCCESS", 
                              f"Data extraction complete!\n\n"
                              f"Total games: {len(games)}\n"
                              f"Saved to: {full_path}")
        except Exception as e:
            self.log(f"WRITE_ERROR: {str(e)}", "error")
            messagebox.showerror("ERROR", f"Failed to save file:\n{str(e)}")
        
        self.btn_start.config(state="normal", text="[ ▶ EXECUTE_SEQUENCE ]")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixScraperApp(root)
    root.mainloop()