from customtkinter import *
import customtkinter
from tkinter import messagebox
from tkinter import *


def add_expression(num):
    global label_expression

    label_expression += str(num)
    result.set(label_expression)


def egal():
    global label_expression
    try:
        label_result = eval(label_expression)
        result.set(str(label_result))
        label_expression = str(label_result)
    except ZeroDivisionError:
        result.set("Division par zero!")
    except SyntaxError:
        result.set("Erreur de syntaxe")


def clear(letter):
    if letter == 'c':
        global label_expression
        result.set("0")
        label_expression = ""
    else:
        global label_convert_expression
        result_convert.set("0")
        expression.set("0")
        label_convert_expression = ""


def backspace(letter):
    if letter == 'c':
        global label_expression
        n = len(label_expression) - 1
        try:
            label_expression = label_expression.replace(label_expression[n], "")
            result.set(label_expression)
        except IndexError:
            messagebox.showwarning(title="Attention", message="Le champ est vide, vous ne pouvez pas supprimer",
                                   icon="warning")
    else:
        global label_convert_expression
        n = len(label_convert_expression) - 1
        try:
            label_convert_expression = label_convert_expression.replace(label_convert_expression[n], "")
            expression.set(label_convert_expression)
        except IndexError:
            messagebox.showwarning(title="Attention", message="Le champ est vide, vous ne pouvez pas supprimer",
                                   icon="warning")


def convert(num):
    global base_finale
    base_finale = num
    base_out.set(f"Base {num}")


def convertir():
    global base_depart, base_finale, expression, label_convert_expression
    if base_depart == 0:
        messagebox.showwarning(title="Attention", message="Vous n'avez pas choisi la base de depart!", icon="warning")
    elif base_finale == 0:
        messagebox.showwarning(title="Attention", message="Vous n'avez pas choisi la base finale!", icon="warning")
    else:
        if base_depart != 10:
            try:
                if base_depart == 2:
                    nbr_base_dix = int(label_convert_expression, 2)
                elif base_depart == 8:
                    nbr_base_dix = int(label_convert_expression, 8)
                else:
                    nbr_base_dix = int(label_convert_expression, 16)

                if base_finale == 2:
                    result_convert.set("{:b}".format(nbr_base_dix))
                elif base_finale == 8:
                    result_convert.set("{:o}".format(nbr_base_dix))
                elif base_finale == 10:
                    result_convert.set(str(nbr_base_dix))
                else:
                    result_convert.set("{:X}".format(nbr_base_dix))

            except:
                messagebox.showwarning(title="Erreur",
                                       message="Utilisez uniquement les chiffres valide pour votre base:\n\n"
                                               "Base 2: uniquement 0 et 1\n"
                                               "Base 8: uniquement de 0 a 7\n"
                                               "Base 10: uniauement de 0 a 9\n"
                                               "Base 16: de 0 a 9 et de A a F\n",
                                       icon="warning")
                expression.set("0")
                label_convert_expression = ""
        else:
            try:
                nbr = int(label_convert_expression)
                if base_finale == 2:
                    nbr_convert = "{:b}".format(nbr)
                    result_convert.set(str(nbr_convert))
                elif base_finale == 8:
                    nbr_convert = "{:o}".format(nbr)
                    result_convert.set(str(nbr_convert))
                elif base_finale == 10:
                    result_convert.set(str(nbr))
                else:
                    nbr_convert = "{:X}".format(nbr)
                    result_convert.set(str(nbr_convert))
            except:
                messagebox.showwarning(title="Erreur",
                                       message="Vous devez entrer uniquement les chiffres compris entre 0 et 9",
                                       icon="warning")


def add_expression_convert(num):
    global label_convert_expression
    label_convert_expression += str(num)
    expression.set(label_convert_expression)


def choisir_base():
    global base_depart
    temp = CTkInputDialog(text="Entrez la base du nombre de depart!", title="Base de depart")
    temp_value = temp.get_input()
    temp_value = int(temp_value)
    bases = [2, 8, 10, 16]
    trouve = temp_value in bases
    while not trouve:
        temp = CTkInputDialog(text="Entrez une base parmi: 2, 8, 10, 16", title="Base de depart")
        temp_value = temp.get_input()
        trouve = temp_value in bases
    base_depart = temp_value
    base_in.set(f"Base {temp_value}")


def theme():
    if switch_var.get() == "off":
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

label_expression = ""
label_convert_expression = ""
base_finale = 0
base_depart = 0

app = CTk()
app.title("calculator")

expression = StringVar(value="0")
result_convert = StringVar(value="0")
base_in = StringVar(value="Base depart")
base_out = StringVar(value="Base finale")
result = StringVar(value="0")

tabs = CTkTabview(app, segmented_button_selected_color="red", segmented_button_selected_hover_color="red",
                  segmented_button_fg_color=("white", "black"), text_color=("black", "white"),
                  segmented_button_unselected_color=("white", "black"))
tabs.add("Calculatrice classique")

tabs.pack(pady=10, padx=15)
switch_var = StringVar(value="off")
switch = CTkSwitch(app, text="Light", command=theme,
                   variable=switch_var, progress_color="white",
                   onvalue="on", offvalue="off",
                   fg_color="black",
                   button_color="red",
                   button_hover_color="red").pack(pady=10)

result_label = CTkLabel(master=tabs.tab("Calculatrice classique"),
                        font=('sans-serif', 30),
                        width=300, height=40,
                        fg_color=("white", "#5E5E5E"), text_color=("black", "white"), corner_radius=7,
                        textvariable=result, justify="right")
result_label.grid(padx=10, pady=20, row=0, column=0, columnspan=4)

