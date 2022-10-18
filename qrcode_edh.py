import constants
import datetime
import math
import data_input
import utils
from fpdf import FPDF
from lib.PDFRounded import PDFRounded as FPDF

from slugify import slugify

commanders = data_input.commanders()

print('Total Commanders:', len(commanders))
print('This will use', math.ceil(len(commanders) / 3), 'rows.')
rows_max = math.ceil(len(commanders) / constants.DOC_COLS)

#Set global values for the PDF
pdf = FPDF(unit='pt', format=[constants.DOC_W,constants.DOC_H])
pdf.set_margins(left=constants.MARGIN_L, top=constants.MARGIN_T, right=constants.MARGIN_R)
pdf.add_page()
pdf.add_font('beleren-bold_P1', fname='static/fonts/beleren-bold_P1.01.ttf')
pdf.set_font(family='beleren-bold_P1', size=9)
pdf.set_auto_page_break(False)

row_count = 0
#Index counter for the list of commander objects
counter = 0

for row in range(0, rows_max):
    y_coord = constants.MARGIN_T + (constants.CELL_H * row_count) + (constants.MARGIN_VERT * row_count)
    col_count = 0
    for col in range(0, constants.DOC_COLS): 
        x_coord = (constants.MARGIN_L) + (constants.CELL_W * col_count) + (constants.MARGIN_HORIZ * col_count)
        if counter < len(commanders):
            #Create the QR code image
            img = utils.create_qrcode_image(commanders[counter])
            
            #Write image to disk
            qr_code_file_name = 'static/output/' + commanders[counter].name_slug + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'
            img.save(qr_code_file_name)

            #Draw mana symbol color blocks
            utils.draw_mana_block(pdf, commanders[counter], x_coord, y_coord)
            
            #Add a rounded white box for the QR to sit on
            pdf.set_draw_color(50,50,50)
            pdf.set_fill_color(255,255,255)
            pdf.rounded_rect(
                x=x_coord + 5,
                y=y_coord + 5,
                w=114,
                h=114,
                r=5,
                style='FD',
                corners='1234'
            )

            #Overlay the QR code image
            pdf.image(
                qr_code_file_name,
                x=x_coord + 7.5,
                y=y_coord + 7.5,
                w=109,
                h=109
            )

            #Add text at the bottom
            pdf.set_xy(
                x_coord + 5,
                y_coord + 128
            )
            pdf.set_text_color(constants.TEXT_COLOR['r'], constants.TEXT_COLOR['g'], constants.TEXT_COLOR['b'])
            pdf.cell(txt=commanders[counter].name, align='C')
            
            col_count += 1
            counter += 1
    row_count += 1

#Write the PDF to disk
pdf_file_name = 'qrcodes' + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'
pdf.output('static/output/' + pdf_file_name)