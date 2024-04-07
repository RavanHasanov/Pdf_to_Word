from pdf2docx import Converter

pdf_path=""
docx_path=""

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()

