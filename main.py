import tkinter as tk
from tkinter import ttk
from googletrans import Translator,LANGUAGES

window = tk.Tk()
window.geometry("400x500")
window.configure(bg="#1c1c1c") 
window.title("Translator")

def Translate(Text="text", UserLanguage="english", TranlateLanguage="urdu"):
    Trans_Lator = Translator()
    Trans_Late = Trans_Lator.translate(text=Text, src=UserLanguage, dest=TranlateLanguage)
    return Trans_Late.text
    
def Data():
    Source = UserCombo.get()
    Destination = TranslateCombo.get()
    User_Text = UserText.get(1.0, "end")
    TransLate_Text = Translate(Text=User_Text, UserLanguage=Source, TranlateLanguage=Destination)
    TranslateText.delete(1.0, "end")
    TranslateText.insert(1.0, TransLate_Text)


Languages = list(LANGUAGES.values())

FirstLabel = tk.Label(window, text="Translator", font=("STENCIL", 30), bg="#1c1c1c", fg="#F3F3F3")
FirstLabel.place(x=70, y=15)

UserTextLabel = tk.Label(window, text="Your Text", font=("STENCIL", 15), bg="#1c1c1c", fg="#F3F3F3")
UserTextLabel.place(x=150, y=80)

UserText = tk.Text(window, fg="#F3F3F3", bg="#3a3a3b", font=("Century", 15))
UserText.place(height=140, width=400, x=0, y=110)



UserCombo = ttk.Combobox(window, values=Languages)
UserCombo.place(x=0, y=270, width=100, height=30)
UserCombo.set("english")
TranslateButton = tk.Button(window, text="Translate", fg="#F3F3F3", bg="#171717", font=("Century", 12),
                            activebackground="#080808", activeforeground="#F3F3F3", command=Data, relief="raised")
TranslateButton.place(height=35, width=100, x=150, y=270)

TranslateCombo = ttk.Combobox(window, values=Languages)
TranslateCombo.place(x=300, y=270, width=100, height=30)
TranslateCombo.set("urdu")

TranslateTextLabel = tk.Label(window, text="Translate Text", font=("STENCIL", 15), bg="#1c1c1c", fg="#F3F3F3")
TranslateTextLabel.place(x=120, y=310)

TranslateText = tk.Text(window, fg="#F3F3F3", bg="#3a3a3b", font=("Century", 15))
TranslateText.place(height=140, width=400, x=0, y=340)

window.mainloop()