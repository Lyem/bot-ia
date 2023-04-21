from core.__seedwork.application.use_cases import UseCase
from core.boleto.infra.pdf.pdfkit.generate_pdf import Pdf_generator


class Generate_pdf(UseCase):

    def execute(self, chatId: str, plan: str):
        if plan == '200':
            price = 20
        elif plan == '400':
            price = 50
        else:
            price = 99
        return Pdf_generator().execute(f'{plan}Mb', price, chatId)
