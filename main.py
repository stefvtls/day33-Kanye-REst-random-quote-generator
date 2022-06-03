import tkinter
import requests

window = tkinter.Tk()
window.title("kanye rest quotes")
window.minsize(height=580, width=340)
window.config(padx=20, pady=20)


def quote():
        kayne_link = requests.get(url="https://api.kanye.rest")
        kayne_link.raise_for_status()
        kayne_quote = kayne_link.json()
        x = kayne_quote["quote"]
        canva.itemconfig(place_for_quote, text=f"{x}")

canva_image = tkinter.PhotoImage(file="background.png")
head_image = tkinter.PhotoImage(file="kanye.png")
canva = tkinter.Canvas(height=440, width=300, highlightthickness=0)
canva.create_image(0, 0, anchor="nw", image=canva_image)
place_for_quote = canva.create_text(40, 70, anchor="nw", font=("Arial", 20, "italic"), fill="black", text="CLICK MY HEAD", width=250)
canva.grid(column=0, row=0)
head = tkinter.Button(image=head_image, command=quote, highlightthickness=0)
head.grid(column=0, row=1)

window.mainloop()