# ex-06.py

if __name__ == '__main__':
    
    data = {
        'backend': 'Python',
        'frontend': 'VueJS',
        'database': 'PostgreSQL',
        'cache': 'Redis',
        'queue': 'RabbitMQ'}

    for chave, valor in data.items():
        print(f'* {chave}: {valor}')
