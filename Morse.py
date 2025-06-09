import tkinter as tk  # Import Tkinter library for GUI

# Dictionary to translate letters, numbers, and punctuation to Morse code
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'  # Space is translated as '/'
}

# Dictionary to replace accented letters with non-accented versions
accented = {
    'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
    'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
    'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U',
    'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
    'Ã': 'A', 'Õ': 'O', 'Ñ': 'N', 'Ç': 'C'
}

# Inverse dictionary to translate Morse code back to letters
morse_inv = {v: k for k, v in morse.items()}

def text_to_morse(text):
    """Convert normal text to Morse code"""
    text = text.upper()  # Convert text to uppercase
    # Replace accented characters with their non-accented versions
    text = ''.join(accented.get(c, c) for c in text)
    # Translate each character to Morse and join them with spaces
    return ' '.join(morse[c] for c in text if c in morse)

def morse_to_text(code):
    """Convert Morse code to normal text"""
    words = code.strip().split(' / ')  # Separate Morse words by '/'
    result = []
    for word in words:
        letters = word.split()  # Separate letters by spaces
        # Translate each Morse code letter to text and join to form the word
        text_word = ''.join(morse_inv.get(letter, '') for letter in letters)
        result.append(text_word)
    # Join words with spaces
    return ' '.join(result)

def translate():
    """Handle translation when button is clicked"""
    input_text = entry.get()  # Get text from input field
    mode = mode_var.get()     # Get selected translation mode
    output.config(state='normal')  # Enable editing in output field
    output.delete(1.0, tk.END)      # Clear previous output

    # Translate depending on selected mode
    if mode == "Text to Morse":
        result = text_to_morse(input_text)
    else:
        result = morse_to_text(input_text)

    output.insert(tk.END, result)  # Show result in output text area
    output.config(state='disabled')  # Disable editing in output field

# Main window setup
root = tk.Tk()
root.title("Morse Code Translator <-> Text")

# Variable to store selected translation mode
mode_var = tk.StringVar(value="Text to Morse")

# Radio buttons to select translation mode
tk.Radiobutton(root, text="Text to Morse", variable=mode_var, value="Text to Morse").pack(anchor='w')
tk.Radiobutton(root, text="Morse to Text", variable=mode_var, value="Morse to Text").pack(anchor='w')

# Label and input field for user text or Morse code
tk.Label(root, text="Enter text or Morse code:").pack(pady=5)
entry = tk.Entry(root, width=60)
entry.pack(pady=5)

# Button to perform translation
button = tk.Button(root, text="Translate", command=translate)
button.pack(pady=5)

# Text area to show translation output (read-only)
output = tk.Text(root, height=6, width=60, state='disabled')
output.pack(pady=5)

# Run the application
root.mainloop()
