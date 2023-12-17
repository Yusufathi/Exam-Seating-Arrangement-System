from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class SeatingView:

    def __init__(self):
        pdf_output = './outputs/output.pdf'

        courseName = "Fundamentals of Programming II"
        courseCode = "CSC201"
        examDate = "10:30-Monday-12/17/23"
        examRoom = "G2-4011"

        studentList = [
            ['Seating#', 'ID', 'Name', 'Signature'],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
            [1, 41710155, 'Yusuf Fathi Mohammed', "             "],
        ]

        self.generate_pdf(pdf_output, courseName, courseCode,
                          examDate, examRoom, studentList)
        print(f"PDF generated: {pdf_output}")

    def generate_pdf(self, output_file, courseName, courseCode, examDate, examRoom, studentList):
        left_margin = 36
        right_margin = 36
        top_margin = 36
        bottom_margin = 36
        col_width = [55, 65, 190, 200]
        

        pdf = SimpleDocTemplate(output_file, pagesize=A4,
                                leftMargin=left_margin,
                                rightMargin=right_margin,
                                topMargin=top_margin,
                                bottomMargin=bottom_margin)
        content = []
        styles = getSampleStyleSheet()
        
        
        courseNameParagraph = Paragraph(
            "Course Name: "+courseName, styles['Heading4'])
        content.append(courseNameParagraph)

        courseCodeParagraph = Paragraph(
            "Course Code: "+courseCode, styles['Heading4'])
        content.append(courseCodeParagraph)

        courseDateParagraph = Paragraph(
            "Exam Date: "+examDate, styles['Heading4'])
        content.append(courseDateParagraph)

        courseRoomParagraph = Paragraph(
            "Exam Room: "+examRoom, styles['Heading4'])
        content.append(courseRoomParagraph)

        content.append(Paragraph("<br/><br/>", styles['Normal']))

        data_style = [('GRID', (0, 0), (-1, -1), 1, colors.black),('FONTSIZE', (0,0), (-1,0), 11)]

        content.append(
            Table(studentList, style=data_style, colWidths=col_width,rowHeights = 25))
        
        content.append(Paragraph("<br/><br/>", styles['Normal']))
        content.append(Paragraph("<br/><br/>", styles['Normal']))

        attParagraph = Paragraph(
            "Att. : ", styles['Heading4'])
        content.append(attParagraph)

        absParagraph = Paragraph(
            "Abs. : ", styles['Heading4'])
        content.append(absParagraph)

        proctorsParagraph = Paragraph(
            "Proctors : ", styles['Heading4'])
        content.append(proctorsParagraph)

        
        pdf.build(content)


    

       
