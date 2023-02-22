from docx2pdf import convert
import glob

all_docx = glob.glob('*.docx')
for file_name in all_docx:
	pdf_name = f'{file_name.split(".")[0]}.pdf'
	convert(file_name,pdf_name)