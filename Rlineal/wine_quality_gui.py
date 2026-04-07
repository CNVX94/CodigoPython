# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class WineQualityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wine Quality Predictor")
        self.root.geometry("550x750")
        self.root.resizable(False, False)
        self.root.minsize(450, 650)
        
        self.model = None
        self.feature_columns = None
        
        self.setup_ui()
        self.train_model()
    
    def setup_ui(self):
        title_label = tk.Label(
            self.root, 
            text="🍷 Wine Quality Predictor 🍷",
            font=("Helvetica", 18, "bold"),
            fg="#722F37"
        )
        title_label.pack(pady=15)
        
        subtitle = tk.Label(
            self.root,
            text="Enter wine parameters to predict quality",
            font=("Helvetica", 10),
            fg="gray"
        )
        subtitle.pack(pady=(0, 15))
        
        self.create_input_fields()
        self.create_buttons()
        self.create_result_area()
    
    def create_input_fields(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.entries = {}
        
        self.feature_labels = [
            ("Fixed Acidity", "fixed acidity"),
            ("Volatile Acidity", "volatile acidity"),
            ("Citric Acid", "citric acid"),
            ("Residual Sugar", "residual sugar"),
            ("Chlorides", "chlorides"),
            ("Free Sulfur Dioxide", "free sulfur dioxide"),
            ("Total Sulfur Dioxide", "total sulfur dioxide"),
            ("Density", "density"),
            ("pH", "pH"),
            ("Sulphates", "sulphates"),
            ("Alcohol", "alcohol")
        ]
        
        self.default_values = {
            "fixed acidity": 7.0,
            "volatile acidity": 0.27,
            "citric acid": 0.36,
            "residual sugar": 2.4,
            "chlorides": 0.087,
            "free sulfur dioxide": 11.0,
            "total sulfur dioxide": 34.0,
            "density": 0.997,
            "pH": 3.39,
            "sulphates": 0.66,
            "alcohol": 9.9
        }
        
        for idx, (label_text, key) in enumerate(self.feature_labels):
            row = idx // 2
            col = (idx % 2) * 2
            
            label = ttk.Label(frame, text=f"{label_text}:", font=("Helvetica", 10))
            label.grid(row=row, column=col, sticky=tk.W, padx=5, pady=5)
            
            entry = ttk.Entry(frame, width=15, font=("Helvetica", 10))
            entry.grid(row=row, column=col+1, padx=5, pady=5)
            entry.insert(0, str(self.default_values[key]))
            
            self.entries[key] = entry
    
    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(fill=tk.X, pady=15, padx=20)
        
        predict_btn = tk.Button(
            button_frame,
            text="🔮 Predict Quality",
            font=("Helvetica", 12, "bold"),
            bg="#722F37",
            fg="white",
            activebackground="#8B3A3A",
            activeforeground="white",
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.predict_quality
        )
        predict_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            font=("Helvetica", 10),
            padx=15,
            pady=5,
            cursor="hand2",
            command=self.clear_fields
        )
        clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
    
    def create_result_area(self):
        result_frame = ttk.LabelFrame(self.root, text="Prediction Result", padding="15")
        result_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.quality_label = tk.Label(
            result_frame,
            text="Enter values and click Predict",
            font=("Helvetica", 14),
            fg="gray"
        )
        self.quality_label.pack(pady=10)
        
        self.status_label = tk.Label(
            result_frame,
            text="",
            font=("Helvetica", 16, "bold")
        )
        self.status_label.pack(pady=10, fill=tk.BOTH, expand=True)
    
    def train_model(self):
        try:
            df = pd.read_csv("WineQT.csv")
            df = df.iloc[:, :-1]
            
            self.feature_columns = [col for col in df.columns if col != 'quality' and col != 'Id']
            
            X = df[self.feature_columns]
            y = df['quality']
            
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            self.model = LinearRegression()
            self.model.fit(X_train, y_train)
            
            self.model.score(X_test, y_test)
            
        except FileNotFoundError:
            messagebox.showerror("Error", "WineQT.csv not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to train model: {str(e)}")
    
    def predict_quality(self):
        if not self.model:
            messagebox.showerror("Error", "Model not loaded!")
            return
        
        try:
            values = []
            for _, key in self.feature_labels:
                entry = self.entries[key]
                value = float(entry.get())
                values.append(value)
            
            prediction = self.model.predict([values])[0]
            
            quality_score = max(0, min(10, round(prediction, 2)))
            
            self.quality_label.config(
                text=f"Predicted Quality Score: {quality_score}",
                fg="#333333"
            )
            
            if quality_score >= 7:
                self.status_label.config(
                    text="✅ QUALITY WINE",
                    fg="#228B22",
                    bg="#90EE90"
                )
            elif quality_score >= 5:
                self.status_label.config(
                    text="⚠️ AVERAGE WINE",
                    fg="#FFA500",
                    bg="#FFE4B5"
                )
            else:
                self.status_label.config(
                    text="❌ LOW QUALITY",
                    fg="#DC143C",
                    bg="#FFB6C1"
                )
            
            self.status_label.config(bg=self.status_label.cget("bg"))
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values!")
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {str(e)}")
    
    def clear_fields(self):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, str(self.default_values[key]))
        
        self.quality_label.config(text="Enter values and click Predict", fg="gray")
        self.status_label.config(text="", bg=self.root.cget("bg"))

def main():
    root = tk.Tk()
    app = WineQualityApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
