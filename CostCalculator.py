import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_cost():
    # Get values from input fields
    athlete_name = name_entry.get()
    training_plan = training_plan_var.get()
    weight = float(weight_entry.get())
    competition_category = competition_category_var.get()
    competitions = int(competitions_spinbox.get())
    private_coaching_hours = int(private_coaching_hours_spinbox.get())

    # Check for user errors and display suitable messages
    if private_coaching_hours > 5:
        result_label.config(text="Error: Maximum 5 hours of private coaching allowed per week")
        return

    if training_plan not in ["Beginner", "Intermediate", "Elite"]:
        result_label.config(text="Error: Only Intermediate and Elite athletes can enter competitions")
        return

    # Perform the cost calculation (customize based on your pricing structure)
    total_cost = calculate_total_cost(training_plan, competitions, private_coaching_hours)

    # Display the result
    result_label.config(text=f"Total Cost for {athlete_name}: £{total_cost:.2f}")

def calculate_total_cost(training_plan, competitions, private_coaching_hours):
    # Implement your cost calculation logic based on the provided parameters
    # This is a simple example; customize it according to your pricing structure
    base_cost = {"Beginner": 25.00, "Intermediate": 30.00, "Elite": 35.00}.get(training_plan, 0)
    competition_cost = 22.00 * competitions
    private_coaching_cost = 9.50 * private_coaching_hours

    total_cost = base_cost + competition_cost + private_coaching_cost
    return total_cost

def open_registration_window():
    registration_window = tk.Toplevel(app)
    registration_window.title("Athlete Registration")

    # Labels and entry widgets for athlete registration
    name_label_reg = ttk.Label(registration_window, text="Name:")
    name_label_reg.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    dob_label_reg = ttk.Label(registration_window, text="Date of Birth:")
    dob_label_reg.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    address_label_reg = ttk.Label(registration_window, text="Address:")
    address_label_reg.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    name_entry_reg = ttk.Entry(registration_window)
    name_entry_reg.grid(row=0, column=1, padx=10, pady=10)

    dob_entry_reg = ttk.Entry(registration_window)
    dob_entry_reg.grid(row=1, column=1, padx=10, pady=10)

    address_entry_reg = ttk.Entry(registration_window)
    address_entry_reg.grid(row=2, column=1, padx=10, pady=10)

    def register_athlete():
        athlete_name_reg = name_entry_reg.get()
        dob_reg = dob_entry_reg.get()
        address_reg = address_entry_reg.get()

        # Perform athlete registration logic here (e.g., store in a database)
        # For now, just show a messagebox with the registration details
        registration_details = f"Athlete Name: {athlete_name_reg}\nDate of Birth: {dob_reg}\nAddress: {address_reg}"
        messagebox.showinfo("Athlete Registration", registration_details)

    # Register button for athlete registration
    register_button = ttk.Button(registration_window, text="Register", command=register_athlete)
    register_button.grid(row=3, column=0, columnspan=2, pady=20)

# Create the main application window
app = tk.Tk()
app.title("Athlete Cost Calculator")

# Create and place widgets in the window
name_label = ttk.Label(app, text="Athlete Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

training_plan_label = ttk.Label(app, text="Training Plan:")
training_plan_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

weight_label = ttk.Label(app, text="Current Weight (kg):")
weight_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

competition_category_label = ttk.Label(app, text="Competition Category:")
competition_category_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

competitions_label = ttk.Label(app, text="Competitions Entered:")
competitions_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

private_coaching_hours_label = ttk.Label(app, text="Private Coaching Hours:")
private_coaching_hours_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")

# Entry widgets
name_entry = ttk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

training_plan_var = tk.StringVar()
training_plan_combobox = ttk.Combobox(app, textvariable=training_plan_var, values=["Beginner", "Intermediate", "Elite"])
training_plan_combobox.grid(row=1, column=1, padx=10, pady=10)

weight_entry = ttk.Entry(app)
weight_entry.grid(row=2, column=1, padx=10, pady=10)

# Combobox for competition category
competition_category_var = tk.StringVar()
competition_categories = ["Heavyweight Unlimited (Over 100)", "Light-Heavyweight 100", "Middleweight 90", "Light-Middleweight 81", "Lightweight 73", "Flyweight 66"]
competition_category_combobox = ttk.Combobox(app, textvariable=competition_category_var, values=competition_categories)
competition_category_combobox.grid(row=3, column=1, padx=10, pady=10)

# Spinbox for competitions
competitions_spinbox = ttk.Spinbox(app, from_=0, to=100)
competitions_spinbox.grid(row=4, column=1, padx=10, pady=10)

# Spinbox for private coaching hours
private_coaching_hours_spinbox = ttk.Spinbox(app, from_=0, to=10)
private_coaching_hours_spinbox.grid(row=5, column=1, padx=10, pady=10)

# Result label
result_label = ttk.Label(app, text="")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Calculate button
calculate_button = ttk.Button(app, text="Calculate", command=calculate_cost)
calculate_button.grid(row=7, column=0, columnspan=2, pady=20)

# Register button to open the registration window
register_button = ttk.Button(app, text="Register Athlete", command=open_registration_window)
register_button.grid(row=8, column=0, columnspan=2, pady=20)

# Start the application
app.mainloop()
