import customtkinter as ctk
import math
import numpy as np

class ScientificCalculator:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Scientific Calculato")
        self.window.geometry("400x600")
        self.window.configure(fg_color="#2b2b2b")
        
        # Set theme
        ctk.set_appearance_mode("white")
        ctk.set_default_color_theme("blue")
        
        # Display
        self.display = ctk.CTkEntry(
            self.window,
            width=380,
            height=60,
            font=("Arial", 24),
            justify="right",
            fg_color="#1a1a1a",
            text_color="white"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Scientific functions
        self.create_scientific_buttons()
        
        # Basic operations
        self.create_basic_buttons()
        
        # Memory
        self.memory = 0
        
    def create_scientific_buttons(self):
        scientific_functions = [
            ("sin", self.sin), ("cos", self.cos), ("tan", self.tan),
            ("√", self.sqrt), ("x²", self.square), ("x³", self.cube),
            ("log", self.log), ("ln", self.ln), ("π", self.pi),
            ("e", self.e), ("(", self.open_parenthesis), (")", self.close_parenthesis),
            ("C", self.clear), ("⌫", self.backspace), ("±", self.toggle_sign),
            ("MC", self.memory_clear), ("MR", self.memory_recall),
            ("M+", self.memory_add), ("M-", self.memory_subtract)
        ]
        
        for i, (text, command) in enumerate(scientific_functions):
            btn = ctk.CTkButton(
                self.window,
                text=text,
                width=90,
                height=50,
                font=("Arial", 16),
                command=command,
                fg_color="#3b3b3b",
                hover_color="#4b4b4b"
            )
            btn.grid(row=1 + i//4, column=i%4, padx=2, pady=2)
            
    def create_basic_buttons(self):
        basic_operations = [
            ("7", lambda: self.add_to_display("7")),
            ("8", lambda: self.add_to_display("8")),
            ("9", lambda: self.add_to_display("9")),
            ("/", lambda: self.add_to_display("/")),
            ("4", lambda: self.add_to_display("4")),
            ("5", lambda: self.add_to_display("5")),
            ("6", lambda: self.add_to_display("6")),
            ("*", lambda: self.add_to_display("*")),
            ("1", lambda: self.add_to_display("1")),
            ("2", lambda: self.add_to_display("2")),
            ("3", lambda: self.add_to_display("3")),
            ("-", lambda: self.add_to_display("-")),
            ("0", lambda: self.add_to_display("0")),
            (".", lambda: self.add_to_display(".")),
            ("=", self.calculate),
            ("+", lambda: self.add_to_display("+"))
        ]
        
        for i, (text, command) in enumerate(basic_operations):
            btn = ctk.CTkButton(
                self.window,
                text=text,
                width=90,
                height=50,
                font=("Arial", 16),
                command=command,
                fg_color="#3b3b3b",
                hover_color="#4b4b4b"
            )
            btn.grid(row=6 + i//4, column=i%4, padx=2, pady=2)
    
    def add_to_display(self, value):
        current = self.display.get()
        self.display.delete(0, "end")
        self.display.insert(0, current + value)
    
    def clear(self):
        self.display.delete(0, "end")
    
    def backspace(self):
        current = self.display.get()
        self.display.delete(0, "end")
        self.display.insert(0, current[:-1])
    
    def toggle_sign(self):
        current = self.display.get()
        if current and current[0] == "-":
            self.display.delete(0)
        else:
            self.display.insert(0, "-")
    
    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def sin(self):
        try:
            value = float(self.display.get())
            # Convert to radians and calculate sin
            result = math.sin(math.radians(value))
            # Round to 6 decimal places to avoid floating point issues
            result = round(result, 6)
            # If result is very close to 0, return 0
            if abs(result) < 1e-10:
                result = 0
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except ValueError:
            self.display.delete(0, "end")
            self.display.insert(0, "Error: Invalid Input")
        except Exception as e:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def cos(self):
        try:
            value = float(self.display.get())
            result = math.cos(math.radians(value))
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def tan(self):
        try:
            value = float(self.display.get())
            result = math.tan(math.radians(value))
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def sqrt(self):
        try:
            value = float(self.display.get())
            result = math.sqrt(value)
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def square(self):
        try:
            value = float(self.display.get())
            result = value ** 2
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def cube(self):
        try:
            value = float(self.display.get())
            result = value ** 3
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def log(self):
        try:
            value = float(self.display.get())
            result = math.log10(value)
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def ln(self):
        try:
            value = float(self.display.get())
            result = math.log(value)
            self.display.delete(0, "end")
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def pi(self):
        self.display.delete(0, "end")
        self.display.insert(0, str(math.pi))
    
    def e(self):
        self.display.delete(0, "end")
        self.display.insert(0, str(math.e))
    
    def open_parenthesis(self):
        self.add_to_display("(")
    
    def close_parenthesis(self):
        self.add_to_display(")")
    
    def memory_clear(self):
        self.memory = 0
    
    def memory_recall(self):
        self.display.delete(0, "end")
        self.display.insert(0, str(self.memory))
    
    def memory_add(self):
        try:
            value = float(self.display.get())
            self.memory += value
            self.display.delete(0, "end")
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def memory_subtract(self):
        try:
            value = float(self.display.get())
            self.memory -= value
            self.display.delete(0, "end")
        except:
            self.display.delete(0, "end")
            self.display.insert(0, "Error")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = ScientificCalculator()
    calculator.run() 