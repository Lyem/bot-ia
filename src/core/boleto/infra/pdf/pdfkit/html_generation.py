def generate_html(price: str, plan: str):
    return '''
            <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Exemplo de Boleto</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    font-size: 12px;
                }

                #boleto {
                    width: 650px;
                    padding: 10px;
                    border: 1px solid #000;
                }

                #logo {
                    float: left;
                    width: 150px;
                    margin-right: 20px;
                }

                #logo img {
                    max-width: 100%;
                }

                #endereco {
                    float: left;
                    width: 250px;
                }

                #instrucoes {
                    float: right;
                    width: 200px;
                    text-align: right;
                }

                table {
                    width: 100%;
                    margin-top: 20px;
                    border-collapse: collapse;
                }

                table td, table th {
                    padding: 5px;
                    border: 1px solid #000;
                    text-align: center;
                }

                table th {
                    background-color: #eee;
                }

                #total {
                    margin-top: 20px;
                    text-align: right;
                    font-weight: bold;
                    font-size: 16px;
                    border-top: 1px solid #000;
                    padding-top: 5px;
                }

                #codigo {
                    margin-top: 20px;
                    border-top: 1px solid #000;
                    padding-top: 5px;
                    text-align: center;
                    font-size: 14px;
                }
            </style>
        </head>''' + f'''
        <body>
            <div id="boleto">
                <div id="logo">
                    <img src="https://media.discordapp.net/attachments/1098759004425040006/1098776050265227274/logo.jpg" alt="Logo">
                </div>
                <div id="endereco">
                    <p>Cat Net</p>
                    <p>Endereço da Empresa</p>
                    <p>Cidade/Estado - CEP</p>
                    <p>CNPJ: 00.000.000/0000-00</p>
                </div>
                <div id="instrucoes">
                    <p><strong>Boleto</strong></p>
                    <p>Pagamento até a data de vencimento</p>
                    <p>Não receber após o vencimento</p>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th>Descrição</th>
                            <th>Quantidade</th>
                            <th>Valor Unitário</th>
                            <th>Valor Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{plan}</td>
                            <td>1</td>
                            <td>R$ {price}</td>
                        </tr>
                    </tbody>
                </table>
                <div id="total">
                    Total: R$ {price}
                </div>
                <div id="codigo">
                    
        <img alt='Barcode Generator TEC-IT'
            src='https://barcode.tec-it.com/barcode.ashx?data=ABC-abc-1234&code=Code128&translate-esc=on'/>
                </div>
            </div>
        </body>
        </html>
    '''
