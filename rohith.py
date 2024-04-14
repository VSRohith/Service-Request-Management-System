import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Define the main application class
class ProServeApp:
    def __init__(self, master):
        self.master = master
        master.geometry('200x100')  # Set initial window size
        master.title("ProServe Solutions App")  # Set window title
        # Create a login button
        self.login_button = tk.Button(master, text="Login", command=self.open_login_window)
        self.login_button.pack()
        # Variable to keep track of login window state
        self.login_window_open = False
    # Method to open login window
    def open_login_window(self):
        if not self.login_window_open:
            self.login_window_open = True
            self.login()
    # Method to create login window
    def login(self):
        login_window = tk.Toplevel(self.master)  # Create a new window
        login_window.title("Login")  # Set window title
        login_window.geometry('400x300')  # Set window size       
        # Username label and entry
        self.username_label = tk.Label(login_window, text="Username:")
        self.username_label.grid(row=0, column=0)
        self.username_entry = tk.Entry(login_window)
        self.username_entry.grid(row=0, column=1)
        # Password label and entry
        self.password_label = tk.Label(login_window, text="Password:")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(login_window, show="*")
        self.password_entry.grid(row=1, column=1)
        # Login button
        self.login_button = tk.Button(login_window, text="Login", command=self.check_login)
        self.login_button.grid(row=2, columnspan=2)
        # Close login window event
        login_window.protocol("WM_DELETE_WINDOW", self.close_login_window)
    # Method to close login window
    def close_login_window(self):
        self.login_window_open = False
    # Method to validate login credentials
    def check_login(self):
        # Replace this with your actual login validation logic
        if self.username_entry.get() == "admin" and self.password_entry.get() == "admin":
            messagebox.showinfo("Login Successful", "Login successful!")  # Show success message
            self.show_services()  # Call method to show available services
        else:
            messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")  # Show error message
    # Method to display available services
    def show_services(self):
        services_window = tk.Toplevel(self.master)  # Create a new window
        services_window.title("Available Services")  # Set window title
        services_window.geometry('400x300')  # Set window size
        # Label for selecting service
        self.services_label = tk.Label(services_window, text="Select a service:")
        self.services_label.pack()
        # List of available services
        self.service_options = ["Cleaning", "Plumbing", "Electrician", "Beauty Services", "Massage", "Pest Control"]
        self.selected_service = tk.StringVar()
        self.selected_service.set(self.service_options[0])
        # Combobox for selecting service
        self.service_combobox = ttk.Combobox(services_window, textvariable=self.selected_service, values=self.service_options)
        self.service_combobox.pack()
        # Submit button
        self.submit_button = tk.Button(services_window, text="Submit", command=self.get_user_details)
        self.submit_button.pack()
    # Method to get user details
    def get_user_details(self):
        user_details_window = tk.Toplevel(self.master)  # Create a new window
        user_details_window.title("User Details")  # Set window title
        user_details_window.geometry('400x300')  # Set window size
        # Address label and entry
        self.address_label = tk.Label(user_details_window, text="Address:")
        self.address_label.grid(row=0, column=0)
        self.address_entry = tk.Entry(user_details_window)
        self.address_entry.grid(row=0, column=1)
        # Phone number label and entry
        self.phone_label = tk.Label(user_details_window, text="Phone number:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(user_details_window)
        self.phone_entry.grid(row=1, column=1)
        # Confirm button
        self.confirm_button = tk.Button(user_details_window, text="Confirm", command=self.confirm_service)
        self.confirm_button.grid(row=2, columnspan=2)
    # Method to confirm the selected service
    def confirm_service(self):
        messagebox.showinfo("Service Requested", "Your service request for {} will be processed soon. Thank you!".format(self.selected_service.get()))
# Create the root window
root = tk.Tk()
app = ProServeApp(root)  # Initialize the application
root.mainloop()  # Start the event loop