CTkLabel(tabs.tab("Calculatrice classique"), text="").grid(row=1, pady=5)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="9",
          command=lambda: add_expression(9)).grid(row=2, column=0)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="8",
          command=lambda: add_expression(8)).grid(row=2, column=1)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="7",
          command=lambda: add_expression(7)).grid(row=2, column=2)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="6",
          command=lambda: add_expression(6)).grid(row=3, column=0)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="5",
          command=lambda: add_expression(5)).grid(row=3, column=1)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=12, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="4",
          command=lambda: add_expression(4)).grid(row=3, column=2)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="3",
          command=lambda: add_expression(3)).grid(row=4, column=0)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="2",
          command=lambda: add_expression(2)).grid(row=4, column=1)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="1",
          command=lambda: add_expression(1)).grid(row=4, column=2)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="0",
          command=lambda: add_expression(0)).grid(row=5, column=0)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text=".",
          command=lambda: add_expression(".")).grid(row=5, column=1)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="=",
          command=egal).grid(row=5, column=2)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 39),
          text="+",
          command=lambda: add_expression("+")).grid(row=2, column=3)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 39),
          text="-",
          command=lambda: add_expression("-")).grid(row=3, column=3)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 39),
          text="*",
          command=lambda: add_expression("*")).grid(row=4, column=3)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 39),
          text="/",
          command=lambda: add_expression("/")).grid(row=5, column=3)

CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text="(",
          command=lambda: add_expression("(")).grid(row=6, column=0)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text=")",
          command=lambda: add_expression(")")).grid(row=6, column=1)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text="→",
          command=lambda: backspace('c')).grid(row=6, column=2)
CTkButton(master=tabs.tab("Calculatrice classique"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text="C",
          command=lambda: clear('c')).grid(row=6, column=3)
CTkLabel(tabs.tab("Calculatrice classique"), text="").grid()

# conversion base
tabs.add("Calculatrice de base")

tabs.pack(pady=10, padx=15)
nb_label = CTkLabel(master=tabs.tab("Calculatrice de base"),
                    font=('sans-serif', 30),
                    width=300, height=40,
                    fg_color=("white", "#5E5E5E"), text_color=("black", "white"), corner_radius=7,
                    textvariable=expression, justify="right")
nb_label.grid(padx=10, pady=10, row=1, column=0, columnspan=4)

CTkButton(tabs.tab("Calculatrice de base"),
          command=choisir_base,
          textvariable=base_in,
          font=('sans-serif', 15, 'italic'),
          text_color="red",
          hover=False,
          bg_color="transparent",
          fg_color="transparent").grid(row=0, column=0, columnspan=4)
CTkLabel(tabs.tab("Calculatrice de base"),
         textvariable=base_out,
         font=('sans-serif', 15, 'italic'),
         text_color="red").grid(row=2, column=0, columnspan=4)

convert_label1 = CTkLabel(master=tabs.tab("Calculatrice de base"),
                          font=('sans-serif', 30),
                          width=300, height=40,
                          fg_color=("white", "#5E5E5E"), text_color=("black", "white"), corner_radius=7,
                          textvariable=result_convert, justify="right")
convert_label1.grid(padx=10, pady=10, row=3, column=0, columnspan=4)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="9",
          command=lambda: add_expression_convert(9)).grid(row=4, column=0)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="8",
          command=lambda: add_expression_convert(8)).grid(row=4, column=1)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="7",
          command=lambda: add_expression_convert(7)).grid(row=4, column=2)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="6",
          command=lambda: add_expression_convert(6)).grid(row=5, column=0)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="5",
          command=lambda: add_expression_convert(5)).grid(row=5, column=1)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=12, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="4",
          command=lambda: add_expression_convert(4)).grid(row=5, column=2)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="3",
          command=lambda: add_expression_convert(3)).grid(row=6, column=0)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="2",
          command=lambda: add_expression_convert(2)).grid(row=6, column=1)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="1",
          command=lambda: add_expression_convert(1)).grid(row=6, column=2)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="0",
          command=lambda: add_expression_convert(0)).grid(row=7, column=0)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12, hover_color="red",
          fg_color="transparent",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="A",
          command=lambda: add_expression_convert("A")).grid(row=7, column=1)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="B",
          command=lambda: add_expression_convert("B")).grid(row=7, column=2)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="C",
          command=lambda: add_expression_convert("C")).grid(row=8, column=0)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="D",
          command=lambda: add_expression_convert("D")).grid(row=8, column=1)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="E",
          command=lambda: add_expression_convert("E")).grid(row=8, column=2)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="red",
          text_color=("black", "white"),
          font=('sans-serif', 39),
          text="F",
          command=lambda: add_expression_convert("F")).grid(row=9, column=0)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 25),
          text="B₂",
          command=lambda: convert(2)).grid(row=4, column=3)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 25),
          text="B₈",
          command=lambda: convert(8)).grid(row=5, column=3)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 25),
          text="B₁₀",
          command=lambda: convert(10)).grid(row=6, column=3)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 25),
          text="B₁₆",
          command=lambda: convert(16)).grid(row=7, column=3)

CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text="→",
          command=lambda: backspace('b')).grid(row=9, column=1)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=16, height=12,
          fg_color="transparent", hover_color="white",
          text_color="red",
          font=('sans-serif', 30),
          text="C",
          command=lambda: clear('b')).grid(row=9, column=2)
CTkButton(master=tabs.tab("Calculatrice de base"),
          width=12, height=8,
          fg_color="red", hover_color="red",
          text_color="white",
          font=('sans-serif', 25),
          text="convert",
          command=convertir).grid(row=9, column=3)

CTkLabel(tabs.tab("Calculatrice de base"), text="").grid()

app.mainloop()
