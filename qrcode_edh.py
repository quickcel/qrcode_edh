import constants
import datetime
import math
import data_input
import utils

commanders = data_input.commanders()
rows_max = math.ceil(len(commanders) / constants.DOC_COLS)

# Set global values for the PDF
pdf = utils.set_pdf_global_values()

# Starting row for the QR code
# Valid values: 0, 1, 2, 3
row_start = 0
# Starting column for the QR code
# Valid values: 0, 1, 2
col_start = 2

row_count = 0
i = 0

for row in range(0, rows_max):
    y_coord = (
        constants.MARGIN_T
        + (constants.CELL_H * row_count)
        + (constants.MARGIN_VERT * row_count)
    )
    # Check to see which row to start on
    if row_start <= row_count:
        col_count = 0
        for col in range(0, constants.DOC_COLS):
            x_coord = (
                (constants.MARGIN_L)
                + (constants.CELL_W * col_count)
                + (constants.MARGIN_HORIZ * col_count)
            )
            # check to see which column to start on
            if col_start <= col_count or i > 0:
                if i < len(commanders):
                    # Create the QR code image
                    img = utils.create_qrcode_image(commanders[i])

                    # Write image to disk
                    qr_code_file_name = (
                        "static/output/"
                        + commanders[i].name_slug
                        + "-"
                        + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                        + ".png"
                    )
                    img.save(qr_code_file_name)

                    # Draw mana symbol color blocks
                    utils.draw_mana_block(pdf, commanders[i], x_coord, y_coord)

                    # Add a rounded white box for the QR to sit on
                    pdf.set_draw_color(50, 50, 50)
                    pdf.set_fill_color(255, 255, 255)
                    pdf.rounded_rect(
                        x=x_coord + 5,
                        y=y_coord + 5,
                        w=114,
                        h=114,
                        r=5,
                        style="FD",
                        corners="1234",
                    )

                    # Overlay the QR code image
                    pdf.image(
                        qr_code_file_name,
                        x=x_coord + 7.5,
                        y=y_coord + 7.5,
                        w=109,
                        h=109,
                    )

                    # Add text at the bottom
                    pdf.set_xy(x_coord + 5, y_coord + 128)
                    pdf.set_text_color(
                        constants.TEXT_COLOR["r"],
                        constants.TEXT_COLOR["g"],
                        constants.TEXT_COLOR["b"],
                    )
                    pdf.cell(txt=commanders[i].name, align="C")

                    i += 1
            col_count += 1
    row_count += 1

# Write the PDF to disk
pdf_file_name = (
    "qrcodes" + "-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".pdf"
)
pdf.output("static/output/" + pdf_file_name)
