import tkinter 
from tkinter import messagebox
import pickle

root = tkinter.Tk()
root.configure(bg = "white")
root.title("Economics Review Guide") 
root.geometry("3000x3000")

to_delete = ""

class Concept():
    def __init__(self, definition, explanation, example): 
        self.definition = definition
        self.explanation = explanation
        self.example = example

concept_1 = Concept("Definition: \nMonopoly is a market structure with one firm producing a unique product, determine the product price with high barriers to enter \nand exit the market. Natural Monopoly is an industry makes the price cheaper and produces efficiently by having a monopoly than \nseveral smaller competing firms.", "Explanation: \nAccording to the graph of monopoly (it's on the far right side), unregulated quantity is at the intersection of marginal cost and marginal \nrevenue; the socially optimal quantity is at the intersection of marginal cost and demand; the fair return quantity is at the intersection of \ndemand and average total cost. The typical examples for monopoly are Facebook, Paypal, Electric Power Companies, Phone Companies.", "Example: \nIf this was competitive market, \n1. Price and quantity: P4, Q2 \n2. Consumer surplus: ACP4. \nIf this is an unregulated monopoly \n3.Priceandquantity:P5, Q1 \n4. Consumer surplus: ABP5 \n5. Deadweight loss: BCG \n6. Quantity total revenue maximized: Q3 MR=0 7. \nQuantity if it perfectly price discriminates: Q2 8. Elastic range of the demand curve: AD \n9. If the government placed a per unit tax on this monopoly then price __↑_ and quantity __↓_ \n10. If the government placed a lump sum subsidy on this monopoly then price \nsame and quantity same. (Lump sum subsidies don’t shift MC)")

concept_2 = Concept("Definition: \n The branch of mathematics concerned with the analysis of strategies for dealing with competitive situations where the outcome of a participant's choice of action depends critically on the actions of other participants. Game theory has been applied to contexts in war, business, and biology. Nash Equilibrium is the optimal outcome where neither player can make themselves better off by deviating from the current strategy.", "Explanation: \nGame: Any set of circumstances that has a result dependent on the actions of two of more decision-makers (players). \nPlayers: A strategic decision-maker within the context of the game. \nStrategy: A complete plan of action a player will take \ngiven the set of circumstances that might arise within the game. \nPayoff: The payout a player receives from arriving at a particular outcome. The payout can be \nin any quantifiable form, from dollars to utility. \nInformation set: The information available at a given point in the game. The term information set is \nmost usually applied when the game has a sequential component. \nEquilibrium: The point in a game where both players have made their decisions and an outcome is reached.", "Example: \n1. If David decides to advertise now and Lindsey decides to do it later, what is David’s expected profit? $1000 \n2. What is Lindsey’s dominant strategy? Now \n3. What is David’s dominant strategy? None \n4. If both owners have the information but do not \nactively collude, what will be the outcome? Both will choose Now \nAssume the advertising company offers a deal that increases the profit for \nboth owners by $2,000 but only if they advertise later. Based on these changes: \n5. What is Lindsey’s dominant strategy? None \n6. What is David’s dominant strategy? Later")
exp = Concept("""Concept: Press the button (Monopoly/Game Theory) to see the definition, explanation (see the graph on the far right side), \nexample (see the graph on the far right side). 

Delete one: In order to delete either definition, or explanation, or example, press the area around definition, explanation, \nand example to delete on of them. In order to show the deleted one again, press the button (Game theory/Monopoly) again
""", "Save File/Load File: On the lower right side, the yellow box is for taking notes. Press save file first to save the file, load file to show the previous one.", "Exit: Exit the program")
concepts = [concept_1, concept_2, exp]

def help():
    for concept in concepts:
        definition = "{}".format(concept.definition)
        explanation = "{}".format(concept.explanation)
        example = "{}".format(concept.example)
    lbl_definition["text"] = exp.definition
    lbl_explanation["text"] = exp.explanation
    lbl_example["text"] = exp.example

def show_concept_one():
    lbl_definition.configure(fg = "black")
    lbl_explanation.configure(fg = "black")
    lbl_example.configure(fg = "black")
    change_graph("monopoly.gif")

    for concept in concepts:
        definition = "{}".format(concept.definition)
        explanation = "{}".format(concept.explanation)
        example = "{}".format(concept.example)
    lbl_definition["text"] = concept_1.definition
    lbl_explanation["text"] = concept_1.explanation
    lbl_example["text"] = concept_1.example

