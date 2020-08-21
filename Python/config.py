import os


class Config:
    RABBITMQ_HOST = os.getenv('RABBIT_HOST', '10.202.232.219')
    RABBITMQ_PORT = os.getenv('RABBIT_PORT', '5672')
    RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', '/')
    RABBITMQ_EXCHANGE = os.getenv('RABBITMQ_EXCHANGE', 'adapter-outbound-exchange')
    RABBITMQ_USER = os.getenv('RABBIT_USER', 'admin')
    RABBITMQ_PASSWORD = os.getenv('RABBIT_PASSWORD', )
    RABBITMQ_QUEUENAME= os.getenv('RABBIT_QUEUENAME', 'RM.Field')
    
    
    CASES_TO_FETCH = os.getenv("CASES_TO_FETCH", "10")
    UPDATE_CASES_TO_FETCH = os.getenv("UPDATE_CASES_TO_FETCH", "20")
    OUTCOME_CASES_TO_FECTH = os.getenv("OUTCOME_CASES_TO_FECTH", "1000")
    TMMOCK_API_URL = os.getenv("tm-base-url", "http://fwmtgatewaytmmock:8000/cases/")
