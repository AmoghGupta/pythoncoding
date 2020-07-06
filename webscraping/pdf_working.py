import PyPDF2

f = open("Working_Business_Proposal.pdf",'rb')

pdf_reader = PyPDF2.PdfFileReader(f)

#print(pdf_reader.numPages)

#reading a pdf file
page_one = pdf_reader.getPage(0)
#print(page_one.extractText())


pdf_writer= PyPDF2.PdfFileWriter()
print(type(pdf_writer))
pdf_writer.addPage(page_one)


pdf_output = open('newfile.pdf','wb')
pdf_writer.write(pdf_output)

#adding a page to PDF file

f.close()
pdf_output.close()