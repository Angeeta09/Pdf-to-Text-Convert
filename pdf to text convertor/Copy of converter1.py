import PyPDF2
import os

if not os.path.isdir("temp"):
    os.mkdir("temp")

txtpath = ""
pdfpath = ""

# Input paths
pdfpath = input("Enter the name of your pdf file - please use backslash when typing in directory path: ").strip().replace('\\', '/')
txtpath = input("Enter the name of your txt file - please use backslash when typing in directory path: ").strip().replace('\\', '/')

BASEDIR = os.path.realpath("temp") # Base directory for text file if no specific path is provided
print(BASEDIR)

# If no txt path is provided, create a default output file in 'temp' directory
if len(txtpath) == 0:
    txtpath = os.path.join(BASEDIR, os.path.basename(os.path.normpath(pdfpath)).replace(".pdf", "") + ".txt")

# Open the PDF file
with open(pdfpath, 'rb') as pdfobj:
    # Use PdfReader instead of PdfFileReader
    pdfread = PyPDF2.PdfReader(pdfobj)
    x = len(pdfread.pages)  # Get the number of pages in the PDF

    # Iterate through each page of the PDF
    for i in range(x):
        page = pdfread.pages[i]
        text = page.extract_text()  # Extract the text from the current page

        # Write the extracted text to the output file
        with open(txtpath, 'a+', encoding="utf-8") as f: 
            f.write(text)
        print(text)  # Optionally print the text being written to the output file
