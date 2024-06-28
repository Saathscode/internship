import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        self.task_var = tk.StringVar()

        # Create UI Elements
        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, height=15, width=60)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.complete_task_button = tk.Button(self.root, text="Mark as Complete", command=self.complete_task)
        self.complete_task_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.save_tasks_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Load tasks from file if exists
        self.load_tasks()

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.itemconfig(index, {'fg': 'gray'})
            # Optionally, you can move completed tasks to a separate list or mark them differently.
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task = line.strip()
                    self.tasks.append(task)
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass  # No saved tasks yet

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
