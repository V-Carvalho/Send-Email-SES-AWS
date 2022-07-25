import boto3

# Criando client
ses = boto3.client(
    service_name='ses',
    region_name='us-west-2',
    aws_access_key_id='KEY',
    aws_secret_access_key='KEY'
)

# Enviando o email através do serviço SES da AWS #
response = ses.send_email(
    Destination={
        'ToAddresses': [
            'EMAIL',  # Email que vai receber
        ],
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'utf-8',
                'Data': 'Email enviado usando o serviço SES (Simple Email Service) da AWS',  # Texto do Email
            },
        },
        'Subject': {
            'Charset': 'utf-8',
            'Data': 'SES - AWS',  # Assunto do Email
        },
    },
    Source='EMAIL'  # Email que vai fazer o envio
)

print("Email enviado: " + response['MessageId'])
