from flask import Flask 
import requests
import PyPDF2 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'




def rotatepdf(url,page_number,angle):

    page_number -= 1

    # Download the pdf from the url 
    r = requests.get(url,allow_redirects=True)
    open('test.pdf','wb').write(r.content)

    # Open the pdf and manipulate the page

    ## 1. Open the Pdf
    pdf_in = open('test.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in,strict=False)
    pdf_writer = PyPDF2.PdfFileWriter()

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)

        if page_num == page_number:
            page.rotateClockwise(angle)
        pdf_writer.addPage(page)
        
    pdf_out = open('rotated.pdf','wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()

rotatepdf('https://bitcoin.org/bitcoin.pdf',2,180)