# The main entry of our App
# Tkinter for building our graphics window
import tkinter as tk

# For processing PDF files
import PyPDF2

# For image processing/logo
from PIL import Image, ImageTk

# File dialog
from tkinter.filedialog import askopenfile


# Test 1
# print("Is this working?")

# initialize the main root window
root = tk.Tk()

# Create a canvas window from the main window
canvas = tk.Canvas(root, width=1280, height=720)

# Split the canvas into 3 identical invisible columns
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('logo_temp.jpg')
# Convert image to a TK image
logo = ImageTk.PhotoImage(logo)
# Place logo inside a label element
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(root, text="Select PDF File", font="OpenSans")
# Add this label below our logo but let is span all columns
instructions.grid(columnspan=3, column=0, row=1)


# Function/command to open the pdf
def open_pdf():
    browse_text.set("Loading ...")
    file = askopenfile(parent=root, mode='rb', title="Choose a File...", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        print('File was successfully opened...')
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)

        # Store the page content inside a text widget
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_config("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


    # print("Printing...")


# Browse button
# Store browse text in variable to use depending on state of app
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command=lambda: open_pdf(), font="OpenSans", bg="black", fg="white", height=5)
browse_text.set("Browse")
browse_button.grid(column=1, row=2)

canvas = tk.Canvas(root, width=1280, height=150)
canvas.grid(columnspan=3)


# Ensure the main graphic window is created
root.mainloop()

print("Welcome to Mad Lib Generator")


def main():
    # Getting user input
    noun = str(input("Please enter a noun: "))
    action = str(input("Please enter a action: "))
    colour = str(input("Please enter a colour: "))

    # Printing all the sentences
    print(noun, "was eating ice cream")
    print("While", action, "in the ocean")
    print("Which was", colour, "in colour")
    print("How is that true?")

    # Restart Function
    restart()


# Restart Function
def restart():
    replay = str(input("Would you like to replay the game? (y/n): "))  # Getting user input
    if replay == "y":  # Check if the input is equal to "y"
        main()  # If it is than run main() again
    elif replay == "n":  # Else if the input is "n"
        print("Goodbye!!")  # Print a goodbye message
        quit()  # Quit the programme
    else:  # Else if the input is not y or n then
        print("Please enter a correct input!!")  # Print a statement to the user
        restart()  # Repeat the Function


# Main game Loop
while True:
    main()
