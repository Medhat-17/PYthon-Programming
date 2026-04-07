import tkinter as tk
from tkinter import scrolledtext, filedialog, simpledialog, messagebox
import json
import os
"""implmenteed hte whoel os from scratch 
"""
file_system = {
    'bin': {
        'notes': 'python_app_notes',
        'editor': 'python_app_editor',
        'calc': 'python_app_calc',
        'help': 'help_command',
    },
    'home': {
        'guest': {}
    }
}
current_dir_path = '/home/guest' 
def _get_path_parts(path):
    """Splits an absolute or relative path into components."""
    parts = []
    for part in path.split('/'):
        if part == '' or part == '.':
            continue
        elif part == '..':
            if parts:
                parts.pop()
        else:
            parts.append(part)
    return parts

def _resolve_path(base_path, path):
    """Resolves a relative path to an absolute path based on a given base_path."""
    if path.startswith('/'):
        return path
    else:
        return os.path.normpath(os.path.join(base_path, path))

def _traverse_path(fs, path_parts, create_if_missing_dir=False):
    """
    Traverses the file system tree.
    Returns (parent_dict, target_name, target_obj, success_boolean)
    target_obj will be None if target_name does not exist in parent_dict.
    """
    current_node = fs
    parent_node = None
    target_name = None

    for i, part in enumerate(path_parts):
        parent_node = current_node

        if i == len(path_parts) - 1:
            target_name = part
            target_obj = current_node.get(part)
            return parent_node, target_name, target_obj, True
        else:
            if part not in current_node:
                if create_if_missing_dir:
                    current_node[part] = {}
                else:
                    return None, None, None, False
            
            if not isinstance(current_node[part], dict):
                return None, None, None, False
            
            current_node = current_node[part]
            
    return current_node, None, current_node, True 
def cmd_ls(app_instance, args):
    """List directory contents."""
    path_to_list = args[0] if args else '.'
    abs_path = _resolve_path(app_instance.current_dir_path, path_to_list)
    path_parts = _get_path_parts(abs_path)

    parent_node, target_name, target_obj, success = _traverse_path(file_system, path_parts)

    if not success:
        return f"ls: cannot access '{path_to_list}': No such file or directory"
    
    if target_name is None:
        if not isinstance(target_obj, dict):
            return f"ls: '{path_to_list}': Not a directory"
        dir_content = target_obj
    else:
        if not isinstance(target_obj, dict):
            return target_name
        dir_content = target_obj

    if not dir_content:
        return "(empty directory)"
    
    items = []
    for name, content in dir_content.items():
        if isinstance(content, dict):
            items.append(f"{name}/")
        else:
            items.append(name)
    return "\n".join(sorted(items))

def cmd_cd(app_instance, args):
    """Change current directory."""
    if not args:
        return "cd: missing argument"
    
    new_path = args[0]
    resolved_path = _resolve_path(app_instance.current_dir_path, new_path)
    path_parts = _get_path_parts(resolved_path)

    parent_node, target_name, target_obj, success = _traverse_path(file_system, path_parts)

    if not success or (target_name is not None and not isinstance(target_obj, dict)):
        return f"cd: {new_path}: No such file or directory, or not a directory"
    
    if target_name is None and not isinstance(target_obj, dict):
        return f"cd: {new_path}: Not a directory"

    app_instance.current_dir_path = resolved_path
    app_instance.update_prompt()
    return ""

def cmd_mkdir(app_instance, args):
    """Create a new directory."""
    if not args:
        return "mkdir: missing operand"
    
    path = args[0]
    abs_path = _resolve_path(app_instance.current_dir_path, path)
    path_parts = _get_path_parts(abs_path)

    if not path_parts:
        return "mkdir: cannot create directory '/': File exists"

    parent_parts = path_parts[:-1]
    new_dir_name = path_parts[-1]

    parent_node, _, _, parent_success = _traverse_path(file_system, parent_parts)

    if not parent_success or not isinstance(parent_node, dict):
        return f"mkdir: cannot create directory '{path}': No such file or directory"
    
    if new_dir_name in parent_node:
        return f"mkdir: cannot create directory '{path}': File exists"
    
    parent_node[new_dir_name] = {}
    return f"Directory '{path}' created."

