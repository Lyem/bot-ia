from .html_generation import generate_html
import pdfkit
import os

class Pdf_generator:
    def execute(self, plan: str, price: str, chat_id: str) -> str:
        path = os.path.join(os.getcwd(), 'src', 'core',
                            'boleto', 'infra', 'pdf', 'pdfkit')
        pdfkit.from_string(generate_html(price, plan), os.path.join(path, f'{chat_id}.pdf'))
        return os.path.join(path, f'{chat_id}.pdf')
