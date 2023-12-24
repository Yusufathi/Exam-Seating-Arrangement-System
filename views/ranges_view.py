from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
from services.time_services import get_date_time_str, getDate


class RangesView:

    def __init__(self, courseName, courseCode, roomsAndRanges):

        pdf_file_name = f'ranges.pdf'
        output_directory = f'./outputs/{getDate()}/{courseName}'
        pdf_output = os.path.join(output_directory, pdf_file_name)
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        self.generate_pdf(pdf_output, courseName, courseCode, roomsAndRanges)

    def generate_pdf(self, output_file, courseName, courseCode, roomsAndRanges):
        left_margin = 36
        right_margin = 36
        top_margin = 36
        bottom_margin = 36
        col_width = [50, 100, 100, 100, 80]

        pdf = SimpleDocTemplate(output_file, pagesize=A4,
                                leftMargin=left_margin,
                                rightMargin=right_margin,
                                topMargin=top_margin,
                                bottomMargin=bottom_margin)

        styles = getSampleStyleSheet()
        content = []

        courseNameParagraph = Paragraph(
            "Course Name: "+courseName, styles['Heading4'])
        content.append(courseNameParagraph)

        courseCodeParagraph = Paragraph(
            "Course Code: "+courseCode, styles['Heading4'])
        content.append(courseCodeParagraph)

        content.append(Paragraph("<br/><br/>", styles['Normal']))

        data_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),
                      ('FONTSIZE', (0, 0), (-1, 0), 11)]

        content.append(
            Table(roomsAndRanges, style=data_style, colWidths=col_width, rowHeights=25))

        content.append(Paragraph("<br/><br/>", styles['Normal']))
        content.append(Paragraph("<br/><br/>", styles['Normal']))

        pdf.build(content)


# courseName = "Fundamentals of Programming II"
        # courseCode = "CSC201"
        # roomsAndRanges = [
        #     ['index#', 'Room', 'Start ID', 'End ID', 'Capacity'],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40],
        #     [1, 'Hall 8-4238', 42020005, 42020008, 40]
        # ]
