import os, zipfile, tkinter as tk
from tkinter import filedialog, messagebox

def choose_folder():
    folder = filedialog.askdirectory(title="选择要打包的文件夹")
    if not folder:
        return
    save_path = filedialog.asksaveasfilename(
        title="保存为 svfzip",
        defaultextension=".svfzip",
        filetypes=[("SVFZIP 文件", "*.svfzip")],
        initialfile= os.path.basename(folder) + ".svfzip",
    )
    if save_path:
        make_svfzip(folder, save_path)

def make_svfzip(folder, out_path):
    try:
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(folder):
                for f in files:
                    abs_path = os.path.join(root, f)
                    if abs_path == out_path:
                        continue
                    rel_path = os.path.relpath(abs_path, folder)
                    zf.write(abs_path, rel_path)
        messagebox.showinfo("完成", f"已生成{out_path}")
    except Exception as e:
        messagebox.showerror("错误", str(e))

if __name__ == "__main__":
    tk.Tk().withdraw()
    choose_folder()