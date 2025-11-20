#!/usr/bin/env python3

from pyfiglet import Figlet
import tkinter as tk
import argparse

def copy_to_clipboard(text: str):
    """Copy text ke clipboard."""
    root = tk.Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    root.destroy()

def ascii_art(text: str, font: str = "standard"):
    """Buat ASCII art dari teks dengan font tertentu."""
    f = Figlet(font=font)
    return f.renderText(text)

def main():
    parser = argparse.ArgumentParser(
        description="Generate ASCII art dari teks dan bisa disalin."
    )
    parser.add_argument(
        "-t", "--text", required=True, help="Teks yang ingin diubah jadi ASCII art."
    )
    parser.add_argument(
        "-f", "--font", default="standard", help="Font FIGlet yang digunakan."
    )
    parser.add_argument(
        "--copy", action="store_true", help="Salin hasil ASCII art ke clipboard."
    )

    args = parser.parse_args()

    art = ascii_art(args.text, args.font)
    print(art)

    if args.copy:
        copy_to_clipboard(art)
        print("(Hasil disalin ke clipboard)")

if __name__ == "__main__":
    main()
