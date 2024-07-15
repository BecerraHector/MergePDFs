import PyPDF2

# PDF files to merge
files = ['file1.pdf', 'file2.pdf', 'file3.pdf']

output_filename = 'output_file.pdf'

merged_pdf = PyPDF2.PdfMerger()

for file in files:
    merged_pdf.append(file)

merged_pdf.write(output_filename)
merged_pdf.close()
