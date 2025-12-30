import customtkinter as ctk
import random

# --- CONFIGURATION ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class StylishQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("CodeAlpha Cyber Training - Task 2")
        self.geometry("900x700")
        self.resizable(False, False)
        
        # Modern Cyberpunk Colors
        self.col_bg = "#0F172A"      # Dark Navy
        self.col_card = "#1E293B"    # Slate Card
        self.col_accent = "#00E5FF"  # Neon Cyan
        self.col_wrong = "#FF2E63"   # Neon Red
        self.col_correct = "#00E676" # Neon Green
        self.col_text = "#ECEFF1"    # Cool White
        self.col_muted = "#64748B"   # Grey Text

        self.configure(fg_color=self.col_bg)

        # ==========================================
        # LARGE QUESTION POOL (25 Questions)
        # ==========================================
        self.large_question_pool = [
            {"q": "You receive an email from 'Netflix' asking to update payment info. The sender is 'support@netflix-verify.net'.", "options": ["Update immediately", "Mark as Phishing", "Click the link", "Reply to ask if real"], "answer": "Mark as Phishing", "exp": "Real companies don't use domains like 'netflix-verify.net'."},
            {"q": "A co-worker calls asking for your password to 'fix a server issue'.", "options": ["Give the password", "Hang up & verify", "Email it instead", "Change password"], "answer": "Hang up & verify", "exp": "Tech support will NEVER ask for your password."},
            {"q": "What does the 's' in HTTPS stand for?", "options": ["Standard", "Secure", "Super", "System"], "answer": "Secure", "exp": "It means traffic is encrypted, but the site could still be fake!"},
            {"q": "Which of these is a 'Smishing' attack?", "options": ["Fake Email", "Fake SMS/Text", "Fake QR Code", "Fake Voicemail"], "answer": "Fake SMS/Text", "exp": "Smishing = SMS Phishing."},
            {"q": "You find a USB drive in the parking lot labeled 'Salary Bonuses'.", "options": ["Plug it in", "Destroy it", "Give to IT Security", "Check files at home"], "answer": "Give to IT Security", "exp": "This is a 'Baiting' attack to install malware."},
            {"q": "What is the best way to stop hackers even if they have your password?", "options": ["Long passwords", "MFA (2FA)", "Incognito Mode", "Clearing History"], "answer": "MFA (2FA)", "exp": "Multi-Factor Authentication blocks 99.9% of hacks."},
            {"q": "A website forces a popup saying 'Your PC is infected! Call this number'.", "options": ["Call the number", "Download the tool", "Close the browser", "Pay the fee"], "answer": "Close the browser", "exp": "This is scareware. Microsoft/Apple will never pop up asking you to call."},
            {"q": "You see a URL 'http://www.paypa1.com'. What is this called?", "options": ["Typosquatting", "SQL Injection", "DDoS", "Ransomware"], "answer": "Typosquatting", "exp": "Attackers lookalike domains (using '1' instead of 'l') to trick users."},
            {"q": "An email arrives with the subject: 'URGENT: INVOICE OVERDUE - ACT NOW'.", "options": ["Pay immediately", "Inspect sender details", "Forward to boss", "Ignore it"], "answer": "Inspect sender details", "exp": "Phishers use urgency and fear to make you skip verification."},
            {"q": "What is 'Quishing'?", "options": ["Quick Phishing", "QR Code Phishing", "Quality Phishing", "Quiet Phishing"], "answer": "QR Code Phishing", "exp": "Malicious QR codes can direct you to fake websites."},
            {"q": "A 'CEO' emails you from a personal Gmail account asking for a wire transfer.", "options": ["Send the money", "Reply asking why", "Verify via phone call", "Ignore"], "answer": "Verify via phone call", "exp": "This is Business Email Compromise (BEC). Always verify financial requests."},
            {"q": "Which file extension is most dangerous in an unknown email attachment?", "options": [".txt", ".jpg", ".exe", ".pdf"], "answer": ".exe", "exp": "Executable (.exe) files can install malware immediately upon clicking."},
            {"q": "You receive a LinkedIn message from a recruiter sending a link to a 'Job Description'.", "options": ["Click the link", "Check their profile first", "Download the file", "Share your resume"], "answer": "Check their profile first", "exp": "Attackers create fake profiles to deliver malware via links."},
            {"q": "Public Wi-Fi (like in a cafe) is generally...", "options": ["Safe for banking", "Encrypted by default", "Unsafe for sensitive data", "Faster than home Wi-Fi"], "answer": "Unsafe for sensitive data", "exp": "Hackers can easily intercept data on open, public Wi-Fi networks."},
            {"q": "What is 'Pretexting'?", "options": ["Guessing passwords", "Creating a fake scenario", "Hacking Wi-Fi", "Sending spam"], "answer": "Creating a fake scenario", "exp": "Pretexting involves inventing a story (lie) to get information."},
            {"q": "Legitimate organizations will usually address you by...", "options": ["'Dear Customer'", "'Dear Member'", "Your Name", "'Hello User'"], "answer": "Your Name", "exp": "Phishing emails use generic greetings because they don't know who you are."},
            {"q": "Hovering your mouse over a link allows you to...", "options": ["Scan for viruses", "See the actual URL", "Block the sender", "Encrypt the email"], "answer": "See the actual URL", "exp": "Always check where a link goes before clicking it."},
            {"q": "Enabling 'Macros' in a Word document from an email is...", "options": ["Safe", "Necessary to read", "Highly Dangerous", "Standard procedure"], "answer": "Highly Dangerous", "exp": "Macros are often used to download malware automatically."},
            {"q": "What is a 'Watering Hole' attack?", "options": ["Flooding a server", "Infecting a site you visit", "Phishing via water bills", "Hacking smart water meters"], "answer": "Infecting a site you visit", "exp": "Hackers infect a legitimate website that they know their target visits."},
            {"q": "If you fall for a phish, what is the FIRST thing you should do?", "options": ["Delete the email", "Disconnect internet & Report", "Wait and see", "Reply to the attacker"], "answer": "Disconnect internet & Report", "exp": "Disconnect to stop data transfer and report it to IT immediately."},
            {"q": "Which is safer: SMS 2FA or App-based 2FA (like Google Authenticator)?", "options": ["SMS is safer", "App-based is safer", "They are equal", "Neither is safe"], "answer": "App-based is safer", "exp": "SMS can be intercepted (SIM Swapping). App codes are generated locally."},
            {"q": "A browser warning says 'Deceptive Site Ahead'. You should...", "options": ["Proceed anyway", "Go back to safety", "Turn off antivirus", "Reload the page"], "answer": "Go back to safety", "exp": "Modern browsers have strong phishing blocklists. Trust the warning."},
            {"q": "What is 'Spear Phishing'?", "options": ["Random spam", "Targeting a specific person", "Phishing via phone", "Mass email attacks"], "answer": "Targeting a specific person", "exp": "It uses specific details about YOU to make the scam look real."},
            {"q": "Someone asks you to download 'AnyDesk' or 'TeamViewer' to fix your computer.", "options": ["Download it", "Refuse and hang up", "Ask for their ID", "Share your screen"], "answer": "Refuse and hang up", "exp": "These are remote control tools. Scammers use them to steal money."},
            {"q": "You win a 'Free iPhone' but need to pay $1 for shipping.", "options": ["Pay the $1", "Enter credit card info", "Ignore/Delete", "Ask for tracking"], "answer": "Ignore/Delete", "exp": "If it sounds too good to be true, it is. They just want your credit card info."}
        ]
        
        self.game_state_reset()
        self.create_start_screen()

    def game_state_reset(self):
        # --- LOGIC CHANGE: Randomly select 10 unique questions from the large pool ---
        self.questions = random.sample(self.large_question_pool, 10)
        self.current_index = 0
        self.score = 0
        self.streak = 0

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    # ==============================
    # 1. START SCREEN
    # ==============================
    def create_start_screen(self):
        self.clear_screen()

        # Header
        header = ctk.CTkFrame(self, height=100, fg_color="transparent")
        header.pack(pady=(60, 20))

        ctk.CTkLabel(header, text="🛡️", font=("Arial", 60)).pack()
        ctk.CTkLabel(header, text="PHISHING AWARENESS", font=("Roboto Medium", 32, "bold"), text_color=self.col_accent).pack(pady=5)
        ctk.CTkLabel(header, text="CERTIFIED TRAINING MODULE", font=("Roboto", 16), text_color=self.col_muted).pack()

        # Info Card
        card = ctk.CTkFrame(self, fg_color=self.col_card, corner_radius=20, width=500, height=200)
        card.pack(pady=40, padx=20)
        
        # Dynamic Text explaining the random generation
        info_text = (
            "Task 2: CodeAlpha Internship\n\n"
            "• You will face 10 Random Questions.\n"
            "• Each session is unique (Pool of 25+).\n"
            "• Topics: Smishing, Vishing, URLs, & More."
        )
        ctk.CTkLabel(card, text=info_text, font=("Roboto", 18), text_color=self.col_text, justify="left").place(relx=0.5, rely=0.5, anchor="center")

        # Buttons
        ctk.CTkButton(self, text="START QUIZ (10 Questions) ➤", font=("Roboto", 20, "bold"), 
                      fg_color=self.col_accent, text_color="black", hover_color="#00B8D4",
                      corner_radius=32, width=300, height=60, 
                      command=self.create_quiz_screen).pack(pady=10)

        # Quit App Button
        ctk.CTkButton(self, text="EXIT APP", font=("Roboto", 14, "bold"), 
                      fg_color="transparent", border_width=1, border_color=self.col_wrong, text_color=self.col_wrong,
                      hover_color="#3a0d14", corner_radius=20, width=150, height=35, 
                      command=self.destroy).pack(pady=10)

    # ==============================
    # 2. QUIZ SCREEN
    # ==============================
    def create_quiz_screen(self):
        self.clear_screen()

        # --- Top Navigation Bar ---
        nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        nav_frame.pack(fill="x", padx=30, pady=(30, 10))

        # Quit Quiz Button
        ctk.CTkButton(nav_frame, text="✕ QUIT QUIZ", font=("Roboto", 12, "bold"),
                      width=100, height=30, corner_radius=15,
                      fg_color="transparent", border_width=1, border_color=self.col_muted, text_color=self.col_muted,
                      hover_color="#334155",
                      command=self.create_start_screen).pack(side="left")

        # Question Count
        ctk.CTkLabel(nav_frame, text=f"QUESTION {self.current_index + 1} / {len(self.questions)}", 
                     font=("Roboto", 14, "bold"), text_color=self.col_text).pack(side="left", padx=40)

        # Streak
        ctk.CTkLabel(nav_frame, text=f"🔥 STREAK: {self.streak}", 
                     font=("Roboto", 14, "bold"), text_color="#FFA726").pack(side="right")

        # Progress Bar
        self.progress = ctk.CTkProgressBar(self, width=800, height=10, progress_color=self.col_accent)
        self.progress.pack(pady=(0, 30))
        self.progress.set((self.current_index) / len(self.questions))

        # --- Question Card ---
        self.card = ctk.CTkFrame(self, fg_color=self.col_card, corner_radius=25, border_width=2, border_color=self.col_card)
        self.card.pack(fill="both", expand=True, padx=50, pady=(0, 40))

        q_data = self.questions[self.current_index]

        # Question Text
        ctk.CTkLabel(self.card, text=q_data["q"], font=("Roboto Medium", 24), 
                     text_color=self.col_text, wraplength=700).pack(pady=(40, 30))

        # Options Container
        options_frame = ctk.CTkFrame(self.card, fg_color="transparent")
        options_frame.pack(fill="both", expand=True, padx=100)

        self.option_buttons = []
        options = q_data["options"][:]
        random.shuffle(options)

        for opt in options:
            btn = ctk.CTkButton(options_frame, text=opt, font=("Roboto", 18), 
                                fg_color="transparent", border_width=2, border_color="#37474F",
                                corner_radius=15, height=55, anchor="w",
                                hover_color="#263238",
                                command=lambda o=opt: self.check_answer(o))
            btn.pack(pady=8, fill="x")
            self.option_buttons.append(btn)

        # Feedback & Next
        self.feedback_frame = ctk.CTkFrame(self, fg_color="transparent", height=80)
        self.feedback_frame.pack(fill="x", side="bottom", pady=20)
        
        self.feedback_label = ctk.CTkLabel(self.feedback_frame, text="", font=("Roboto", 18, "bold"))
        self.feedback_label.pack()

        self.next_btn = ctk.CTkButton(self.feedback_frame, text="NEXT ➜", width=150, height=40,
                                      fg_color=self.col_accent, text_color="black", hover_color="#00B8D4",
                                      font=("Roboto", 16, "bold"), corner_radius=20,
                                      command=self.next_question)

    # ==============================
    # 3. LOGIC
    # ==============================
    def check_answer(self, selected):
        correct = self.questions[self.current_index]["answer"]
        explanation = self.questions[self.current_index]["exp"]

        for btn in self.option_buttons:
            btn.configure(state="disabled")
            if btn.cget("text") == correct:
                btn.configure(fg_color=self.col_correct, border_color=self.col_correct, text_color="black")
            elif btn.cget("text") == selected and selected != correct:
                btn.configure(fg_color=self.col_wrong, border_color=self.col_wrong)

        if selected == correct:
            self.score += 1
            self.streak += 1
            self.feedback_label.configure(text=f"✅ CORRECT! {explanation}", text_color=self.col_correct)
            self.card.configure(border_color=self.col_correct)
        else:
            self.streak = 0
            self.feedback_label.configure(text=f"❌ WRONG. {explanation}", text_color=self.col_wrong)
            self.card.configure(border_color=self.col_wrong)

        self.next_btn.pack(pady=10)

    def next_question(self):
        self.current_index += 1
        if self.current_index < len(self.questions):
            self.create_quiz_screen()
        else:
            self.create_result_screen()

    # ==============================
    # 4. RESULTS
    # ==============================
    def create_result_screen(self):
        self.clear_screen()

        ctk.CTkLabel(self, text="TRAINING COMPLETE", font=("Roboto", 20, "bold"), text_color=self.col_muted).pack(pady=(80, 10))
        
        score_percent = (self.score / len(self.questions)) * 100
        final_color = self.col_correct if score_percent >= 70 else self.col_wrong
        
        score_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=5, border_color=final_color, corner_radius=100, width=200, height=200)
        score_frame.pack(pady=20)
        
        ctk.CTkLabel(score_frame, text=f"{score_percent:.0f}%", font=("Roboto", 60, "bold"), text_color=self.col_text).place(relx=0.5, rely=0.5, anchor="center")

        status = "PASSED: SECURITY AWARE" if score_percent >= 70 else "FAILED: REVIEW REQUIRED"
        ctk.CTkLabel(self, text=status, font=("Roboto", 24, "bold"), text_color=final_color).pack(pady=20)

        # Summary Text
        ctk.CTkLabel(self, text=f"You answered {self.score} out of 10 correctly.", font=("Roboto", 16), text_color=self.col_text).pack(pady=5)

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=20)

        # Retry
        ctk.CTkButton(btn_frame, text="Try Again (New Questions) ↺", font=("Roboto", 16), width=220, height=50, corner_radius=25,
                      fg_color="#37474F", hover_color="#455A64", command=self.restart).pack(side="left", padx=10)
        
        # Quit App
        ctk.CTkButton(btn_frame, text="Exit App ✕", font=("Roboto", 16), width=150, height=50, corner_radius=25,
                      fg_color=self.col_wrong, hover_color="#C2185B", command=self.destroy).pack(side="left", padx=10)

    def restart(self):
        self.game_state_reset()
        self.create_start_screen()

if __name__ == "__main__":
    app = StylishQuizApp()
    app.mainloop()