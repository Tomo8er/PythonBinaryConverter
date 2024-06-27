import tkinter as tk
from tkinter import messagebox, filedialog

def convert_to_binary(text):
    binary_result = ""
    for char in text:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]
        binary_result += binary_value.zfill(8)
    return binary_result

def convert_and_display():
    user_input = input_text.get("1.0", "end-1c")
    binary_output = convert_to_binary(user_input)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", binary_output)

def save_to_file():
    binary_output = output_text.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(binary_output)
        messagebox.showinfo("File Saved", f"ファイルが {file_path} に保存されました。")

root = tk.Tk()
root.title("Text to Binary Converter")

input_label = tk.Label(root, text="テキストを入力してください:")
input_label.pack()

input_text = tk.Text(root, height=10, width=50)  
input_text.pack()

convert_button = tk.Button(root, text="変換して表示", command=convert_and_display)
convert_button.pack()

output_label = tk.Label(root, text="二進数表現:")
output_label.pack()

output_text = tk.Text(root, height=10, width=50)  
output_text.pack()

save_button = tk.Button(root, text="ファイルに保存", command=save_to_file)
save_button.pack()

root.mainloop()
