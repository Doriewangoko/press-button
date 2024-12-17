import customtkinter

# Set appearance mode and color theme
customtkinter.set_appearance_mode("System")  # Modes: "System" (default), "Light", "Dark"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# Create the main window
app = customtkinter.CTk()
app.geometry("240x240")
app.title("CustomTkinter Example")

# Define a callback function for the button
def button_callback():
    print("Button pressed")

# Create a button widget
button = customtkinter.CTkButton(master=app, text="Press Me", command=button_callback)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# Run the application
app.mainloop()
