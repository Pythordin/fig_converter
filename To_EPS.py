import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import ctypes

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    entry_file.delete(0, tk.END)  # テキストボックスをクリア
    entry_file.insert(0, file_path)  # 選択されたファイルのパスを挿入

def select_save_location():
    save_path = filedialog.askdirectory()
    entry_save.delete(0, tk.END)  # テキストボックスをクリア
    entry_save.insert(0, save_path)  # 選択された保存場所のパスを挿入

def convert_to_eps():
    image_path = entry_file.get()  # テキストボックスから画像ファイルのパスを取得
    save_path = entry_save.get()  # テキストボックスから保存場所のパスを取得
    image_name = entry_image_name.get()  # テキストボックスから画像ファイル名を取得
    if image_path and save_path and image_name:
        eps_path = save_path + "/" + image_name + ".eps"  # 保存場所とファイル名を結合してEPSファイルのパスを作成
        image = Image.open(image_path)
        # 画像形式に応じて変換
        if image.format == 'JPEG':
            # JPEG画像をRGBモードに変換
            image = image.convert('RGB')
        elif image.format == 'PNG':
            # PNG画像をRGBモードに変換
            if image.mode == 'RGBA':
                image = image.convert('RGB')
        # 画像をEPSに変換して保存
        image.save(eps_path, 'EPS')
        messagebox.showinfo("Conversion Complete", "Image to EPS conversion completed successfully!")  # 変換完了のメッセージを表示

# GUIのセットアップ
ctypes.windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
root.title("Image to EPS Converter")

# ファイル選択ボタン
select_button = tk.Button(root, text="Select Image File", command=select_file)
select_button.grid(row=0, column=0, padx=5, pady=5)

# ファイルパスを表示するテキストボックス
entry_file = tk.Entry(root, width=50)
entry_file.grid(row=0, column=1, padx=5, pady=5)

# 保存場所選択ボタン
select_save_button = tk.Button(root, text="Select Save Location", command=select_save_location)
select_save_button.grid(row=1, column=0, padx=5, pady=5)

# 保存場所を表示するテキストボックス
entry_save = tk.Entry(root, width=50)
entry_save.grid(row=1, column=1, padx=5, pady=5)

# EPSファイル名を入力するエントリー
label_image_name = tk.Label(root, text="EPS File Name:")
label_image_name.grid(row=2, column=0, padx=5, pady=5)
entry_image_name = tk.Entry(root, width=30)
entry_image_name.grid(row=2, column=1, padx=5, pady=5)

# 変換ボタン
convert_button = tk.Button(root, text="Convert to EPS", command=convert_to_eps)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# GUIのメインループ
root.mainloop()