def cmd_touch(app_instance, args):
    """Create an empty file."""
    if not args:
        return "touch: missing operand"
    
    path = args[0]
    abs_path = _resolve_path(app_instance.current_dir_path, path)
    path_parts = _get_path_parts(abs_path)

    if not path_parts:
        return "touch: cannot create file '/': Is a directory"

    parent_parts = path_parts[:-1]
    file_name = path_parts[-1]

    parent_node, _, _, parent_success = _traverse_path(file_system, parent_parts)

    if not parent_success or not isinstance(parent_node, dict):
        return f"touch: cannot create file '{path}': No such file or directory"
    
    if file_name in parent_node and isinstance(parent_node[file_name], dict):
        return f"touch: cannot create file '{path}': Is a directory"
    
    parent_node[file_name] = ""
    return f"File '{path}' created."

def cmd_cat(app_instance, args):
    """Display file content."""
    if not args:
        return "cat: missing operand"
    
    path = args[0]
    abs_path = _resolve_path(app_instance.current_dir_path, path)
    path_parts = _get_path_parts(abs_path)

    parent_node, target_name, target_obj, success = _traverse_path(file_system, path_parts)

    if not success or target_name is None or target_obj is None:
        return f"cat: {path}: No such file or directory"
    
    if isinstance(target_obj, dict):
        return f"cat: {path}: Is a directory"
    
    return target_obj

def cmd_echo(app_instance, args):
    """Write text to a file or display it."""
    if not args:
        return "echo: missing argument"
    
    text = args[0]
    file_path = None
    
    if len(args) >= 3 and args[1] in ('>', '>>'):
        file_path = args[2]
        abs_file_path = _resolve_path(app_instance.current_dir_path, file_path)
        path_parts = _get_path_parts(abs_file_path)

        parent_parts = path_parts[:-1]
        file_name = path_parts[-1]

        parent_node, target_name, target_obj, parent_success = _traverse_path(file_system, parent_parts)

        if not parent_success or not isinstance(parent_node, dict):
            return f"echo: {file_path}: No such file or directory"
        
        if file_name in parent_node and isinstance(parent_node[file_name], dict):
            return f"echo: {file_path}: Is a directory"

        if args[1] == '>':
            parent_node[file_name] = text
        else:
            existing_content = parent_node.get(file_name, "")
            parent_node[file_name] = existing_content + text
        return ""
    else:
        return text

def cmd_rm(app_instance, args):
    """Remove a file or an empty directory."""
    if not args:
        return "rm: missing operand"
    
    path = args[0]
    abs_path = _resolve_path(app_instance.current_dir_path, path)
    path_parts = _get_path_parts(abs_path)

    if not path_parts:
        return "rm: cannot remove '/': Is a directory"

    parent_parts = path_parts[:-1]
    item_name = path_parts[-1]

    parent_node, _, _, parent_success = _traverse_path(file_system, parent_parts)

    if not parent_success or not isinstance(parent_node, dict):
        return f"rm: cannot remove '{path}': No such file or directory"
    
    if item_name not in parent_node:
        return f"rm: cannot remove '{path}': No such file or directory"

    target_obj = parent_node[item_name]
    
    if isinstance(target_obj, dict):
        if target_obj:
            return f"rm: cannot remove '{path}': Directory not empty"
        else:
            del parent_node[item_name]
            return f"Removed '{path}/'."
    else:
        del parent_node[item_name]
        return f"Removed '{path}'."

def cmd_pwd(app_instance, args):
    """Print working directory."""
    return app_instance.current_dir_path

