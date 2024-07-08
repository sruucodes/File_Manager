# file_management_tool.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from file_management import list_files, sort_files, rename_files, organize_files_by_type

class FileManagementTool:
    def __init__(self, root):
        self.root = root
        self.root.title("File Management Tool")
        self.root.geometry("450x350")
        
        self.directory = None
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame for folder selection
        folder_frame = ttk.Frame(self.root, padding="10")
        folder_frame.pack(fill=tk.X)
        
        self.folder_label = ttk.Label(folder_frame, text="No folder selected", width=50, anchor="w")
        self.folder_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.select_button = ttk.Button(folder_frame, text="Select Folder", command=self.select_folder)
        self.select_button.pack(side=tk.RIGHT)
        
        # Frame for sorting options
        sort_frame = ttk.LabelFrame(self.root, text="Sort Options", padding="10")
        sort_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        
        self.sort_var = tk.StringVar(value="name")
        self.sort_options = ["name", "date", "type", "size"]
        
        for option in self.sort_options:
            rb = ttk.Radiobutton(sort_frame, text=option.capitalize(), variable=self.sort_var, value=option)
            rb.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Frame for rename option
        rename_frame = ttk.Frame(self.root, padding="10")
        rename_frame.pack(fill=tk.X)
        
        self.rename_var = tk.BooleanVar()
        self.rename_check = ttk.Checkbutton(rename_frame, text="Rename all files", variable=self.rename_var)
        self.rename_check.pack(side=tk.LEFT, padx=(0, 10))
        
        self.rename_pattern_entry = ttk.Entry(rename_frame)
        self.rename_pattern_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.rename_pattern_entry.insert(0, "file_###")  # Default rename pattern
        
        # Frame for organize option
        organize_frame = ttk.Frame(self.root, padding="10")
        organize_frame.pack(fill=tk.X)
        
        self.organize_var = tk.BooleanVar()
        self.organize_check = ttk.Checkbutton(organize_frame, text="Organize files by type", variable=self.organize_var)
        self.organize_check.pack(side=tk.LEFT, padx=(0, 10))
        
        # Frame for run button
        run_frame = ttk.Frame(self.root, padding="10")
        run_frame.pack(fill=tk.X)
        
        self.run_button = ttk.Button(run_frame, text="Run", command=self.run)
        self.run_button.pack(pady=10)
    
    def select_folder(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.folder_label.config(text=self.directory)
    
    def sort_files(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a folder first")
            return
        
        files = list_files(self.directory)
        sorted_files = sort_files(files, self.directory, self.sort_var.get())
        
        messagebox.showinfo("Sorted Files", "\n".join(sorted_files))
    
    def run(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a folder first")
            return
        
        files = list_files(self.directory)
        sorted_files = sort_files(files, self.directory, self.sort_var.get())
        
        if self.rename_var.get():
            rename_pattern = self.rename_pattern_entry.get()
            rename_files(sorted_files, self.directory, rename_pattern)
            messagebox.showinfo("Success", "Files renamed successfully")
        
        if self.organize_var.get():
            organize_files_by_type(sorted_files, self.directory)
            messagebox.showinfo("Success", "Files organized by type successfully")
        
        if not self.rename_var.get() and not self.organize_var.get():
            messagebox.showinfo("Success", "Files sorted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagementTool(root)
    root.mainloop()
