#!/usr/bin/env python3

import tkinter as tk
import subprocess
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # create label for "The last read value"
        self.last_value_label = tk.Label(self, text="The last read value")
        self.last_value_label.grid(row=0, column=0, padx=2, pady=5)

        # create textbox for last value
        self.last_value_entry = tk.Entry(self, width=10)
        self.last_value_entry.grid(row=0, column=1, padx=2, pady=5)

        # create label for "The predicted Ys are:"
        self.predicted_label = tk.Label(self, text="The predicted Ys are:")
        self.predicted_label.grid(row=1, column=0, padx=2, pady=5)

        # create label for RANK
        self.rank_label = tk.Label(self, text="RANK")
        self.rank_label.grid(row=2, column=0, padx=2, pady=5)

        # create label for SUM
        self.sum_label = tk.Label(self, text="SUM")
        self.sum_label.grid(row=3, column=0, padx=2, pady=5)

        # create label for Pop SD
        self.popsd_label = tk.Label(self, text="Pop SD")
        self.popsd_label.grid(row=4, column=0, padx=2, pady=5)

        # create label for VAR
        self.var_label = tk.Label(self, text="VAR")
        self.var_label.grid(row=5, column=0, padx=2, pady=5)


        ######################## create checkbox and textboxes for RANK  #######################
        self.rank_checkbox_var = tk.BooleanVar()
        self.rank_checkbox = tk.Checkbutton(self, text="", variable=self.rank_checkbox_var)
        self.rank_checkbox.grid(row=2, column=1, padx=2, pady=5)

        self.rank_mse_label = tk.Label(self, text="MSE:")
        self.rank_mse_label.grid(row=2, column=2, padx=2, pady=5)
        self.rank_mse_entry = tk.Entry(self, width=10)
        self.rank_mse_entry.grid(row=2, column=3, padx=2, pady=5)


        self.rank_sd_label = tk.Label(self, text="SD:")
        self.rank_sd_label.grid(row=2, column=4, padx=2, pady=5)
        self.rank_sd_entry = tk.Entry(self, width=10)
        self.rank_sd_entry.grid(row=2, column=5, padx=2, pady=5)

        self.rank_pred_label = tk.Label(self, text="Predicted +/- SD")
        self.rank_pred_label.grid(row=2, column=6, padx=2, pady=5)
        self.rank_pred_entry_from = tk.Entry(self, width=10)
        self.rank_pred_entry_from.grid(row=2, column=7, padx=2, pady=5)
        
        self.rank_pred_to_label = tk.Label(self, text="to")
        self.rank_pred_to_label.grid(row=2, column=8, padx=2, pady=5)
        self.rank_pred_entry_to = tk.Entry(self, width=10)
        self.rank_pred_entry_to.grid(row=2, column=9, padx=2, pady=5)



        ######################## create checkbox and textboxes for SUM  #######################
        self.sum_checkbox_var = tk.BooleanVar()
        self.sum_checkbox = tk.Checkbutton(self, text="", variable=self.sum_checkbox_var)
        self.sum_checkbox.grid(row=3, column=1, padx=2, pady=5)

        self.sum_mse_label = tk.Label(self, text="MSE:")
        self.sum_mse_label.grid(row=3, column=2, padx=2, pady=5)
        self.sum_mse_entry = tk.Entry(self, width=10)
        self.sum_mse_entry.grid(row=3, column=3, padx=2, pady=5)


        self.sum_sd_label = tk.Label(self, text="SD:")
        self.sum_sd_label.grid(row=3, column=4, padx=2, pady=5)
        self.sum_sd_entry = tk.Entry(self, width=10)
        self.sum_sd_entry.grid(row=3, column=5, padx=2, pady=5)

        self.sum_pred_label = tk.Label(self, text="Predicted +/- SD")
        self.sum_pred_label.grid(row=3, column=6, padx=2, pady=5)
        self.sum_pred_entry_from = tk.Entry(self, width=10)
        self.sum_pred_entry_from.grid(row=3, column=7, padx=2, pady=5)

        self.sum_pred_to_label = tk.Label(self, text="to")
        self.sum_pred_to_label.grid(row=3, column=8, padx=2, pady=5)
        self.sum_pred_entry_to = tk.Entry(self, width=10)
        self.sum_pred_entry_to.grid(row=3, column=9, padx=2, pady=5)


        ######################## create checkbox and textboxes for Pop SD  #######################
        self.popsd_checkbox_var = tk.BooleanVar()
        self.popsd_checkbox = tk.Checkbutton(self, text="", variable=self.popsd_checkbox_var)
        self.popsd_checkbox.grid(row=4, column=1, padx=2, pady=5)

        self.popsd_mse_label = tk.Label(self, text="MSE:")
        self.popsd_mse_label.grid(row=4, column=2, padx=2, pady=5)
        self.popsd_mse_entry = tk.Entry(self, width=10)
        self.popsd_mse_entry.grid(row=4, column=3, padx=2, pady=5)


        self.popsd_sd_label = tk.Label(self, text="SD:")
        self.popsd_sd_label.grid(row=4, column=4, padx=2, pady=5)
        self.popsd_sd_entry = tk.Entry(self, width=10)
        self.popsd_sd_entry.grid(row=4, column=5, padx=2, pady=5)

        self.popsd_pred_label = tk.Label(self, text="Predicted +/- SD")
        self.popsd_pred_label.grid(row=4, column=6, padx=2, pady=5)
        self.popsd_pred_entry_from = tk.Entry(self, width=10)
        self.popsd_pred_entry_from.grid(row=4, column=7, padx=2, pady=5)

        self.popsd_pred_to_label = tk.Label(self, text="to")
        self.popsd_pred_to_label.grid(row=4, column=8, padx=2, pady=5)
        self.popsd_pred_entry_to = tk.Entry(self, width=10)
        self.popsd_pred_entry_to.grid(row=4, column=9, padx=2, pady=5)


        ######################## create checkbox and textboxes for VAR  #######################
        self.var_checkbox_var = tk.BooleanVar()
        self.var_checkbox = tk.Checkbutton(self, text="", variable=self.var_checkbox_var)
        self.var_checkbox.grid(row=5, column=1, padx=2, pady=5)

        self.var_mse_label = tk.Label(self, text="MSE:")
        self.var_mse_label.grid(row=5, column=2, padx=2, pady=5)
        self.var_mse_entry = tk.Entry(self, width=10)
        self.var_mse_entry.grid(row=5, column=3, padx=2, pady=5)


        self.var_sd_label = tk.Label(self, text="SD:")
        self.var_sd_label.grid(row=5, column=4, padx=2, pady=5)
        self.var_sd_entry = tk.Entry(self, width=10)
        self.var_sd_entry.grid(row=5, column=5, padx=2, pady=5)

        self.var_pred_label = tk.Label(self, text="Predicted +/- SD")
        self.var_pred_label.grid(row=5, column=6, padx=2, pady=5)
        self.var_pred_entry_from = tk.Entry(self, width=10)
        self.var_pred_entry_from.grid(row=5, column=7, padx=2, pady=5)

        self.var_pred_to_label = tk.Label(self, text="to")
        self.var_pred_to_label.grid(row=5, column=8, padx=2, pady=5)
        self.var_pred_entry_to = tk.Entry(self, width=10)
        self.var_pred_entry_to.grid(row=5, column=9, padx=2, pady=5)



        # create start button
        self.start_button = tk.Button(self, text="Start", command=self.start_button_callback)
        self.start_button.grid(row=0, column=6, padx=2, pady=5)

        # create reset button
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_button_callback)
        self.reset_button.grid(row=0, column=7, padx=2, pady=5)

    def start_button_callback(self):

        ######################## RANK START #######################

        if self.rank_checkbox_var.get():
            import RANK
            Ypred, mse, std_dev, min_range, max_range = RANK.get_output()

            # update values in GUI
            self.last_value_entry.delete(0, tk.END)
            self.last_value_entry.insert(0, str(Ypred))

            self.rank_mse_entry.delete(0, tk.END)
            self.rank_mse_entry.insert(0, str(round(mse, 4)))            
            
            self.rank_sd_entry.delete(0, tk.END)
            self.rank_sd_entry.insert(0, str(round(std_dev, 4)))
            
            self.rank_pred_entry_from.delete(0, tk.END)
            self.rank_pred_entry_from.insert(0, str(round(min_range, 4)))
            
            self.rank_pred_entry_to.delete(0, tk.END)
            self.rank_pred_entry_to.insert(0, str(round(max_range, 4)))

        ######################## SUM START #######################

        elif self.sum_checkbox_var.get():
            import SUM
            Ypred, mse, std_dev, min_range, max_range = SUM.get_output()

            # update values in GUI
            self.last_value_entry.delete(0, tk.END)
            self.last_value_entry.insert(0, str(Ypred))

            self.sum_mse_entry.delete(0, tk.END)
            self.sum_mse_entry.insert(0, str(round(mse, 4)))

            self.sum_sd_entry.delete(0, tk.END)
            self.sum_sd_entry.insert(0, str(round(std_dev, 4)))
            
            self.sum_pred_entry_from.delete(0, tk.END)
            self.sum_pred_entry_from.insert(0, str(round(min_range, 4)))
            
            self.sum_pred_entry_to.delete(0, tk.END)
            self.sum_pred_entry_to.insert(0, str(round(max_range, 4)))

        ######################## RANK Pop SD #######################

        elif self.popsd_checkbox_var.get():
            import Pop_SD
            Ypred, mse, std_dev, min_range, max_range = Pop_SD.get_output()

            # update values in GUI
            self.last_value_entry.delete(0, tk.END)
            self.last_value_entry.insert(0, str(Ypred))

            self.popsd_mse_entry.delete(0, tk.END)
            self.popsd_mse_entry.insert(0, str(round(mse, 4)))

            self.popsd_sd_entry.delete(0, tk.END)
            self.popsd_sd_entry.insert(0, str(round(std_dev, 4)))
            
            self.popsd_pred_entry_from.delete(0, tk.END)
            self.popsd_pred_entry_from.insert(0, str(round(min_range, 4)))
            
            self.popsd_pred_entry_to.delete(0, tk.END)
            self.popsd_pred_entry_to.insert(0, str(round(max_range, 4)))

        ######################## VAR START #######################

        elif self.var_checkbox_var.get():
            import VAR
            Ypred, mse, std_dev, min_range, max_range = VAR.get_output()

            # update values in GUI
            self.last_value_entry.delete(0, tk.END)
            self.last_value_entry.insert(0, str(Ypred))

            self.var_mse_entry.delete(0, tk.END)
            self.var_mse_entry.insert(0, str(round(mse, 4)))

            self.var_sd_entry.delete(0, tk.END)
            self.var_sd_entry.insert(0, str(round(std_dev, 4)))
            
            self.var_pred_entry_from.delete(0, tk.END)
            self.var_pred_entry_from.insert(0, str(round(min_range, 4)))
            
            self.var_pred_entry_to.delete(0, tk.END)
            self.var_pred_entry_to.insert(0, str(round(max_range, 4)))






    def reset_button_callback(self):
        # clear all textboxes
        self.last_value_entry.delete(0, tk.END)

        self.rank_mse_entry.delete(0, tk.END)        
        self.rank_sd_entry.delete(0, tk.END)
        self.rank_pred_entry_from.delete(0, tk.END)
        self.rank_pred_entry_to.delete(0, tk.END)

        self.sum_mse_entry.delete(0, tk.END)        
        self.sum_sd_entry.delete(0, tk.END)
        self.sum_pred_entry_from.delete(0, tk.END)
        self.sum_pred_entry_to.delete(0, tk.END)

        self.popsd_mse_entry.delete(0, tk.END)        
        self.popsd_sd_entry.delete(0, tk.END)
        self.popsd_pred_entry_from.delete(0, tk.END)
        self.popsd_pred_entry_to.delete(0, tk.END)   

        self.var_mse_entry.delete(0, tk.END)        
        self.var_sd_entry.delete(0, tk.END)
        self.var_pred_entry_from.delete(0, tk.END)
        self.var_pred_entry_to.delete(0, tk.END)   

        
        # clear checkboxes
        self.rank_checkbox_var.set(False)
        self.sum_checkbox_var.set(False)
        self.popsd_checkbox_var.set(False)
        self.var_checkbox_var.set(False)



root = tk.Tk()
root.title("RANK, SUM, Pop_SD, VAR")
app = Application(master=root)
app.mainloop()
