from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_certificate(student_name):
    filename = f"{student_name}_certificate.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 700, "Certificate of Achievement")
    c.setFont("Helvetica", 20)
    c.drawCentredString(300, 650, f"Presented to {student_name}")
    c.showPage()
    c.save()
