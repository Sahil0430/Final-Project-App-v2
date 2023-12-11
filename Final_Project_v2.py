import tkinter as tk
from tkinter import Toplevel, Listbox, MULTIPLE, messagebox, ttk

# Global variables to store user selections
selected_proteins = []
selected_veggies = []

# Mock database of recipes
recipes = {
    "Chicken Salad": {
        "ingredients": ["Chicken", "Lettuce", "Tomato", "Cucumber"],
        "time": "15 mins",
        "steps": ["Chop all ingredients", "Mix them", "Serve"],
        "calories": "300 kcal"
    },
    "Beef Stew": {
        "ingredients": ["Beef", "Potato", "Carrot", "Onion"],
        "time": "1 hour",
        "steps": ["Brown the beef", "Add vegetables and simmer", "Serve hot"],
        "calories": "450 kcal"
    },
    # ... other recipes
}

# Function definitions ...
# Function to open the Protein selection window
def open_protein_window():
    protein_window = Toplevel(root)
    protein_window.title("Select Protein")

    proteins = ["Chicken", "Beef", "Fish"]
    protein_listbox = Listbox(protein_window, selectmode=MULTIPLE)
    for protein in proteins:
        protein_listbox.insert(tk.END, protein)
    protein_listbox.pack()

    tk.Button(protein_window, text="Save", command=lambda: save_ingredients(protein_listbox, "protein")).pack()
    tk.Button(protein_window, text="Back", command=protein_window.destroy).pack()

# Function to open the Veggies selection window
def open_veggies_window():
    veggies_window = Toplevel(root)
    veggies_window.title("Select Veggies")

    veggies = ["Tomato", "Onion", "Carrot", "Potato", "Cucumber", "Lettuce", "Spinach", "Cabbage"]
    veggies_listbox = Listbox(veggies_window, selectmode=MULTIPLE)
    for veggie in veggies:
        veggies_listbox.insert(tk.END, veggie)
    veggies_listbox.pack()

    tk.Button(veggies_window, text="Save", command=lambda: save_ingredients(veggies_listbox, "veggies")).pack()
    tk.Button(veggies_window, text="Back", command=veggies_window.destroy).pack()

# Function to save selected ingredients
def save_ingredients(listbox, ingredient_type):
    global selected_proteins, selected_veggies
    selected = [listbox.get(i) for i in listbox.curselection()]
    if ingredient_type == "protein":
        selected_proteins = selected
    else:
        selected_veggies = selected
    messagebox.showinfo("Selection Saved", f"Selected {ingredient_type}: {', '.join(selected)}")
# Function to find and display a recipe
def find_recipe():
    print("Finding recipe...")
    print("Selected proteins:", selected_proteins)
    print("Selected veggies:", selected_veggies)
    for recipe, details in recipes.items():
        if all(ingredient in selected_proteins + selected_veggies for ingredient in details["ingredients"]):
            print("Recipe found:", recipe)
            display_recipe(recipe, details)
            return
    print("No matching recipe found.")
    messagebox.showinfo("No Recipe Found", "Sorry, no matching recipe found. Try different ingredients.")
# Function to display the recipe details
def display_recipe(name, details):
    recipe_window = Toplevel(root)
    recipe_window.title(name)
    tk.Label(recipe_window, text=f"Recipe: {name}").pack()
    tk.Label(recipe_window, text=f"Ingredients: {', '.join(details['ingredients'])}").pack()
    tk.Label(recipe_window, text=f"Time to Cook: {details['time']}").pack()
    tk.Label(recipe_window, text=f"Calories: {details['calories']}").pack()
    tk.Label(recipe_window, text="Cooking Steps:").pack()
    for step in details['steps']:
        tk.Label(recipe_window, text=f"- {step}").pack()

# Main application window
# Use a ttk style
style = ttk.Style()
style.theme_use('clam')  # or 'alt', 'default', 'classic', 'vista', etc.

root = tk.Tk()
root.title("GranRecipes")

# Set a minimum size for the window
root.minsize(300, 200)

# Customize fonts and colors for buttons
titleLabel = ttk.Label(root, text="Welcome to GranRecipes!", font=("Helvetica", 16, "bold"))
titleLabel.pack(pady=10)

subLabel = ttk.Label(root, text="Let Ol' Gran help you out here. What's left over in the kitchen?", font=("Helvetica", 10))
subLabel.pack(pady=5)

proteinButton = ttk.Button(root, text="Protein", command=open_protein_window)
proteinButton.pack(pady=5)

veggiesButton = ttk.Button(root, text="Veggies", command=open_veggies_window)
veggiesButton.pack(pady=5)

findRecipeButton = ttk.Button(root, text="Find Recipe", command=find_recipe)
findRecipeButton.pack(pady=10)


# Start the GUI event loop
root.mainloop()