def show_concept_two():
    lbl_definition.configure(fg = "black")
    lbl_explanation.configure(fg = "black")
    lbl_example.configure(fg = "black")
    change_graph("game.gif")

    for concept in concepts:
        definition = "{}".format(concept.definition)
        explanation = "{}".format(concept.explanation)
        example = "{}".format(concept.example)
    lbl_definition["text"] = concept_2.definition
    lbl_explanation["text"] = concept_2.explanation
    lbl_example["text"] = concept_2.example

def set_delete_definition(event = None):
    print("DEFINITION SET")
    global to_delete
    to_delete = "definition"
    lbl_definition.configure(fg = "red")

def set_delete_example(event = None):
    print("EXAMPLE SET")
    global to_delete
    to_delete = "example"
    lbl_example.configure(fg = "red")

def set_delete_explanation(event = None):
    print("EXPLANATION SET")
    global to_delete
    to_delete = "explanation"
    lbl_explanation.configure(fg = "red")

def delete_one():
    print("DELETE ONE")
    global to_delete
    print(to_delete)
    if to_delete == "definition":
        lbl_definition["text"] = ""
    elif to_delete == "explanation":
        lbl_explanation["text"] = ""
    elif to_delete == "example":
        lbl_example["text"] = ""

def load_file():
    data = pickle.load(open("Capstone.dat", "rb"))
    print("Loaded Data: {}".format(data))
    text_input.delete(1.0, "end")
    text_input.insert("end", data)

def save_file():
    data = text_input.get(1.0, "end")
    pickle.dump(data, open("Capstone.dat", "wb"))
    print("Saved Data: {}".format(data))

def exit():
    confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to quit? Please make sure to save your notes before you quit.")
    if confirm: 
        global root
        root.quit()

def change_graph(image):
    photo = tkinter.PhotoImage(file = image )
    lb_graph.configure(image = photo)
    lb_graph.image = photo


lbl_button = tkinter.Label(root, text = "Button", bg = "White")
lbl_button.grid(row = 0, column = 0)

btn_concept_1 = tkinter.Button(root, text = "Monopoly", fg = "black", width = 16, height = 3, command = show_concept_one) 
btn_concept_1.grid(row = 1, column = 0)

btn_concept_2 = tkinter.Button(root, text = "Game Theory", fg = "black", width = 16, height = 3, command = show_concept_two) 
btn_concept_2.grid(row = 2, column = 0)

btn_delete_one = tkinter.Button(root, text = "Delete One", fg = "black", width = 16, height = 3, command = delete_one) 
btn_delete_one.grid(row = 3, column = 0)

btn_save_file = tkinter.Button(root, text = "Save File", fg = "black", width = 16, height = 3, command = save_file) 
btn_save_file.grid(row = 4, column = 0)

btn_load_file = tkinter.Button(root, text = "Load File", fg = "black", width = 16, height = 3, command = load_file) 
btn_load_file.grid(row = 5, column = 0)

btn_help = tkinter.Button(root, text = "Help", fg = "black", width = 16, height = 3, command = help) 
btn_help.grid(row = 6, column = 0)

btn_exit = tkinter.Button(root, text = "Exit", fg = "black", width = 16, height = 3, command = exit) 
btn_exit.grid(row = 7, column = 0)

lbl_title = tkinter.Label(root, text = "Dates of Test: May 17 2019", bg = "White")
lbl_title.grid(row = 8, column = 0)

lbl_e = tkinter.Label(root, text = "Explanation", bg = "White")
lbl_e.grid(row = 0, column = 4)

lbl_definition = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_definition.grid(row = 2, column = 4)
 
lbl_explanation = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_explanation.grid(row = 4, column = 4)
 
lbl_example = tkinter.Label(root, text = "" , bg = "white", width = 100)
lbl_example.grid(row = 6, column = 4)

photo = tkinter.PhotoImage()
lb_graph = tkinter.Label(image = photo)
lb_graph.image = photo 
lb_graph.grid(row = 0, column = 8, rowspan = 7)

lbl_input = tkinter.Label(root, text = "Taking Your Notes Here" , bg = "white")
lbl_input.grid(row = 6, column = 8)
text_input = tkinter.Text(root, width = 58, bg="Yellow", bd=5)
text_input.grid(row = 7, column = 8, rowspan = 2) 

lbl_definition.bind("<Button-1>", set_delete_definition)

lbl_explanation.bind("<Button-1>", set_delete_explanation)

lbl_example.bind("<Button-1>", set_delete_example )



root.mainloop() 