def cmd_help(app_instance, args):
    """Display help message."""
    return """
Available commands:
  ls [path]             - List directory contents
  cd <path>             - Change current directory
  pwd                   - Print working directory
  mkdir <directory>     - Create a new directory
  touch <file>          - Create an empty file
  cat <file>            - Display file content
  echo <text> [>/>> file] - Display text or write/append to a file
  rm <file_or_dir>      - Remove a file or an empty directory
  notes                 - Launch the Notes application
  editor <file>         - Launch the Text Editor for a file
  calc                  - Launch the Calculator application
  help                  - Show this help message
  exit                  - Exit the OS
"""

# --- Helper for file content updates (used by apps) ---
def _update_file_content(base_path, path, content):
    """Helper to update a file's content after creation."""
    abs_path = _resolve_path(base_path, path)
    path_parts = _get_path_parts(abs_path)
    parent_parts = path_parts[:-1]
    file_name = path_parts[-1]

    parent_node, _, _, parent_success = _traverse_path(file_system, parent_parts, create_if_missing_dir=True)

    if not parent_success or not isinstance(parent_node, dict):
        return f"Error: Could not update file '{path}'. Parent directory not found or is a file."
    
    if file_name not in parent_node or not isinstance(parent_node[file_name], str):
        parent_node[file_name] = content
    else:
        parent_node[file_name] = content
    return "" # No error message on success


# --- Simulated Applications (Tkinter Windows) ---

class NotesApp:
    def __init__(self, master, app_instance):
        self.top = tk.Toplevel(master)
        self.top.title("Notes App")
        self.top.geometry("400x300")
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.app_instance = app_instance # Reference to the main OSApp

        self.notes_path = _resolve_path(self.app_instance.current_dir_path, "notes.txt")

        self.note_entry = tk.Entry(self.top, width=40)
        self.note_entry.pack(pady=5)

        self.add_button = tk.Button(self.top, text="Add Note", command=self.add_note)
        self.add_button.pack(pady=2)

        self.notes_text = scrolledtext.ScrolledText(self.top, width=40, height=10, state='disabled')
        self.notes_text.pack(pady=5)

        self.list_notes() # Initial list

    def _get_notes(self):
        notes_content = _traverse_path(file_system, _get_path_parts(self.notes_path))[2] or ""
        notes = []
        if notes_content:
            try:
                notes = json.loads(notes_content)
            except json.JSONDecodeError:
                notes = [notes_content] # Fallback for simple text notes
        return notes

    def _save_notes(self, notes):
        result = _update_file_content(self.app_instance.current_dir_path, "notes.txt", json.dumps(notes))
        if result:
            messagebox.showerror("Notes App Error", result)

    def add_note(self):
        note_text = self.note_entry.get().strip()
        if note_text:
            notes = self._get_notes()
            notes.append(note_text)
            self._save_notes(notes)
            self.note_entry.delete(0, tk.END)
            self.list_notes()
        else:
            messagebox.showwarning("Notes App", "Note cannot be empty.")

    def list_notes(self):
        self.notes_text.config(state='normal')
        self.notes_text.delete(1.0, tk.END)
        notes = self._get_notes()
        if notes:
            for i, note in enumerate(notes):
                self.notes_text.insert(tk.END, f"{i+1}. {note}\n")
        else:
            self.notes_text.insert(tk.END, "No notes yet.")
        self.notes_text.config(state='disabled')

    def on_closing(self):
        self.top.destroy()


