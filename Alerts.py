"""
Arquivo para demostrar a intenção de enviar alertas com base na porcentagem de presença dos alunos.
Este código envia um e-mail de alerta para o conselho tutelar responsável quando a porcentagem de presença de um aluno cai abaixo de 50% e
uma mensagem no WhatsApp para o responsável do aluno quando a porcentagem de presença cai abaixo de 75%.
Ele utiliza o servidor SMTP do Gmail com exemplo para enviar e-mail.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com' # Exemplo com o servidor SMTP do Gmail
smtp_port = 587
smtp_username = '' # Armazene em variáveis de ambiente
smtp_password = ''  # Use uma senha de aplicativo

def enviar_alerta_presenca(nome):
    # Informações do e-mail
    from_addr = ''# E-mail da instituição aqui:
    to_addr = '' # E-mail do conselho tutelar aqui:
    subject = 'Comunicação de Aluno com Presença Escolar Abaixo do Mínimo' #corpo do e-mail
    body = 'Prezado(a) Conselheiro(a) Tutelar,\n\n' 
    body += f'Gostaríamos de informar que o(a) aluno(a) {nome}, está com a frequência escolar abaixo de 50% no presente semestre letivo, conforme o acompanhamento realizado pela nossa instituição.\n\n'
    body += 'Considerando a importância da assiduidade para o desenvolvimento educacional e social do(a) estudante, solicitamos a gentileza de que sejam tomadas as medidas cabíveis para verificar e, se necessário, intervir no caso, a fim de garantir o direito à educação e o acompanhamento adequado do aluno.\n\n'
    body += 'Estamos à disposição para fornecer quaisquer informações adicionais ou documentação que se fizer necessária.\n\n'
    body += 'Agradecemos pela atenção e colaboração.'


    # Configurar a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Enviar o e-mail
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("E-mail enviado com sucesso!")
        server.quit()
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")



"""
função para enviar alerta via WhatsApp quando a porcentagem de presença do aluno cai abaixo de 75%.
A função utiliza a biblioteca pywhatkit para enviar uma mensagem instantânea.
A intenção é notificar o responsável do aluno sobre a baixa frequência escolar.
"""

import pywhatkit as kit
def enviar_alerta_whatsapp(nome, numero_responsavel):
    mensagem = f"Alerta: O aluno {nome} está com a frequência escolar abaixo de 75%."
    try:
        kit.sendwhatmsg_instantly(f"+55{numero_responsavel}", mensagem)
        print("Mensagem enviada com sucesso via WhatsApp!")
    except Exception as e:
        print(f"Erro ao enviar mensagem via WhatsApp: {e}")