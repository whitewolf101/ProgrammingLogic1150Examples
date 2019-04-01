import docx

document = docx.Document()

document.add_paragraph('Hello Word!')

document.save('hello_word.docx')

