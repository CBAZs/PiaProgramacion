from pyhunter import PyHunter
from datetime import datetime


def hunter_mail(api, company, number):
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    try:
        hunter = PyHunter(api)
        result = hunter.domain_search(company=company, limit=10)
        
        with open('correos.txt','a') as f:
            f.write(date)
            f.write('\n')
            counter = 0
            
            for i in range(int(number)):
                if (result['emails'][i]['first_name'] is not None):
                    info = ('[+] '+result['emails'][i]['first_name']+' '+result['emails'][i]['last_name']+': '+result['emails'][i]['value'])
                    counter += 1
                    f.write('%s\n' %info)
                    with open('logs.info', 'a') as j:
                        j.write(f'[{date} HUNTER]: Se ha recuperado un correo\n')
       
        with open('logs.info', 'a') as j:
            j.write(f'[{date} HUNTER]: Se guardaron ' + str(counter) + ' correos.\n')
        print('\nSe guardaron ',counter,' correos.')
    except Exception as e:
        with open('logs.info', 'a') as j:
            j.write(f'[{date} HUNTER ERROR]: {e}\n')
        print('Error:', e)

