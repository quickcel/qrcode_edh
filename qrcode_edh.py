import qrcode
import constants
import datetime
from fpdf import FPDF
from PDFRounded import PDFRounded as FPDF
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
from slugify import slugify

'''
START INPUTS
Customize values below based on your commander
'''
deck_url = 'https://archidekt.com/decks/1709090'

commander_name = 'Skullbriar, the Walking Grave'
#commander_name = 'Thassa, Deep-Dwelling'
#commander_name = 'Marchesa, the Black Rose'

#Commander Colors
commander_colors = []
commander_colors.append(constants.WHITE)
commander_colors.append(constants.BLUE)
commander_colors.append(constants.BLACK)
commander_colors.append(constants.RED)
commander_colors.append(constants.GREEN)

#Most times you don't want to print a whole sheet.
#Specify a sheet position if you just want a single code
position = [0, 2]
#position = 'all' 

#Color of commander text underneath the code
text_color = {
    'r':constants.BLACK['r'],
    'g':constants.BLACK['g'],
    'b':constants.BLACK['b']
}

#QR Code Color: Used for 3+ color commanders
qr_code_color = {
    'r':constants.BLACK['r'],
    'g':constants.BLACK['g'],
    'b':constants.BLACK['b']   
}
'''
END INPUTS
'''

output_file_prefix = slugify(commander_name)
qr_code_file_name = 'static/output/' + output_file_prefix + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.png'
pdf_file_name = output_file_prefix + '-' + datetime.datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'


pdf_page_w = 612
pdf_page_h = 792

margin_top = 46.44
margin_right = 45
margin_bottom = 46.44
margin_left = 45

margin_horizontal = 45
margin_vertical = 41.04

cell_w = 144
cell_h = 144

bleed = 9

cols = 3
rows = 4

pdf = FPDF(unit='pt', format=[pdf_page_w,pdf_page_h])
pdf.set_margins(left=margin_left, top=margin_top, right=margin_right)
pdf.add_page()
pdf.add_font('beleren-bold_P1', fname='static/fonts/beleren-bold_P1.01.ttf')
pdf.set_font(family='beleren-bold_P1', size=9)
pdf.set_auto_page_break(False)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(deck_url)

if len(commander_colors) == 1:
    img = qr.make_image(
        fill_color=(commander_colors[0]['r'], commander_colors[0]['g'], commander_colors[0]['b']),
    )    
elif len(commander_colors) == 2:
    img = qr.make_image(
        image_factory=StyledPilImage,
        color_mask=VerticalGradiantColorMask(
            back_color=(255,255,255),
            top_color=(commander_colors[0]['r'], commander_colors[0]['g'], commander_colors[0]['b']),
            bottom_color=(commander_colors[1]['r'], commander_colors[1]['g'], commander_colors[1]['b'])
        ),
        #eye_drawer=RoundedModuleDrawer(),
        )
elif len(commander_colors) in (3,4,5):
    img = qr.make_image(
        fill_color=(qr_code_color['r'], qr_code_color['g'], qr_code_color['b']),
    )

img.save(qr_code_file_name)

row_count = 0
for row in range(0, rows):
    y_coord = margin_top + (cell_h * row_count) + (margin_vertical * row_count)
    col_count = 0
    for col in range(0, cols): 
        x_coord = (margin_left) + (cell_w * col_count) + (margin_horizontal * col_count)       
        if position == [row, col] or position == 'all':
            y_offset = 10
            for color in commander_colors:
                #draw the color blocks
                pdf.set_draw_color(color['r'], color['g'], color['b'])
                pdf.set_fill_color(color['r'], color['g'], color['b'])
                pdf.rect(
                    x=x_coord - bleed,
                    y=y_coord + y_offset,
                    w=cell_w + (bleed * 2),
                    h=16,
                    style='FD'
                )
                #Overlay the mana symbols
                pdf.image(
                    color['mana_svg'],
                    w=8, h=8,
                    x=x_coord + 128,
                    y=y_coord + y_offset + 3.5
                )
                y_offset += 16

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

            #Overlay the QR code
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
            pdf.set_text_color(text_color['r'], text_color['g'], text_color['b'])
            pdf.cell(txt=commander_name, align='C')
        else:
            pass
        col_count += 1
    row_count += 1

#Write the PDF to disk
pdf.output('static/output/' + pdf_file_name)