class EditorApp:
    def __init__(self, master, app_instance, initial_file_path=""):
        self.top = tk.Toplevel(master)
        self.top.title(f"Editor: {initial_file_path or 'Untitled'}")
        self.top.geometry("600x400")
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.app_instance = app_instance

        self.current_file_path = _resolve_path(self.app_instance.current_dir_path, initial_file_path) if initial_file_path else ""

        self.text_area = scrolledtext.ScrolledText(self.top, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        button_frame = tk.Frame(self.top)
        button_frame.pack(fill='x', pady=5)

        tk.Button(button_frame, text="New", command=self.new_file).pack(side='left', padx=5)
        tk.Button(button_frame, text="Open", command=self.open_file_dialog).pack(side='left', padx=5)
        tk.Button(button_frame, text="Save", command=self.save_file).pack(side='left', padx=5)

        self.status_label = tk.Label(self.top, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side='bottom', fill='x')

        if self.current_file_path:
            self.load_file(self.current_file_path)
        else:
            self.update_status("New file.")

    def update_status(self, message):
        self.status_label.config(text=message)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file_path = ""
        self.top.title("Editor: Untitled")
        self.update_status("New file created.")

    def load_file(self, path):
        path_parts = _get_path_parts(path)
        _, _, content, success = _traverse_path(file_system, path_parts)
        if success and content is not None and not isinstance(content, dict):
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(1.0, content)
            self.current_file_path = path
            self.top.title(f"Editor: {os.path.basename(path)}")
            self.update_status(f"Opened '{os.path.basename(path)}'.")
        else:
            messagebox.showerror("Editor Error", f"Cannot open '{path}': File not found or is a directory.")
            self.new_file() # Revert to new file state

    def open_file_dialog(self):
        # Simulate file dialog by asking for file name
        file_name = simpledialog.askstring("Open File", "Enter file name (e.g., my_doc.txt):", parent=self.top)
        if file_name:
            # Assume files are in current_dir_path for simplicity or a 'documents' folder
            # For a real OS, this would involve browsing the file_system structure
            file_to_open = _resolve_path(self.app_instance.current_dir_path, file_name)
            self.load_file(file_to_open)

    def save_file(self):
        content = self.text_area.get(1.0, tk.END).strip()
        if not self.current_file_path:
            file_name = simpledialog.askstring("Save File As", "Enter file name (e.g., my_doc.txt):", parent=self.top)
            if not file_name:
                self.update_status("Save cancelled.")
                return
            self.current_file_path = _resolve_path(self.app_instance.current_dir_path, file_name)
        
        result = _update_file_content(self.app_instance.current_dir_path, self.current_file_path, content)
        if result:
            messagebox.showerror("Editor Error", result)
        else:
            self.top.title(f"Editor: {os.path.basename(self.current_file_path)}")
            self.update_status(f"File '{os.path.basename(self.current_file_path)}' saved.")

    def on_closing(self):
        self.top.destroy()


class CalculatorApp:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Calculator")
        self.top.geometry("300x200")
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.expression_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.result_var.set("Result: ")

        tk.Label(self.top, text="Expression:").pack(pady=5)
        tk.Entry(self.top, textvariable=self.expression_var, width=30).pack(pady=5)
        tk.Button(self.top, text="Calculate", command=self.calculate).pack(pady=5)
        tk.Label(self.top, textvariable=self.result_var, font=("Arial", 14)).pack(pady=5)

    def calculate(self):
        expression = self.expression_var.get()
        if not expression:
            self.result_var.set("Result: Enter an expression")
            return
        try:
            result = eval(expression) # WARNING: eval is dangerous in real apps!
            self.result_var.set(f"Result: {result}")
        except Exception as e:
            self.result_var.set(f"Error: {e}")

    def on_closing(self):
        self.top.destroy()


# --- Main OS Application (Tkinter) ---

class OSApp:
    def __init__(self, master):
        self.master = master
        master.title("Tiny PyOS GUI")
        master.geometry("800x600")
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.current_dir_path = '/home/guest' # Instance-specific current path

        # --- Top Frame for Prompt and Input ---
        self.input_frame = tk.Frame(master, bd=2, relief=tk.RAISED)
        self.input_frame.pack(side=tk.TOP, fill=tk.X, pady=5, padx=5)

        self.prompt_label = tk.Label(self.input_frame, text=self._get_prompt(), font=("Arial", 10, "bold"))
        self.prompt_label.pack(side=tk.LEFT, padx=5)

        self.command_entry = tk.Entry(self.input_frame, font=("Courier New", 10))
        self.command_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        self.command_entry.bind("<Return>", self.execute_command_from_entry)

        self.execute_button = tk.Button(self.input_frame, text="Execute", command=self.execute_command_from_entry)
        self.execute_button.pack(side=tk.RIGHT, padx=5)

        # --- Output Frame ---
        self.output_frame = tk.Frame(master, bd=2, relief=tk.SUNKEN)
        self.output_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx=5, pady=5)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD, state='disabled', font=("Courier New", 10), bg="#1e1e1e", fg="#00ff00")
        self.output_text.pack(expand=True, fill='both')
        self.app_frame = tk.Frame(master, bd=2, relief=tk.GROOVE)
        self.app_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=5, padx=5)

        tk.Button(self.app_frame, text="Notes", command=lambda: self.launch_app('notes')).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.app_frame, text="Editor", command=lambda: self.launch_app('editor')).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.app_frame, text="Calculator", command=lambda: self.launch_app('calc')).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.app_frame, text="Help", command=lambda: self.execute_command("help")).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.app_frame, text="Exit OS", command=self.on_closing).pack(side=tk.RIGHT, padx=5, pady=5)

        self.commands = {
            'ls': cmd_ls,
            'cd': cmd_cd,
            'mkdir': cmd_mkdir,
            'touch': cmd_touch,
            'cat': cmd_cat,
            'echo': cmd_echo,
            'rm': cmd_rm,
            'pwd': cmd_pwd,
            'help': cmd_help,
        }

        self.apps = {
            'notes': NotesApp,
            'editor': EditorApp,
            'calc': CalculatorApp,
        }

        self.write_output("--- Welcome to Tiny PyOS GUI! ---")
        self.write_output("Type commands in the input field, or launch apps below.")
        self.write_output("Type 'help' for a list of commands.")
        self.update_prompt()

    def _get_prompt(self):
        return f"guest@{self.current_dir_path}>"

    def update_prompt(self):
        self.prompt_label.config(text=self._get_prompt())

    def write_output(self, message):
        self.output_text.config(state='normal')
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.see(tk.END) # Scroll to bottom
        self.output_text.config(state='disabled')

    def execute_command_from_entry(self, event=None):
        command_line = self.command_entry.get().strip()
        self.write_output(f"$ {command_line}") # Echo command to output
        self.command_entry.delete(0, tk.END)

        if not command_line:
            return

        self.execute_command(command_line)

    def execute_command(self, command_line):
        parts = command_line.split(maxsplit=1)
        cmd = parts[0]
        args = parts[1].split() if len(parts) > 1 else []

        if cmd in self.commands:
            result = self.commands[cmd](self, args) # Pass app_instance to commands
            if result:
                self.write_output(result)
        elif cmd in self.apps:
            if cmd == 'editor' and len(args) > 0:
                EditorApp(self.master, self, args[0]) # Pass file path to editor
            else:
                self.apps[cmd](self.master, self) # Pass app_instance to app constructor if needed
        else:
            self.write_output(f"pyos: {cmd}: command not found")

    def launch_app(self, app_name):
        if app_name in self.apps:
            if app_name == 'editor':
                # For editor, we need to ask for a file or launch as untitled
                file_name = simpledialog.askstring("Editor", "Enter file to open (optional):", parent=self.master)
                if file_name is None: # Cancelled
                    return
                EditorApp(self.master, self, file_name)
            else:
                self.apps[app_name](self.master, self)
        else:
            self.write_output(f"Error: {app_name} is not a recognized application.")


    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit PyOS?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = OSApp(root)
    root.mainloop()
