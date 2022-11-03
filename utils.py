import qrcode
from fpdf import FPDF
from PDFRounded import PDFRounded as FPDF
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import VerticalGradiantColorMask
import constants


def set_pdf_global_values():
    pdf = FPDF(unit="pt", format=[constants.DOC_W, constants.DOC_H])
    pdf.set_margins(
        left=constants.MARGIN_L, top=constants.MARGIN_T, right=constants.MARGIN_R
    )
    pdf.add_page()
    pdf.add_font("beleren-bold_P1", fname="static/fonts/beleren-bold_P1.01.ttf")
    pdf.set_font(family="beleren-bold_P1", size=9)
    pdf.set_auto_page_break(False)

    return pdf


def create_qrcode_image(commander):
    c = commander

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(c.deck_url)

    if len(c.colors) == 1:
        img = qr.make_image(
            fill_color=(c.colors[0]["r"], c.colors[0]["g"], c.colors[0]["b"]),
        )
    elif len(c.colors) == 2:
        img = qr.make_image(
            image_factory=StyledPilImage,
            color_mask=VerticalGradiantColorMask(
                back_color=(255, 255, 255),
                top_color=(c.colors[0]["r"], c.colors[0]["g"], c.colors[0]["b"]),
                bottom_color=(c.colors[1]["r"], c.colors[1]["g"], c.colors[1]["b"]),
            ),
            # eye_drawer=RoundedModuleDrawer(),
        )
    elif len(c.colors) in (3, 4, 5):
        img = qr.make_image(
            fill_color=(
                constants.QR_CODE_COLOR["r"],
                constants.QR_CODE_COLOR["g"],
                constants.QR_CODE_COLOR["b"],
            ),
        )

    return img


def draw_mana_block(pdf, commander, x_coord, y_coord):
    c = commander

    y_offset = 10
    for color in c.colors:
        # draw the color blocks
        pdf.set_draw_color(color["r"], color["g"], color["b"])
        pdf.set_fill_color(color["r"], color["g"], color["b"])
        pdf.rect(
            x=x_coord - constants.CELL_BLEED,
            y=y_coord + y_offset,
            w=constants.CELL_W + (constants.CELL_BLEED * 2),
            h=16,
            style="FD",
        )
        # Overlay the mana symbols
        pdf.image(
            color["mana_svg"], w=8, h=8, x=x_coord + 128, y=y_coord + y_offset + 3.5
        )
        y_offset += 16

    return pdf
